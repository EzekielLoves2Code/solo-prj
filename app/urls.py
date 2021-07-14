from django.urls import path
from . import views 
urlpatterns = [
    path('', views.index),
    # path('<int:view_id>', views.view),
    path('<int:view_id>/remove',views.remove),
    # path('<int:view_id>/editpage',views.editpage),
]
