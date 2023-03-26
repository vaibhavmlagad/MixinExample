from django.urls import path
from .views import CourseList, CourseDetails

urlpatterns = [
    path('courses/', CourseList.as_view(), name='course-list'),
    path('courses/<int:pk>/', CourseDetails.as_view(), name='course-details'),
]
