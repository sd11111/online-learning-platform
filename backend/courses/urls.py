from django.urls import path
from .views import (
    CommentListCreateView, CommentDetailView,
    RatingListCreateView, RatingDetailView,
    CourseListCreateView, CourseDetailView, 
    LessonListCreateView, LessonDetailView
)
urlpatterns = [
    path('', CourseListCreateView.as_view(), name='course-list'),
    path('<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('lessons/', LessonListCreateView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonDetailView.as_view(), name='lesson-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
    path('ratings/', RatingListCreateView.as_view(), name='rating-list'),
    path('ratings/<int:pk>/', RatingDetailView.as_view(), name='rating-detail'),
]
