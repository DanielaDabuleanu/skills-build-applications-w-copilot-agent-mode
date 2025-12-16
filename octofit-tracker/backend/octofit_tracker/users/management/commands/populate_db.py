from django.core.management.base import BaseCommand
from users.models import User
from activities.models import Activity
from django.db import connection

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Delete existing data
        User.objects.all().delete()
        Activity.objects.all().delete()
        # Add more deletions for other models as needed

        # Create teams
        marvel_team = 'Marvel'
        dc_team = 'DC'

        # Create users (super heroes)
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team=marvel_team),
            User(name='Iron Man', email='ironman@marvel.com', team=marvel_team),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team=dc_team),
            User(name='Batman', email='batman@dc.com', team=dc_team),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user=users[0], type='Running', duration=30),
            Activity(user=users[1], type='Cycling', duration=45),
            Activity(user=users[2], type='Swimming', duration=25),
            Activity(user=users[3], type='Yoga', duration=60),
        ]
        Activity.objects.bulk_create(activities)

        self.stdout.write(self.style.SUCCESS('Test data populated for users and activities.'))

        # Create unique index on email for users collection
        with connection.cursor() as cursor:
            cursor.execute('''db.users.createIndex({ "email": 1 }, { "unique": true })''')
        self.stdout.write(self.style.SUCCESS('Unique index created on email field for users collection.'))

        # Add similar logic for teams, leaderboard, workouts as needed
