from django.urls import path

from evolve_transfer.views import homepage_view, login_view, register_view

urlpatterns = [
    path('', homepage_view.homepage, name='homepage'),
    path('login/', login_view.login_request, name='login_request'),
    path('signup/', register_view.register_request, name='register_request')
]