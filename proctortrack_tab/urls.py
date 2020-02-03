from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from .views import proctortrack_view

urlpatterns = [
	# Url: that will used to render seperate page for our Proctor tab
	url(r"^$", login_required(proctortrack_view), name="proctortrack_view"),
]