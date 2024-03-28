from django.urls import path
from .views import UnitsLinkedToWorker, MakeVisit

urlpatterns = [
    path('units/', UnitsLinkedToWorker.as_view(), name='units_linked_to_worker'),
    path('visit/', MakeVisit.as_view(), name='make_visit'),
]
