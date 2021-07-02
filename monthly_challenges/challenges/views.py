from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string



monthly_challenge_list = {
    'january':'Eat no meat for entire month',
    'february':'Walk for 20 mins everyday',
    'march':'Learn django 20 mins daily',
    'april':'Eat no meat for entire month',
    'may':'Walk for 20 mins everyday',
    'june':'Learn django 20 mins daily',
    'july':'Eat no meat for entire month',
    'august':'Walk for 20 mins everyday',
    'september':'Learn django 20 mins daily',
    'october':'Eat no meat for entire month',
    'november':'Walk for 20 mins everyday',
    'december': 'Learn django 20 mins daily'
}
# Create your views here.
def index(request):
    months = list(monthly_challenge_list.keys())

    return render(request,"challenges/index.html",{
        "months":months,
    })


def monthly_challenges_by_number(request, month):
    try:
        months = list(monthly_challenge_list.keys())
        redirect_month = months[month-1]

        redirect_path = reverse("month-challenge",args = [redirect_month])

        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("<h1>This is an invalid month number</h1>")

        

def monthly_challenges(request, month):
    try:
        challenge_text = monthly_challenge_list[month]
        return render(request,"challenges/challenge.html",{
            'text':challenge_text,
            'month_name':month,
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("<h1>This is an invalid month</h1>")



