from django.urls import path
from .views import (
    PetOwnersListCreateAPIView,
    PetOwnersRetrieveUpdateDestroyAPIView,
    PetListCreateAPIView,
    PetRetrieveUpdateDestroyAPIView
)

app_name = 'vet'

urlpatterns = [
    path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
    path("owners/<int:pk>", PetOwnersRetrieveUpdateDestroyAPIView.as_view(), name="owners_list-retrieve-update-destroy"),
    path("pets/", PetListCreateAPIView.as_view(), name="pets_list-create"),
    path("pets/<int:pk>", PetRetrieveUpdateDestroyAPIView.as_view(), name="pets_list-retrieve-update-destroy"),
]
