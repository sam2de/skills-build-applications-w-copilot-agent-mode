from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **options):
        # Clear existing data
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Create teams
        marvel = Team.objects.create(name='Marvel', description='Marvel Superheroes')
        dc = Team.objects.create(name='DC', description='DC Superheroes')

        # Create users
        users = [
            User(name='Spider-Man', email='spiderman@marvel.com', team='Marvel', is_superhero=True),
            User(name='Iron Man', email='ironman@marvel.com', team='Marvel', is_superhero=True),
            User(name='Wonder Woman', email='wonderwoman@dc.com', team='DC', is_superhero=True),
            User(name='Batman', email='batman@dc.com', team='DC', is_superhero=True),
        ]
        User.objects.bulk_create(users)

        # Create activities
        activities = [
            Activity(user='Spider-Man', activity_type='Swinging', duration=60),
            Activity(user='Iron Man', activity_type='Flying', duration=45),
            Activity(user='Wonder Woman', activity_type='Running', duration=30),
            Activity(user='Batman', activity_type='Martial Arts', duration=50),
        ]
        Activity.objects.bulk_create(activities)

        # Create leaderboard
        Leaderboard.objects.create(team='Marvel', points=200, rank=1)
        Leaderboard.objects.create(team='DC', points=180, rank=2)

        # Create workouts
        workouts = [
            Workout(name='Pushups', description='Upper body strength', difficulty='Easy'),
            Workout(name='Sprints', description='Speed training', difficulty='Medium'),
        ]
        Workout.objects.bulk_create(workouts)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
