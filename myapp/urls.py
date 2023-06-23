from django.urls import path
from .views import about, login, contacts, cars, drivers, clients, index_myapp

urlpatterns = [
    path('', index_myapp, name='index'),
    path('about/', about, name='about'),
    path('login/', login, name='login'),
    path('cars/', cars, name='cars'),
    path('drivers/', drivers, name='drivers'),
    path('clients/', clients, name='clients'),
    path('contacts/<int:id>/', contacts, name='contacts'),

]

# path('add_from/', add_from, name='add_from')