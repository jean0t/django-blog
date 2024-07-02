from django.urls import path

from .views import front_page, post_detail

app_name = "blog"
urlpatterns = [
	path("", front_page, name="front_page"),
   	path("<slug:slug>/", post_detail, name="post_detail"),
]
