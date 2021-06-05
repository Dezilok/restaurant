from django.urls import path
from django.contrib.auth.decorators import permission_required

from . import views


app_name = "foods"
urlpatterns = [
    path(
        route='',
        view=views.FoodListView.as_view(),
        name='list'
    ),
    path(
        route='add/',
        view=views.FoodCreateView.as_view(),
        name='add'),
    path(
        route='<slug:slug>/',
        view=views.FoodDetailView.as_view(),
        name='detail'
    ),
    path(
        route="<slug:slug>/update/",
        view=views.FoodUpdateView.as_view(),
        name='update'
    ),
]
