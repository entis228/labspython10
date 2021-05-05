from django.urls import path
from .views import *

urlpatterns=[
    path('',index),
    path('findand',findand),
    path('favicon.ico/',my_image),
    path('find/',find),
    path('download/',download),
]