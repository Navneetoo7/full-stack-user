
from .views import user_list, user_details
from django.urls import path
urlpatterns = [
    path('start/', user_list),
    path('list/<int:pk>', user_details),

]

