
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    # Course URLs
    path('api/courses/', views.CourseListCreateView.as_view(), name='course-list-create'),
    path('api/courses/<uuid:pk>/', views.CourseDetailView.as_view(), name='course-detail'),
    
    # Teacher URLs
    path('api/teachers/', views.TeacherListCreateView.as_view(), name='teacher-list-create'),
    path('api/teachers/<int:pk>/', views.TeacherDetailView.as_view(), name='teacher-detail'),
    
    # Student URLs
    path('api/students/', views.StudentListCreateView.as_view(), name='student-list-create'),
    path('api/students/<int:pk>/', views.StudentDetailView.as_view(), name='student-detail'),
    
    # Workload URLs
    path('api/workloads/', views.WorkloadListCreateView.as_view(), name='workload-list-create'),
    path('api/workloads/<int:pk>/', views.WorkloadDetailView.as_view(), name='workload-detail'),
    
    # Inscription URLs
    path('api/inscriptions/', views.InscriptionListCreateView.as_view(), name='inscription-list-create'),
    path('api/inscriptions/<int:pk>/', views.InscriptionDetailView.as_view(), name='inscription-detail'),
    
    # Custom endpoints
    path('api/courses/statistics/', views.course_statistics, name='course-statistics'),
    path('api/workloads/<int:workload_id>/students/', views.StudentsByWorkloadView.as_view(), name='workload-students'),
]

# Permite formato de sufijo en URLs (ej: .json, .api)
urlpatterns = format_suffix_patterns(urlpatterns)