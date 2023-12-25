from rest_framework.routers import DefaultRouter
from django.urls import path, include
from pets_api.urls import router
from .views import RegisterView, AccountListView

router.register('accounts', AccountListView, basename='accounts')
# router.register('register', RegisterView.as_view(), basename='auth_register')

urlpatterns = [
    path('register/', RegisterView.as_view(), name='auth_register'),
    # path('accounts/', AccountListView.as_view({'get': 'list'}), name='auth_register'),
]