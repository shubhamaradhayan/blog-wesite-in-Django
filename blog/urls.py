
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about', views.about),
    # path('/blogDescription/<str:id>', views.desc),
    path('contactUs', views.contact),
    path('posts/<int:id>', views.desc),
    path('posts/', views.post),
    path('search', views.search),
    # path('list', views.listing),
    # path('search/<str:item>', views.search),
    
]
