from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=200)
    head = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Discipline(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Program(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=20)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=200)
    coordinator_contact = models.CharField(max_length=200)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="programs"
    )
    disciplines = models.ManyToManyField(Discipline, related_name="programs")

    def __str__(self):
        return f"{self.code} {self.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="teachers"
    )

    def __str__(self):
        return f"{self.name} ({self.position})"


class FacultyInfo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    dean = models.CharField(max_length=200)
    deputy_dean = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name
