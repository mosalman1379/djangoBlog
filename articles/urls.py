
from django.urls import path
from . import views
from Django.views import about


urlpatterns = [
    path('',views.article_list),

]
