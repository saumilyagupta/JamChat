from django.urls import path ,include
from . import views
urlpatterns = [
    path("room/<str:room>/",views.room , name='room'),
    path("", views.home , name="home"),
    path("checkroom", views.checkroom , name="checkroom"),
    path("send" , views.send , name="send"),
    path('getMessages/<str:room>',views.getMessages , name = 'getMessages')

]
