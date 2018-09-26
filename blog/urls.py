from django.urls import path
from .views import *


urlpatterns = [
    path('create/', post_create_view, name='create'),
    path('list/', post_list_view, name='list'),
    path('detail/<int:id>/', post_detail_view, name='detail'),
    path('update/<int:id>/', post_update_view, name='update'),
]
