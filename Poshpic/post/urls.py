from django.urls import path
from . import views


urlpatterns = [
    path("post/", views.Post_PhototgrapherView.as_view()),
    path("post/<int:pk>/", views.Post_PhototgrapherView.as_view()),
    path("post/<int:pk>/like/", views.LikeApiView.as_view()),
    path("post/<int:pk>/comment/", views.CommentApiView.as_view()),
    path(
        "comment/<int:pk>/delete/",
        views.CommentApiView.as_view(),
    ),
    path("post/<int:pk>/repost/", views.RepostApiView.as_view()),
    path("posthistory/", views.PostHistoryListView.as_view()),
    path("posthistory/<int:pk>/", views.PostHistoryListView.as_view()),
]
