from django.urls import path
from .views import (
    PetOwnersListCreateAPIView,
    PetListCreateAPIView
)

app_name = 'vet'

urlpatterns = [
    path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
    path("pets/", PetListCreateAPIView.as_view(), name="pets_list-create"),
]
