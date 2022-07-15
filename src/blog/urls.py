from django.urls import path
from . import api

urlpatterns = [
    path('', api.get_blogs),
    path('<int:id>/', api.get_single_blog),
    path('create/', api.add_blog),
    path('delete/<int:id>/', api.delete_blog),
    path('update/<int:id>/', api.update_blog),
]