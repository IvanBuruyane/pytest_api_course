from django.urls import path
from api.coronavstech.fibonacci_app import views


urlpatterns = [
    path("", views.get_fibonacci_n, name="get_fibonacci_n"),
]
