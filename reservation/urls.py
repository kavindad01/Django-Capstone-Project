from django.urls import path
from .views import index,bookingview


urlpatterns=[

    path('',views.index,name='index'),
   # path('menu/',views.Menu.as_),
    path('booking/',bookingview.as_view())

]