
from rest_framework import serializers
from .models.Course import Course
from .models.Teacher import Teacher
from .models.Student import Student
from .models.Workload import Workload
from .models.Inscription import Inscription


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified')


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified')


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified')


class WorkloadSerializer(serializers.ModelSerializer):
    course_name = serializers.CharField(source='course.name', read_only=True)
    teacher_name = serializers.SerializerMethodField()
    
    class Meta:
        model = Workload
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified')
    
    def get_teacher_name(self, obj):
        return f"{obj.teacher.names} {obj.teacher.father_surname} {obj.teacher.mother_surname}"


class InscriptionSerializer(serializers.ModelSerializer):
    student_name = serializers.SerializerMethodField()
    workload_info = serializers.SerializerMethodField()
    
    class Meta:
        model = Inscription
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified')
    
    def get_student_name(self, obj):
        return f"{obj.student.names} {obj.student.father_surname} {obj.student.mother_surname}"
    
    def get_workload_info(self, obj):
        return f"{obj.workload.course.name} - Grupo {obj.workload.group}"


# Serializers anidados para respuestas más completas
class CourseDetailSerializer(serializers.ModelSerializer):
    prerequisites = CourseSerializer(many=True, read_only=True)
    workloads = WorkloadSerializer(source='workload_set', many=True, read_only=True)
    
    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified')


class StudentDetailSerializer(serializers.ModelSerializer):
    inscriptions = InscriptionSerializer(source='inscription_set', many=True, read_only=True)
    
    class Meta:
        model = Student
        fields = '__all__'
        read_only_fields = ('id', 'created', 'modified')