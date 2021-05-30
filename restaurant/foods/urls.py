from django.urls import path

from . import views


app_name = "foods"
urlpatterns = [
    path(
        route='',
        view=views.FoodListView.as_view(),
        name='list'
    ),
]
