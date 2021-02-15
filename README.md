# leaguesite - Awesome League

LeagueSite is DRF based Python application, created for a coding assignment.

## Sample Data

In order to run the application, first makesure the database migrations are done.

```bash
python manage.py makemigrations
python manage.py migrate
```

Then, to feed the initial data, run load_sample_data management command.

```bash
python manage.py load_sample_data 
```


#### Users
load_sample_data will add 177 users to the table including admin, coaches and players.
Following is a sample of such users.

| user type | user name | email  | password  |
| ------------ | ------------ | ------------ | ------------ |
| admin  | admin  | admin@awesomeleague.com  |  awesomeleague1234 |
| coach | billy.cresswell  | billy.cresswell@awesomeleague.com  | billy123 |
| player | antone.amrhein  | antone.amrhein@awesomeleague.com  | antone123 |
| player | hans.stejskal  | hans.stejskal@awesomeleague.com  | hans123 |


#### The Game Structure

As there are 16 teams, if all the teams play with each other in the first round there would be 240 games in the first round. To reduce this count, an additional assumption is made, that the teams are played in groups inside a Round.

Ex.

In the First round:
- There are 4 groups that each containing 4 teams.
- Inside the group, teams play with each other. ( so there would be 12 games in a group, 48 games in the round )
- From a group, 2 teams are qualified for the second round.

Similarly the games goes as ,
- for the second round, there are 2 groups each containing 4 teams.
- for the semifinals 1 group with 4 teams
- for the finals, 1 group with 2 teams.

## Python
- Python version - 3.7.4


## What is included and what is missing
- [✓] Complete Object Model
- [✓] Requested APIs to view score-board, player-info, team-info and search players inside team
- [✓] Requested APIs to view usage statistics, currently online users.
- [✓] Role-based access control for the above APIs. ( used Django groups as roles )
- [✓] Separate CRUD API to control all the entity data.
- [✓] Used default Django privileges for CRUD API access control.
- [✕] Testing the CRUD API and its access control couldn't be completed.
- [✕] Code comments and refactoring isn't completed.
- [✕] Unit/Integration test coverage is low. 
 

