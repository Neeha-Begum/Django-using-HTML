from django.urls import path
from buses import views
urlpatterns=[
    path('info',views.func1)
]