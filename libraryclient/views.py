from django.shortcuts import render

# Create your views here.
def display_client(request):
    return render(request, 'client.html')