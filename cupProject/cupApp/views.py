from django.shortcuts import render
from django.http import HttpResponse
from .models import Cup
# Create your views here.
def index(request):
    return HttpResponse("Test URL")

#these two functions work in the same way with just inline calling for the numbers not a big issue
def hello(request , name):
    return HttpResponse(f'hello {name}')

def timesTwo(request, number):
    return HttpResponse(f'The product of your number times 2 is: {number*2}')

def total(request, number):
    printNumber = 0
    for x in range(number+1): #have to add [+1} in order to get the number
        printNumber += x

    return HttpResponse(f' the sum of numbers from 0 to {number} is : {printNumber}')
#adds new cup that is fixed
def newCup(request):
    Cup.objects.create(name = 'Fancy',material= 'Glass' , manufactuerDate = '2017-04-22')
    return HttpResponse('boop new cup found!!!')
# competely lists all cups by name
def cupView(request):
    namePrint = ''
    cupList = Cup.objects.all()
    for cup in cupList:
        namePrint += f'{cup} <br>'

    return HttpResponse(namePrint)
# updates all cups after a date with different material
def updateCup(request):
    cupList = Cup.objects.all()
    Cup.objects.filter(manufactuerDate__gt = '2012-01-01').update(material = 'Slightly New')
    print(cupList)

    return HttpResponse('cup list updated')

# retrives all cups and cups by filter for for use in html page
def cupIndex(request):
    cupList = Cup.objects.all()
    after2012 = Cup.objects.filter(manufactuerDate__gt = '2012-01-01') # completed all problems in exercise 3
    context ={'allCups': cupList, 'newCups': after2012 , 'name':"Thomas"}
# context to send ti html page
    return render(request, 'cupApp/index.html',context)