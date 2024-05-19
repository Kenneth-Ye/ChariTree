from django.urls import path
from . import views

urlpatterns = [
    path('add_cause', views.add_cause),
    path('get_causes', views.get_causes),
    # name, description, image, total $ received
    # list of transactions -> $ spent at each cause (cause addr/name)
    path('get_charity_total', views.get_charity_info),
    path('get_charity_transactions', views.get_char_transactions),
    path('post_charity_transactions', views.post_char_transactions),
    path('post_transactions', views.post_transactions),
    path('get_transactions', views.get_transactions),
    path('get_all_charities', views.get_all_charities),
 ]