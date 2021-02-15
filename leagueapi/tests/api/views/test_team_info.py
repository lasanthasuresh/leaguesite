from django.test import TestCase
from model_bakery import baker
from pprint import pprint

from leagueapi.api.views.team_info import find_players_by_average_score


class TestPlayerModel(TestCase):

    def test_animals_can_speak(self):
        mock_players = create_mock_players()
        filtered_players = find_players_by_average_score(mock_players, 0.9)
        pprint(list(map(lambda x: x.name, filtered_players)))


def create_mock_players():
    return [
        MockPlayer(name="A", average_score=2.262480205),
        MockPlayer(name="B", average_score=3.465466617),
        MockPlayer(name="C", average_score=1.875181453),
        MockPlayer(name="D", average_score=0.9928443913),
        MockPlayer(name="E", average_score=7.981496043),
        MockPlayer(name="F", average_score=2.840561369),
        MockPlayer(name="G", average_score=6.427145857),
        MockPlayer(name="H", average_score=1.599412438),
        MockPlayer(name="I", average_score=7.103868961),
        MockPlayer(name="J", average_score=3.213308054),
        MockPlayer(name="L", average_score=9.867085349),
        MockPlayer(name="M", average_score=6.753272008),
        MockPlayer(name="N", average_score=3.859599519),
        MockPlayer(name="O", average_score=2.30074085),
        MockPlayer(name="P", average_score=9.064418045),
        MockPlayer(name="Q", average_score=7.859625553),
        MockPlayer(name="R", average_score=5.444561662),
        MockPlayer(name="S", average_score=9.042559633),
        MockPlayer(name="T", average_score=6.226819994),
        MockPlayer(name="U", average_score=0.8084111076),
        MockPlayer(name="V", average_score=3.745269993),
        MockPlayer(name="W", average_score=4.400250222),
        MockPlayer(name="X", average_score=5.429413445),
        MockPlayer(name="Y", average_score=8.136532215),
        MockPlayer(name="Z", average_score=4.557663266),
    ]


class MockPlayer:
    def __init__(self, name, average_score):
        self.average_score = average_score
        self.name = name

    def __str__(self):
        return f"{self.name} -  {self.average_score}"
