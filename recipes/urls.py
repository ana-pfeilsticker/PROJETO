from django.urls import path

from recipes.views import about, contacts, home

urlpatterns = [
    path('', home),  # HOME
    path('about/', about),  # ABOUT
    path('contacts/', contacts),  # CONTACTS

]
