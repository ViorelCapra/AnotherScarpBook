from django.urls import path
from .views import HomeView, EntryView,CreateEntryView,SearchResultsView


urlpatterns = [
    path('',HomeView.as_view(template_name='entries/index.html'),name ='blog-home'),
    path('entry/<int:pk>/', EntryView.as_view(), name='entry-detail'),
    path('create_entry',CreateEntryView.as_view(success_url='/'),name='create_entry'),
    path('search/', SearchResultsView.as_view(), name='search_results')
]
