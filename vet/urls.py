from django.urls import path
from .views import PetOwnersList, PetsList

app_name = 'vet'

urlpatterns = [
    path('owners/', PetOwnersList.as_view(), name= "owners_list"),
    path('pets/', PetsList.as_view(), name='pets_list')
]
