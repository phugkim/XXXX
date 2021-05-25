from django.urls import path
### VIEWS
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('simple/', views.simple.as_view()),
    path('person/', views.GetAllPerson.as_view()),
    # path('user/', views.UserViewSet.as_view()),
    # path('group/', views.GroupViewSet.as_view()),
# Hiển thị ra giao diện
    path('show-template/', views.showTemplate, name='show-template'),

]