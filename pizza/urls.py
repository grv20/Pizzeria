from django.urls import path
from . import views

app_name = "pizza"

urlpatterns = [ 
path('', views.index, name ='index'),
path('pizzas/', views.pizzas, name = 'pizzas'),
path('pizzas/(?P<pizza_id>\d+)/', views.pizza, name='pizza'),
]
