from django.shortcuts import render

# Create your views here.

def mathbotHome(request):
    return render(request, 'mathbot_home/index.html')
def mathbotCalc(request):
    return render(request, 'mathbot_calculator/index.html')
def mathbotCont(request):
    return render(request, 'mathbot_contact/index.html')
def mathbotForum(request):
    return render(request, 'mathbot_forum/index.html')
def mathbotAsk(request):
    return render(request, 'mathbot_forum/ask/index.html')
def mathbotQues(request):
    return render(request, 'mathbot_forum/questions/1354628/index.html')