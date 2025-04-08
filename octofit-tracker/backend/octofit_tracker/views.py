from rest_framework import viewsets
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['mydatabase']

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = db.users.find()
        return Response(list(users))

    def retrieve(self, request, pk=None):
        user = db.users.find_one({'_id': ObjectId(pk)})
        return Response(user)

class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        teams = db.teams.find()
        return Response(list(teams))

    def retrieve(self, request, pk=None):
        team = db.teams.find_one({'_id': ObjectId(pk)})
        return Response(team)

class ActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        activities = db.activities.find()
        return Response(list(activities))

    def retrieve(self, request, pk=None):
        activity = db.activities.find_one({'_id': ObjectId(pk)})
        return Response(activity)

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        leaderboards = db.leaderboards.find()
        return Response(list(leaderboards))

    def retrieve(self, request, pk=None):
        leaderboard = db.leaderboards.find_one({'_id': ObjectId(pk)})
        return Response(leaderboard)

class WorkoutViewSet(viewsets.ViewSet):
    def list(self, request):
        workouts = db.workouts.find()
        return Response(list(workouts))

    def retrieve(self, request, pk=None):
        workout = db.workouts.find_one({'_id': ObjectId(pk)})
        return Response(workout)
