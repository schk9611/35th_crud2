from django.urls import path

from . import views
from owners.views import OwnersView, DogsView

urlpatterns = [
    path('/owners', OwnersView.as_view()),
    path('/dogs', DogsView.as_view()),
]