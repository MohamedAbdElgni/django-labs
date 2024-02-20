from django.shortcuts import render


data=[
    {
        'id':1,
        'name':'Python',
        'details':'Python is a programming language',
        'duration':'3 months',
        'subtracks':['Python Basics','Python Advanced','django','flask','sqlalchemy']
    },
    {
        'id':2,
        'name':'JavaScript',
        'details':'JavaScript is a programming language',
        'duration':'3 months',
        'subtracks':['JavaScript Basics','JavaScript Advanced','React','Angular','Vue']
    },
    {
        'id':3,
        'name':'Sql',
        'details':'Sql is a programming language',
        'duration':'3 months',
        'subtracks':['Sql Basics','Sql Advanced','Mysql','Postgres','Sqlite']
    },
]



def Tracks(request):
    return render(request, 'tracks/Tracks.html' , context={'data':data})

def TrackDetails(request, id):
    track = {}
    for d in data:
        if d['id'] == id:
            track = d
    return render(request, 'tracks/TrackById.html' , context={'track':track})