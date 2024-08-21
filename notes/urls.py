from django.urls import path
from notes import views
urlpatterns=[
    path('des',views.func,name="note"),
    path('hi',views.func2,name="update")
]