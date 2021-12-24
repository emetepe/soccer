from django.core.management.base import BaseCommand, CommandError

from teams.models import Team, Stadium

import pandas as pd

class Command(BaseCommand):
    help = '''
        Loads teams from ./data/table_teams.csv file
    '''

    def handle(self, *args, **options):
        filepath = './data/table_teams.csv'
        df = pd.read_csv(filepath, sep=';', encoding='latin-1')
        for index, row in df.iterrows():
            
            # Create Stadium
            new_stadium = Stadium(
                name = row['stadium'],
                pic = row['stadium_pic']
            )
            new_stadium.save()

            # Create Team
            new_team = Team(
                name=row['team'],
                coach_name=row['coach'],
                coach_pic=row['coach_pic'],
                emblem_pic=row['emblem_pic'],
                shirt_pic=row['tshirt_pic'],
                description='',
                stadium=new_stadium
            )
            new_team.save()
            self.stdout.write(self.style.SUCCESS('Successfully {} team add'.format(new_team.name)))