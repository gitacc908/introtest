from django.urls import path
from . import views


urlpatterns = [
    path('worker-stores/', views.WorkerStoreListView.as_view(), name='worker-stores'),
    path('worker-visit/', views.WorkerVisitView.as_view(), name='worker-visit')
]
