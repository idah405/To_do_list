from . import views
from.views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
from django.urls import path
#from To_do_list.tasks.views import CustomLoginView



urlpatterns = [
    
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', views.index, name = "list"),
    path('register/', RegisterPage.as_view(), name='register'),
    path('update_task/<str:pk>/', views.updateTask, name = "update_task"),
    path('delete/<str:pk>/', views.deleteTask, name = "delete"),

]
