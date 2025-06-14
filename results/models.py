from django.db import models

class Student(models.Model):
    roll_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField()

    def __str__(self):
        return f"{self.roll_number} - {self.name}"


class Subject(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.code} - {self.name}"


class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='marks')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.FloatField()

    class Meta:
        unique_together = ('student', 'subject')

    def __str__(self):
        return f"{self.student} | {self.subject} | {self.marks_obtained}"


class Result(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='result')
    total_marks = models.FloatField()
    percentage = models.FloatField()
    grade = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.student} | {self.percentage}% | Grade: {self.grade}"
