from django.urls import path

from bug_tracker.views import IndexListView, BugCreateView, BugDetailView, BugUpdateView, BugDeleteView, aboutView, BugSearchListView, homeView

urlpatterns = [
    path('', homeView, name="home"),
    path('bugs', IndexListView.as_view(), name='bug_list'),
    path('about/', aboutView, name='about_page'),
    path('create/', BugCreateView.as_view(), name='create_bug'),
    path('<int:pk>/',  BugDetailView.as_view(), name='bug_detail'),
    path('<int:pk>/update/', BugUpdateView.as_view(), name='bug_update'),
    path('<int:pk>/delete', BugDeleteView.as_view(), name='bug_delete'),
    path('search/', BugSearchListView.as_view(), name="search_results")
]
