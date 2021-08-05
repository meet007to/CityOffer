from django.urls import path
from django.conf.urls.static import static
from django.conf.urls.static import settings
from .views import *

urlpatterns = [
    path("", Product, name="product"),
    path("order/", Order1, name="order"),
    path("sprofile/", Profile, name="sprofile"),
    path("editsprofile/", EditsProfile, name="editsprofile"),
    path('ab/', PersonListView.as_view(), name='person_changelist'),
    path('add/', PersonCreateView.as_view(), name='person_add'),
    path('<int:pk>/', PersonUpdateView.as_view(), name='person_change'),
    path('ajax/load-cities/', load_cities, name='ajax_load_cities'),
    path("slogout/", Slogout, name="slogout")

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
