

from django.shortcuts import render

def homepage(request):
    return render(request, 'myapp1/homepage.html', {'message': 'Welcome to my website!'})

def form_page(request):
    if request.method == 'POST':
        # Handle form submission here
        pass
    else:
        return render(request, 'myapp1/form_page.html')