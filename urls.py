from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_view),
    path('now/', views.date_view),
    path('random_num/', views.random_number),
    path('image/', views.image_view),
    path('students/', views.student_view),
    path('post/', views.create_post),

]