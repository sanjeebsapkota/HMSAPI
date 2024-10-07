from django.urls import path


from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    # Patient Management
    PatientListCreateAPIView,

    # Doctor and Staff Management
    DoctorListCreateAPIView,
    StaffListCreateAPIView,

    # Appointment Management
    AppointmentListCreateAPIView,

    # Medical Records Management
    MedicalRecordListCreateAPIView,

    # Billing and Payment
    InvoiceListCreateAPIView,

    # Inventory Management
    InventoryItemListCreateAPIView,

    # Emergency Management
    EmergencyListCreateAPIView,
    EmergencyDetailAPIView,

    # Inventory Usage
    InventoryUsageListCreateAPIView,

    # User Registration
    RegisterAPIView,
    
    CustomTokenObtainPairView,
    PatientDemographicsReportAPIView, 
    AppointmentSummaryReportAPIView, 
    FinancialReportAPIView,


    #####Receiptionist 
    ReceptionistListCreateAPIView, 
    ReceptionistDetailAPIView
)

from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    # Patient Management
    PatientListCreateAPIView,

    # Doctor and Staff Management
    DoctorListCreateAPIView,
    StaffListCreateAPIView,

    # Appointment Management
    AppointmentListCreateAPIView,

    # Medical Records Management
    MedicalRecordListCreateAPIView,

    # Billing and Payment
    InvoiceListCreateAPIView,

    # Inventory Management
    InventoryItemListCreateAPIView,

    # Emergency Management
    EmergencyListCreateAPIView,
    EmergencyDetailAPIView,

    # Inventory Usage
    InventoryUsageListCreateAPIView,

    # User Registration
    RegisterAPIView,
    
    # Custom JWT Login View
    CustomTokenObtainPairView,
    

    ##Login 
    LoginView,

    ##Group User
    GroupListView,

    #Report Format
    PatientDemographicsReportAPIView, 
    AppointmentSummaryReportAPIView, 
    FinancialReportAPIView,

    #Logout
    LogoutAPIView,

    #For nurse
    NurseListCreateAPIView
)

urlpatterns = [
    # Patient Management
    path('patients/', PatientListCreateAPIView.as_view(), name='patient-list-create'),

    # Doctor Management
    path('doctors/', DoctorListCreateAPIView.as_view(), name='doctor-list-create'),

    #Staff Management
    path('staff/', StaffListCreateAPIView.as_view(), name='staff-list-create'),

    # Appointment Management
    path('appointments/', AppointmentListCreateAPIView.as_view(), name='appointment-list-create'),

    # Medical Records Management
    path('medical-records/', MedicalRecordListCreateAPIView.as_view(), name='medical-record-list-create'),
    # path('medical-records/<int:pk>/', MedicalRecordListCreateAPIView.as_view(), name='medical-record-update'),

    # Billing and Payment
    path('invoices/', InvoiceListCreateAPIView.as_view(), name='invoice-list-create'),

    # Inventory Management
    path('inventory/', InventoryItemListCreateAPIView.as_view(), name='inventory-item-list-create'),

    # Emergency Management
    path('emergencies/', EmergencyListCreateAPIView.as_view(), name='emergency-list-create'),
    path('emergencies/<int:pk>/', EmergencyDetailAPIView.as_view(), name='emergency-detail'),

    # Inventory Usage
    path('inventory-usage/', InventoryUsageListCreateAPIView.as_view(), name='inventory-usage-list-create'),

    # User Registration
    path('register/', RegisterAPIView.as_view(), name='register'),

    # Authentication endpoints
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Using Custom JWT view for login
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    #Login 
    path('login/', LoginView.as_view(), name='login'),

    ## Group_User Details
    path('groups/', GroupListView.as_view(), name='group-list'),


    ####Report part
    path('reports/patient-demographics/', PatientDemographicsReportAPIView.as_view(), name='patient-demographics'),
    path('reports/appointment-summary/', AppointmentSummaryReportAPIView.as_view(), name='appointment-summary'),
    path('reports/financial/', FinancialReportAPIView.as_view(), name='financial-report'),

    #####lOGOUT
    path('logout/', LogoutAPIView.as_view(), name='logout'),

    ##Nurse
    path('nurses/', NurseListCreateAPIView.as_view(), name='nurse-list-create'),


    ######Receiptionsit details
    path('receptionists/', ReceptionistListCreateAPIView.as_view(), name='receptionist-list-create'),
    path('receptionists/<int:pk>/', ReceptionistDetailAPIView.as_view(), name='receptionist-detail'),
]
