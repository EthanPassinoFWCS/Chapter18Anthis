from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def index(request):
    """The home page for Learning Log."""
    return render(request, 'pizzas/index.html')
