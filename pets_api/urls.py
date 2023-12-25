from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PetListViewSet, SpeciesViewSet
from accounts.views import AccountListView

router = DefaultRouter()
router.register('pets', PetListViewSet, basename='pet')
router.register('species', SpeciesViewSet, basename='species')
router.register('accounts', AccountListView, basename='accounts')

urlpatterns = router.urls + [

]