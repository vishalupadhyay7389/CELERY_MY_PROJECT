from django.shortcuts import render
from myceleryproject.celery import add
from myapp.tasks import sub
from time import sleep
from celery.result import AsyncResult

# Create your views here.

# def index(request):
#     print("Result: ")
#     result_1 = add.delay(10 , 20)
#     print("Result 1 : = " , result_1)
#     result_2 = sub.delay(100 , 20)
#     print("Result 2 : = " , result_2)
#     return render (request,"myapp/home.html")

###### Enqueue task using apply_assync ############
# def index(request):
#     print("Result: ")
#     result_1 = add.apply_async(args =[10 , 20])
#     print("Result 1 : = " , result_1)
#     result_2 = sub.apply_async(args =[100 , 20])
#     print("Result 2 : = " , result_2)
#     return render (request,"myapp/home.html")

#################### Display Addition value After task Excution #########################

def index(request):
    result = add.delay(100,30)
    # print("Ready : " , result.ready())
    # print("Succeful : " , result.successful())
    # print("Failed : " , result.failed())
    return render(request , 'myapp/home.html' , {'result':result})

def check_result(request , task_id):
    result = AsyncResult(task_id)
    return render(request ,'myapp/result.html' , {'result':result})

def about(request):
    print("Result: ")
    return render (request,"myapp/about.html")

def contact(request):
    print("Result: ")
    return render (request,"myapp/contact.html")
