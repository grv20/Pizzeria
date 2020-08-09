from django.shortcuts import render
from .models import Pizza

# Create your views here.

def index(request):
	return render(request, 'pizza/index.html')
	
def pizzas(request):
	"""Show all pizzas."""
	pizzas = Pizza.objects.all()
	context = {'pizzas' : pizzas}
	return render(request, 'pizza/pizzas.html', context)
	
def pizza(request, pizza_id):
	"""Show a single topic and all its entries."""
	pizza = Pizza.objects.get(id=pizza_id)
	toppings = pizza.topping_set.all()
	context = {'pizza': pizza, 'toppings': toppings}
	return render(request, 'pizza/pizza.html', context)
