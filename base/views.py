from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Patient
from rest_framework.permissions import IsAuthenticated,AllowAny
from .serializers import *
from .permissions import *

class PatientListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor | IsNurse | IsManager | IsReceiptionist]

    def get(self, request):
        search_query = request.GET.get('search', '')
        if search_query:
            patients = Patient.objects.filter(name__icontains=search_query)  # Assuming 'name' is a field
        else:
            patients = Patient.objects.all()
        
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from django.db.models import Q


#####Now FOR DOCTOR AND Staff ##########

class DoctorListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsManager | IsDoctor | IsNurse|IsStaff]
    def get(self, request):

        #####
        search_query = request.GET.get('search', '')
        if search_query:
            doctors = Doctor.objects.filter(
                Q(name__icontains=search_query)  # Assuming 'name' is a field
                # Q(specialty__icontains=search_query)  # Assuming 'specialty' is another field
            )
        else:
        
            doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)
    


    
    def post(self,request):
        serializer = DoctorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StaffListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsStaff|IsManager]

    def get(self, request):
        staff = Staff.objects.all()
        serializer = StaffSerializer(staff,many=True)
        return Response(serializer.data)
    
    def post (self, request):
        serializer = StaffSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status =status.HTTP_400_BAD_REQUEST) 
    
class MedicalRecordListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsDoctor | IsManager | IsNurse|IsStaff]  # Example for restricted access

    def get(self, request):
        records = MedicalRecord.objects.all()
        serializer = MedicalRecordSerializer(records, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MedicalRecordSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def put(self, request, pk):

    #     try:
    #         record = MedicalRecord.objects.get(pk=pk)
    #     except MedicalRecord.DoesNotExist:
    #         return Response({'error': 'Medical record not found.'}, status=status.HTTP_404_NOT_FOUND)
        
    #     serializer = MedicalRecordSerializer(record, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InvoiceListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsManager | IsStaff]  # Only managers AND Staff can access this view

    def get(self, request):
        invoices = Invoice.objects.all()
        serializer = InvoiceSerializer(invoices, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = InvoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InventoryItemListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsManager | IsStaff]
    def get(self, request):
        items = InventoryItem.objects.all()
        serializer = InventoryItemSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = InventoryItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmergencyListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsManager | IsStaff|IsDoctor|IsReceiptionist]
    def get(self, request):
        emergencies = Emergency.objects.all()
        serializer = EmergencySerializer(emergencies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = EmergencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmergencyDetailAPIView(APIView):
    permission_classes = [IsAuthenticated, IsManager | IsStaff|IsDoctor|IsReceiptionist]
    def get(self, request, pk):
        try:
            emergency = Emergency.objects.get(pk=pk)
        except Emergency.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmergencySerializer(emergency)
        return Response(serializer.data)
    
    def patch(self, request, pk):
        try:
            emergency = Emergency.objects.get(pk=pk)
        except Emergency.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EmergencySerializer(emergency, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AppointmentListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsManager | IsNurse|IsDoctor]
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

# View to handle inventory usage
class InventoryUsageListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated, IsManager | IsStaff]
    def get(self, request):
        usage_records = InventoryUsage.objects.all()
        serializer = InventoryUsageSerializer(usage_records, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = InventoryUsageSerializer(data=request.data)
        if serializer.is_valid():
            # Reduce inventory quantity based on usage
            inventory_item = serializer.validated_data['inventory_item']
            used_quantity = serializer.validated_data['used_quantity']

            if inventory_item.quantity >= used_quantity:
                inventory_item.quantity -= used_quantity
                inventory_item.save()

                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Not enough inventory available'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class RegisterAPIView(APIView):
    permission_classes = []
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        print(serializer.errors)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.models import User, Group


class CustomTokenObtainPairView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        
        user = authenticate(username=username, password=password)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        

class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                # Generate JWT tokens
                refresh = RefreshToken.for_user(user)
                access_token = str(refresh.access_token)
                return Response({
                    'message': 'Login successful',
                    'access': access_token,
                    'refresh': str(refresh),
                }, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


from django.contrib.auth.models import Group

######Group
class GroupListView(APIView):
    permission_classes = [AllowAny]  # Add your custom permission class here if needed

    def get(self, request):
        groups = Group.objects.all()
        serializer = GroupSerializer(groups, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


#########Custom permission
from .permissions import IsDoctor, IsManager, IsNurse, IsStaff

######Now for the analytical section  ###############
####################################
###################################
from django.db.models import Count, Sum

###########################REPORT SECTION ###################
# Report on Patient Demographics
class PatientDemographicsReportAPIView(APIView):
    def get(self, request):
        demographics = Patient.objects.values('name').annotate(count=Count('id'))
        return Response(demographics)

# Report on Appointment Summary
class AppointmentSummaryReportAPIView(APIView):
    def get(self, request):
        appointments_summary = Appointment.objects.values('doctor__name', 'status').annotate(count=Count('id'))
        return Response(appointments_summary)

# Report on Revenue and Expenses
class FinancialReportAPIView(APIView):
    def get(self, request):
        revenue = Invoice.objects.filter(status='Paid').aggregate(total_revenue=Sum('amount'))
        expenses = InventoryItem.objects.aggregate(total_expenses=Sum('cost'))
        return Response({
            'revenue': revenue['total_revenue'],
            'expenses': expenses['total_expenses']
        })

######################## END |||||||||| #############################

#########TO GET RECEIPTIONIST DETAILS  CREATE NEW AND UPDATE//EDIT 
class ReceptionistListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated|IsReceiptionist]  # Add your custom permission class here if needed

    def get(self, request):
        receptionists = Receptionist.objects.all()
        serializer = ReceptionistSerializer(receptionists, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReceptionistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReceptionistDetailAPIView(APIView):
    permission_classes = [IsAuthenticated| IsDoctor|IsManager |IsReceiptionist]  # Add your custom permission class here if needed

    def get_object(self, pk):
        try:
            return Receptionist.objects.get(pk=pk)
        except Receptionist.DoesNotExist:
            return None

    def get(self, request, pk):
        receptionist = self.get_object(pk)
        if receptionist is not None:
            serializer = ReceptionistSerializer(receptionist)
            return Response(serializer.data)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        receptionist = self.get_object(pk)
        if receptionist is not None:
            serializer = ReceptionistSerializer(receptionist, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        receptionist = self.get_object(pk)
        if receptionist is not None:
            receptionist.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
    







##############LOGOUT ###############
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken
from rest_framework_simplejwt.tokens import AccessToken, RefreshToken
class LogoutAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        # Obtain the refresh token from the request
        refresh_token = request.data.get('refresh')

        if refresh_token is None:
            return Response({"detail": "Refresh token not provided."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Blacklist the refresh token
            outstanding_token = OutstandingToken.objects.get(token=refresh_token)
            BlacklistedToken.objects.create(token=outstanding_token)
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)
        except OutstandingToken.DoesNotExist:
            return Response({"detail": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)
        


#####For Nurse
class NurseListCreateAPIView(APIView):
    permission_classes = [IsAuthenticated,IsManager|IsNurse|IsReceiptionist|IsStaff]

    def get(self, request):
        nurses = Nurse.objects.all()
        serializer = NurseSerializer(nurses, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NurseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)