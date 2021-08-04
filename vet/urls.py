from django.urls import path
from .views import (
    PetOwnersListCreateAPIView,
    PetOwnersRetrieveUpdateDestroyAPIView,
    PetListCreateAPIView,
    PetRetrieveUpdateDestroyAPIView,
    PetDateListAPIView,
    PetDateCreateAPIView,
    PetDateRetrieveUpdateDestroyAPIView,
    PetDateRetrievePet
)

app_name = 'vet'

urlpatterns = [
    path("owners/", PetOwnersListCreateAPIView.as_view(), name="owners_list-create"),
    path("owners/<int:pk>", PetOwnersRetrieveUpdateDestroyAPIView.as_view(), name="owners_list-retrieve-update-destroy"),
    path("pets/", PetListCreateAPIView.as_view(), name="pets_list-create"),
    path("pets/<int:pk>", PetRetrieveUpdateDestroyAPIView.as_view(), name="pets_list-retrieve-update-destroy"),
    path("petdate/", PetDateListAPIView.as_view(), name="petdate_list"),
    path("petdate/create/", PetDateCreateAPIView.as_view(), name="petdate_create"),
    path("petdate/<int:pk>", PetDateRetrieveUpdateDestroyAPIView.as_view(), name = "pets_retrieve_update_destroy"),
    path("petdate/pet/", PetDateRetrievePet.as_view(), name = "petdate_filter-pet")
]
