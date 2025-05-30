# MyWebApps/MyFirstApplication/views.py
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404

from .models.Course import Course
from .models.Teacher import Teacher
from .models.Student import Student
from .models.Workload import Workload
from .models.Inscription import Inscription

from .serializers import (
    CourseSerializer, CourseDetailSerializer,
    TeacherSerializer, StudentSerializer, StudentDetailSerializer,
    WorkloadSerializer, InscriptionSerializer
)


# =============================================================================
# COURSE VIEWS
# =============================================================================

class CourseListCreateView(generics.ListCreateAPIView):
    """
    GET: Lista todos los cursos
    POST: Crea un nuevo curso
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Obtiene un curso específico con detalles
    PUT: Actualiza un curso completamente
    PATCH: Actualiza un curso parcialmente
    DELETE: Elimina un curso
    """
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer


# =============================================================================
# TEACHER VIEWS
# =============================================================================

class TeacherListCreateView(generics.ListCreateAPIView):
    """
    GET: Lista todos los profesores
    POST: Crea un nuevo profesor
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Obtiene un profesor específico
    PUT: Actualiza un profesor completamente
    PATCH: Actualiza un profesor parcialmente
    DELETE: Elimina un profesor
    """
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


# =============================================================================
# STUDENT VIEWS
# =============================================================================

class StudentListCreateView(generics.ListCreateAPIView):
    """
    GET: Lista todos los estudiantes
    POST: Crea un nuevo estudiante
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Obtiene un estudiante específico con inscripciones
    PUT: Actualiza un estudiante completamente
    PATCH: Actualiza un estudiante parcialmente
    DELETE: Elimina un estudiante
    """
    queryset = Student.objects.all()
    serializer_class = StudentDetailSerializer


# =============================================================================
# WORKLOAD VIEWS
# =============================================================================

class WorkloadListCreateView(generics.ListCreateAPIView):
    """
    GET: Lista todas las cargas de trabajo
    POST: Crea una nueva carga de trabajo
    """
    queryset = Workload.objects.all()
    serializer_class = WorkloadSerializer


class WorkloadDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Obtiene una carga de trabajo específica
    PUT: Actualiza una carga de trabajo completamente
    PATCH: Actualiza una carga de trabajo parcialmente
    DELETE: Elimina una carga de trabajo
    """
    queryset = Workload.objects.all()
    serializer_class = WorkloadSerializer


# =============================================================================
# INSCRIPTION VIEWS
# =============================================================================

class InscriptionListCreateView(generics.ListCreateAPIView):
    """
    GET: Lista todas las inscripciones
    POST: Crea una nueva inscripción
    """
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer


class InscriptionDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    GET: Obtiene una inscripción específica
    PUT: Actualiza una inscripción completamente
    PATCH: Actualiza una inscripción parcialmente
    DELETE: Elimina una inscripción
    """
    queryset = Inscription.objects.all()
    serializer_class = InscriptionSerializer


# =============================================================================
# CUSTOM API VIEWS (Ejemplos adicionales)
# =============================================================================

@api_view(['GET'])
def course_statistics(request):
    """
    Vista personalizada para estadísticas de cursos
    """
    total_courses = Course.objects.count()
    active_courses = Course.objects.filter(status=True).count()
    
    return Response({
        'total_courses': total_courses,
        'active_courses': active_courses,
        'inactive_courses': total_courses - active_courses
    })


class StudentsByWorkloadView(APIView):
    """
    Vista personalizada para obtener estudiantes por carga de trabajo
    """
    def get(self, request, workload_id):
        try:
            workload = Workload.objects.get(id=workload_id)
            inscriptions = Inscription.objects.filter(workload=workload)
            students = [inscription.student for inscription in inscriptions]
            serializer = StudentSerializer(students, many=True)
            return Response({
                'workload': WorkloadSerializer(workload).data,
                'students': serializer.data,
                'total_students': len(students)
            })
        except Workload.DoesNotExist:
            return Response(
                {'error': 'Workload not found'}, 
                status=status.HTTP_404_NOT_FOUND
            )