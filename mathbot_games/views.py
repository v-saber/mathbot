from django.shortcuts import render

# Create your views here.

def mathbotGames(request):
    return render(request, 'games/index.html')
def mathbotGamess(request):
    return render(request, 'games/1/math-battle.html')

