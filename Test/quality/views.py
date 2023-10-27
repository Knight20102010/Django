from django.shortcuts import render
from django.http import HttpResponse
import os, time

def hello(request):
    return render(request, 'hello.html')



"""
employee = {"1123":"Jozef Petras","1124":"Rastislav Guláš","1125":"Mária Surová", "1126":"Júlia Kocáková"}

def looking_name():
    x = input("Zadaj cislo ID > ")
    if x in employee:
        return HttpResponse(employee[x])
    else:
        return HttpResponse("ID číslo sa nenachádza v zozname!!!")
    
def adding_name():
    y = input("Zadaj ID cislo > ")
    z = input("Zadaj zamestnanca > ")  
    if y in employee:
        return "ID je už vytvorené!!!"
    else:    
        u = employee[y] = z 
        return u
  


while True:
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    menu = input(("1. View \n2. Add\n>"))
    if menu == "1":
        print(looking_name())
    elif menu == "2":
        print(adding_name())  
    else:
        print("Vyber si z ponuky 1 - View alebo 2 - Add")    
"""

# Create your views here.
