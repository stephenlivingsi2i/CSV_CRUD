from django.urls import path
from employee import views



urlpatterns = [
    path('addEmployee/',
         views.add_employee,
         name='add_employee'),
    path('getEmployees/',
          views.get_employees,
          name='get_employees'),
     path('getEmployeeById/<int:employee_id>/',
          views.get_employee_by_id,
          name='get_employee_by_id'),
     path('updateEmployee/<int:employee_id>/<str:column_name>/',
          views.update_employee,
          name='update_employee'),

]