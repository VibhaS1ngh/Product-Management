from productApp.views import UserRegistrationView, UserLoginView, ProductView
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', ProductView)

urlpatterns = [
    path('register/', UserRegistrationView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('products/',include(router.urls))


]