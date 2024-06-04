from django.db import models

class Student(models.Model):
    fullname = models.CharField(max_length=100)

    def __str__(self):
        return self.fullname 
    

class Subject(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Rating(models.Model):
    rating = models.IntegerField()
    name = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    #date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Прізвище ім'я: {self.student}, Предмет: {self.name}, Оцінка: {self.rating}"