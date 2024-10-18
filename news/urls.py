from django.urls import path
from .views import index, news_details


urlpatterns = [
    path("", index, name="home-page"),
    path("news/<int:id>", news_details, name="news-details-page"),
]