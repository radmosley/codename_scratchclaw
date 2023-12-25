from rest_framework.routers import DefaultRouter
from django.urls import path, include
from pets_api.urls import router
from .views import RegisterView, AccountListView
from rest_framework_simplejwt import views as jwt_views

# router.register('accounts', AccountListView, basename='accounts')
# router.register('register', RegisterView.as_view(), basename='auth_register')

# urlpatterns = [
#     path('register/', RegisterView.as_view(), name='auth_register'),
#     path('accounts/', AccountListView.as_view({'get': 'list'}), name='auth_register'),
# ]
urlpatterns = [
     path('token/', 
          jwt_views.TokenObtainPairView.as_view(), 
          name ='token_obtain_pair'),
     path('token/refresh/', 
          jwt_views.TokenRefreshView.as_view(), 
          name ='token_refresh')
]