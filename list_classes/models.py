from django.db import models
from django.contrib import admin

class Course(models.Model):
    # Instructor
    instructor_name = models.CharField(max_length=50, blank=True)
    instructor_email = models.CharField(max_length=50, blank=True)
    course_number = models.IntegerField(primary_key=True)   # Unique course number
    semester_code = models.IntegerField(null=True, blank=True)   # Code for semester (always starts with 1)
    subject = models.CharField(max_length=4, blank=True)    # Mnemonic of class (ex: "CS" 1010)
    catalog_number = models.IntegerField(null=True, blank=True)  # Number of class (ex: CS "1010")
    description = models.CharField(max_length=500)  # Name of class
    units = models.CharField(max_length=5, blank=True)  # Number of units (string)
    component = models.CharField(max_length=5, blank=True)  # LEC,DIS,etc.
    class_capacity = models.IntegerField(null=True, blank=True)
    wait_list = models.IntegerField(null=True, blank=True)
    wait_cap = models.IntegerField(null=True, blank=True)
    enrollment_total = models.IntegerField(null=True, blank=True)
    enrollment_available = models.IntegerField(null=True, blank=True)
    topic = models.CharField(max_length=50, blank=True)  # Not sure - usually empty string

    def __str__(self):
        return self.description