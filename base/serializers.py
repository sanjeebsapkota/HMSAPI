from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User,Group

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = '__all__'


class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class InventoryItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryItem
        fields = '__all__'


class EmergencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Emergency
        fields = '__all__'

class InventoryUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventoryUsage
        # fields = '__all__'
        fields = ['name']

class InventoryUsageSerializer(serializers.ModelSerializer):
    inventory_item_name = serializers.ReadOnlyField(source='inventory_item.name')

    class Meta:
        model = InventoryUsage
        fields = ['id', 'inventory_item', 'inventory_item_name', 'used_quantity', 'date_used', 'purpose']


class UserSerializer(serializers.ModelSerializer):
    groups = serializers.PrimaryKeyRelatedField(many=True, queryset=Group.objects.all(), required=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'email','groups']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        groups = validated_data.pop('groups',[])
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
            email=validated_data['email']
        )
        user.groups.set(groups)
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']


class ReceptionistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receptionist
        fields = '__all__'

class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nurse
        fields = '__all__'