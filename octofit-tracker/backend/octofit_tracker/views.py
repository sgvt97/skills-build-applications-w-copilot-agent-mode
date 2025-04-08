from rest_framework import viewsets
from rest_framework.response import Response
from pymongo import MongoClient
from bson import ObjectId
from django.http import JsonResponse

client = MongoClient('mongodb://localhost:27017/')
db = client['octofit_db']

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

def api_root(request):
    base_url = 'https://improved-robot-w45v6j9wgxj3g4vq-8000.app.github.dev/'
    return JsonResponse({
        'users': base_url + 'users/',
        'teams': base_url + 'teams/',
        'activities': base_url + 'activities/',
        'leaderboard': base_url + 'leaderboard/',
        'workouts': base_url + 'workouts/'
    })
