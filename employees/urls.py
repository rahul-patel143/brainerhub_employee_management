from django.urls import path
from rest_framework.routers import DefaultRouter
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import UploadExcelView, EmployeeListView, CompanyListView

schema_view = get_schema_view(
    openapi.Info(
        title="Employee API",
        default_version='v1',
        description="API for uploading and retrieving employee data.",
    ),
    public=True,
)

urlpatterns = [
    path('upload/', UploadExcelView.as_view(), name='upload-excel'),
    path('employees/', EmployeeListView.as_view(), name='list-employees'),
    path('employees/<int:employee_id>/', EmployeeListView.as_view(), name='employee-detail'),
    path('companies/', CompanyListView.as_view(), name='list-companies'),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
