from django.urls import path
from .views import (
    # Listas Genericas
    PetOwnersListAPIView,
    PetsListAPIView,
    # PetOwnersListCreate, 
    # PetsListCreate, 
    # PetOwnerRetrieveUpdateDestroyAPIView, 
    # PetsRetrieveUpdateDestroyAPIView
)

app_name = 'vet'

urlpatterns = [
    path("owners/", PetOwnersListAPIView.as_view(), name="owners_list-create"),
    path("pets/", PetsListAPIView.as_view(), name="pets_list-create"),
    # path("owners/", PetOwnersListCreate.as_view(), name="owners_list-create"),
    # path("owners/<int:pk>", PetOwnerRetrieveUpdateDestroyAPIView.as_view(), name="owners_retrieve-update-destroy"),
    # path("pets/", PetsListCreate.as_view(), name="pets_list-create"),
    # path("pets/<int:pk>", PetsRetrieveUpdateDestroyAPIView.as_view(), name="pets_list"),
]
