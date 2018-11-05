from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout/', views.logout, name="logout"),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('findBooks/',views.findBooks,name="findBooks"),
    path('upload/',views.upload,name='upload'),
    path('user/<int:user_id>/',views.details,name='details'),
    path('result/',views.result,name='result'),
    path('delete/<int:book_id>',views.delete,name='delete'),
]