from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name="index"),
	url(r'^card/add/$', views.create_card, name="cards-create"),
	url(r'^card/(?P<card_id>\d+)/$', views.show, name="cards-show"),
	url(r'^card/(?P<card_id>\d+)/note/$', views.create_note, name="notes-create"),
]