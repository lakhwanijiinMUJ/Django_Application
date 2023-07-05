from django.contrib.auth import authenticate
from django.shortcuts import render, redirect

from .forms import RegistrationForms
from .models import User_Data,Scores
from django.core.mail import EmailMessage
from django.contrib import messages
import datetime

def signin(request):
    if request.method == "POST":
        email=request.POST.get("email")
        password=request.POST.get("password")
        results=User_Data.objects.raw("select * from login_user_data")
        results2=User_Data.objects.raw("select * from login_scores")
        for result in results:
            if(result.email==email and result.password==password):
                request.session["user_name"]=result.first
                request.session["email"]=result.email
                for result in results2:
                    if(result.email==email):
                        request.session["level"]=result.currentlevel
                        request.session["id"]=result.id
                        return redirect("answers")
    return render(request,"signin.html")

def signup(request):
    if request.method == "POST":
        first_name=request.POST.get("first")
        last_name = request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        repassword=request.POST.get("repassword")
        date=request.POST.get("date")
        if(password!=repassword):
            messages.success(request,"Your Password does not match")
        message_body=f"Your form has been submitted Successfully \nThank you {first_name} {last_name}"
        email_message=EmailMessage("Form Submission Confirmation",message_body,to=[email])
        email_message.send()
        User_Data.objects.create(first=first_name, last_name=last_name, email=email, password=password,
                                date=date)
        current_datetime = datetime.datetime.now()
        Scores.objects.create(first=first_name,email=email,currentlevel=1,score=0,time=current_datetime.strftime("%X"))

        messages.success(request,"Form Submitted Successfully \n Confirmation Mail is Sent")
    return render(request,"signup.html")

def answers(request):
    if request.method=="POST":
        answer=request.POST.get("answer")
        level=request.session["level"]
        time=request.POST.get("date")
        id=request.session["id"]
        if(answer=="Love1" and level=="1"):
            level="2"
            messages.success(request,"Your Answer is correct \n Pls signin again")
        elif(answer=="Love2" and level=="2"):
            level="3"
            messages.success(request, "Your Answer is correct \n Pls signin again")
        elif(answer=="Love3" and level=="4"):
            level="4"
            messages.success(request, "Your Answer is correct \n Pls signin again")
        else:
            messages.success(request, "Your Answer is Incorrect \n Pls signin again")
        user=Scores.objects.get(id=id)
        user.currentlevel=level
        user.score=user.score+100
        user.time=time
        user.save()
    data={"user_name":request.session["user_name"],
             "email":request.session["email"],
             "level":request.session["level"]}
    context={"data":data}

    return render(request,"answers.html",context)