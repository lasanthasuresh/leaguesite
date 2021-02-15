import logging
from datetime import datetime
from random import random, randint

from django.contrib.auth.models import User, Group
from django.core.management.base import BaseCommand

from leagueapi.management.commands.dummydata import team_names, fname_lname_pairs
from leagueapi.models import Team, Coach, Player, Tournament, Round, RoundGroup, Game, GamePlayerScore, \
    GameTeamStatistics, UserSession, UserProfile, Admin

logger = logging.getLogger(__name__)

def create_game_and_get_winning_team(group, teamA, teamB, game_name):
    game = Game.objects.create(game_name=game_name, group=group)
    game.save()
    team_a_stats = create_game_team_stats(teamA, game, 0)
    team_b_stats = create_game_team_stats(teamB, game, team_a_stats.final_score)

    team_a_won = team_a_stats.final_score > team_b_stats.final_score
    update_team_stats(teamA, team_a_stats, team_a_won)
    update_team_stats(teamB, team_b_stats, not team_a_won)

    team_a_stats.save()
    team_b_stats.save()

    return teamA if team_a_won else teamB


def update_team_stats(team, team_stats, won):
    team.average_score = ((team.average_score * team.number_of_games) + team_stats.final_score) / (
            team.number_of_games + 1)
    team.number_of_games += 1

    team_stats.is_won_team = won

    if won:
        team.number_of_wins += 1


def create_game_team_stats(team, game, prev_score):
    team = Team.objects.get(pk=team.pk)
    total_score = 0

    last_team_player_score = None

    for player in team.players.all():
        score = randint(1, 25)
        total_score += score
        team_player_score = GamePlayerScore.objects.create(player=player, game=game, score=score)
        team_player_score.save()
        last_team_player_score = team_player_score

    # to avoid the both teams to have the same final_score
    if total_score == prev_score:
        last_team_player_score.score += 5
        last_team_player_score.save()
        total_score += 5

    return GameTeamStatistics.objects.create(team=team, game=game, final_score=total_score)


def create_round_and_get_winning_teams(round_name, tournament, teams, group_count):
    round = Round.objects.create(round_name=round_name, tournament=tournament)
    qualified_teams = []

    for g_i in range(group_count):
        group = RoundGroup.objects.create(group_name=f"Group-{g_i+1}", round=round)
        group.save()
        group_teams = teams[g_i * group_count: (g_i + 1) * group_count]

        game_id = 1

        # ensure the values set in previous rounds are cleared.
        for team in group_teams:
            team.win_counts_in_group = 0

        for teamA in group_teams:
            for teamB in group_teams:
                if teamA != teamB:
                    winning_team = create_game_and_get_winning_team(group, teamA, teamB,
                                                                    f"{group.group_name}-Game-{game_id}")
                    winning_team.win_counts_in_group += 1
                    game_id += 1

        group_teams.sort(key=lambda t: t.win_counts_in_group, reverse=True)

        for selected_team in group_teams[:len(group_teams) // 2]:
            qualified_teams.append(selected_team)

    for qualified_team in qualified_teams:
        round.qualified_teams.add(qualified_team)

    round.save()

    return qualified_teams


def create_dataset_with_groups():

    logger.info("Init...")
    create_admin_user()

    teams = create_teams()
    logger.info("Teams Created...")

    tournament = Tournament.objects.create(name="AL2021", description="Awesome League - 2021", date=datetime.today())
    tournament.save()
    logger.info("Tournament Created...")

    teams = create_round_and_get_winning_teams('First Round', tournament, teams, 4)
    logger.info("First round data loaded...")

    teams = create_round_and_get_winning_teams('Second Round', tournament, teams, 2)
    logger.info("Second round data loaded...")

    teams = create_round_and_get_winning_teams('Semi Finals', tournament, teams, 1)
    logger.info("Semi Final round data loaded...")

    teams = create_round_and_get_winning_teams('Finals', tournament, teams, 1)
    logger.info("Final round data loaded...")


def create_dataset_without_groups():
    teams = create_teams()

    pass


def create_teams():
    teams = []
    team_player_count = 10
    team_count = 16

    coach_group = Group.objects.create(name='COACH')
    coach_group.save()

    player_group = Group.objects.create(name='PLAYER')
    player_group.save()

    for index in range(team_count):
        name_pair = fname_lname_pairs[index * (team_player_count + 1)]
        user = create_user(name_pair, [coach_group])
        coach = Coach.objects.create(username=user.username, user=user)
        coach.save()

        team_name = team_names[index]
        team = Team.objects.create(team_name=team_name, coach=coach)
        team.save()
        teams.append(team)

        for player_index in range(team_player_count):
            name_pair = fname_lname_pairs[index * (team_player_count + 1) + player_index + 1]
            user = create_user(name_pair, [player_group])

            height = 1.76 + (0.4 * random())
            player = Player.objects.create(username=user.username, user=user, team=team, height=height)
            player.save()

    return teams


def create_user(name_pair, groups):
    username = "{fname}.{lname}".format(fname=name_pair[0], lname=name_pair[1]).lower()
    email = "{username}@awesomeleague.com".format(username=username)
    password = "{fname}123".format(fname=name_pair[0]).lower()
    user = User.objects.create_user(username=username, email=email, password=password)
    user.first_name = name_pair[0]
    user.last_name = name_pair[1]

    for group in groups:
        user.groups.add(group)

    user.save()
    return user


def create_admin_user():
    admin_group = Group.objects.create(name="ADMIN")
    admin_group.save()

    admin_user = User.objects.create_user('admin', 'admin@awesomeleague.com', 'awesomeleague1234',
                                          first_name='Franklin', last_name='Harlow')
    admin_user.groups.add(admin_group)
    admin_user.save()

    admin_profile = Admin.objects.create(username='admin', user=admin_user)
    admin_profile.save()


def delete_all_existing():
    GamePlayerScore.objects.all().delete()
    GameTeamStatistics.objects.all().delete()
    Player.objects.all().delete()
    UserSession.objects.all().delete()
    Admin.objects.all().delete()
    Game.objects.all().delete()
    RoundGroup.objects.all().delete()
    Round.objects.all().delete()
    Tournament.objects.all().delete()
    Team.objects.all().delete()
    Coach.objects.all().delete()
    User.objects.all().delete()
    Group.objects.all().delete()


class Command(BaseCommand):
    help = 'Imports a sample configuration/data set. \n' \
           'There are two flavours of sample configurations. With groups and without groups within a round.\n' \
           '    0 - dataset with grouping inside a round\n' \
           '    1 - dataset with no grouping inside a round\n'

    def handle(self, *args, **options):
        type = 0

        delete_all_existing()

        if type is None:
            type = 0

        if type == 0:
            create_dataset_with_groups()
        else:
            create_dataset_without_groups()
