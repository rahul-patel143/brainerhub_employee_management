import pandas as pd
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .serializers import EmployeeSerializer, CompanySerializer, EmployeeCompanySerializer
from .models import Employee, Company

class UploadExcelView(APIView):
    """
    API to upload an Excel or CSV file and insert data into the database.
    """
    
    @swagger_auto_schema(
        operation_description="Upload an Excel (.xlsx) or CSV (.csv) file to insert employee data.",
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'file': openapi.Schema(type=openapi.TYPE_FILE, description="Upload an Excel or CSV file"),
            },
            required=['file'],
        ),
        responses={201: "Data uploaded successfully", 400: "Invalid file format or validation error"},
    )
    def post(self, request, *args, **kwargs):
        file = request.FILES.get('file')
        if not file:
            return Response({"error": "No file uploaded"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            if file.name.endswith('.csv'):
                df = pd.read_csv(file)
            elif file.name.endswith('.xlsx'):
                df = pd.read_excel(file)
            else:
                return Response({"error": "Invalid file format. Only CSV and Excel are supported."}, 
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"error": f"Error reading file: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

        # Rename columns for matching with Django model fields
        df.rename(columns={
            'EMPLOYEE_ID': 'employee_id',
            'FIRST_NAME': 'first_name',
            'LAST_NAME': 'last_name',
            'PHONE_NUMBER': 'phone_number',
            'COMPANY_NAME': 'company_name',
            'SALARY': 'salary',
            'MANAGER_ID': 'manager_id',
            'DEPARTMENT_ID': 'department_id'
        }, inplace=True)

        employees = df.to_dict(orient='records')
        serializer = EmployeeSerializer(data=employees, many=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Data uploaded successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmployeeListView(APIView):
    """
    API to retrieve all employees or a specific employee by employee_id.
    """

    @swagger_auto_schema(
        operation_description="Retrieve all employees or a specific employee by ID.",
        responses={200: EmployeeCompanySerializer(many=True)},
    )
    def get(self, request, employee_id=None):
        if employee_id:  # If ID is provided, get specific employee
            try:
                employee = Employee.objects.select_related('company').get(employee_id=employee_id)
                serializer = EmployeeCompanySerializer(employee)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Employee.DoesNotExist:
                return Response({"error": "Employee not found"}, status=status.HTTP_404_NOT_FOUND)
        else:  # Get all employees
            employees = Employee.objects.select_related('company').all()
            serializer = EmployeeCompanySerializer(employees, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)

class CompanyListView(APIView):
    """
    API to retrieve all companies.
    """
    
    @swagger_auto_schema(
        operation_description="Retrieve all companies from the database.",
        responses={200: CompanySerializer(many=True)},
    )
    def get(self, request):
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
