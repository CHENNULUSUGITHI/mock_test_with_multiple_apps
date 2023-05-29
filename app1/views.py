from django.shortcuts import render

# Create your views here.
def mock1(request):
    return render(request,'mock1.html')