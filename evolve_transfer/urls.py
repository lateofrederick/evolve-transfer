from django.urls import path

from evolve_transfer.views import homepage_view

urlpatterns = [
    path('', homepage_view.homepage, name='homepage'),
]