"""Platzigram views"""

# Django
from django.http import HttpResponse
from django.http import JsonResponse
# Utilities
from datetime import datetime

def hello_world(request):
    """Return a greeting."""
    return HttpResponse('Oh, hi! current server time is {}'.format(
        datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))

def sorted_numbers(request):
    numbers = request.GET['numbers']
    numbersList = numbers.split(",")

    for i in range( len(numbersList) - 1 ):
        for j in range( i, len(numbersList) - 1 ):
            if int( numbersList[i] ) > int( numbersList[j] ):
                actualNum = numbersList[j]
                numbersList[j] = numbersList[i]
                numbersList[i] = actualNum

    data = {
        'status': 'ok',
        'orderedNumbers': numbersList,
        'message': 'Integers sorted succesfully'
    }

    return JsonResponse(data, safe=False)

def greet_user(request, name, age):
    if age < 18:
        message = "Sorry {} you're not allowed to be here being under age".format(name)
    else:
        message = "Hi {}, welcome to Platzigram".format(name)

    return HttpResponse(message)