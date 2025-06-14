from rest_framework import serializers
from .models import Student, Subject, Marks, Result

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = '__all__'


class MarksSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    subject = serializers.StringRelatedField()

    class Meta:
        model = Marks
        fields = '__all__'


class ResultSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()

    class Meta:
        model = Result
        fields = '__all__'
