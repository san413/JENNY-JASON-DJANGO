from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
def our_story(request):
    return render(request, 'our_story.html')

