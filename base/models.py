from django.db import models
from django.contrib.auth.models import AbstractUser

class Patient(models.Model):
    name = models.CharField(max_length=255)
    contact_info = models.CharField(max_length=255)
    medical_history = models.TextField()
    date_registered = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
    

class Doctor(models.Model):
    name = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)

class Receptionist(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=300)
    contact_number = models.CharField(max_length=15)  # Adjust max_length as needed


class Staff(models.Model):
    name = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    availability = models.BooleanField(default=True)



class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateTimeField()
    status = models.CharField(max_length=50, default='Pending')


class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    record = models.TextField()
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)

class Invoice(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_issued = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='Unpaid')


class InventoryItem(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    date_added = models.DateTimeField(auto_now_add=True)

class InventoryUsage(models.Model):
    inventory_item = models.ForeignKey(InventoryItem, on_delete=models.CASCADE)
    used_quantity = models.IntegerField()
    date_used = models.DateTimeField(auto_now_add=True)
    purpose = models.CharField(max_length=255)  # E.g., Surgery, Emergency, etc.

    def __str__(self):
        return f"{self.used_quantity} of {self.inventory_item.name} used on {self.date_used}"

class Emergency(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    severity = models.CharField(max_length=50)  # e.g., High, Medium, Low
    status = models.CharField(max_length=50, default='Pending')  # e.g., Pending, Resolved
    date_reported = models.DateTimeField(auto_now_add=True)


class Nurse(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    hire_date = models.DateField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"