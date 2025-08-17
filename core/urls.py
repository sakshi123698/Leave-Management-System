from django.urls import path
from . import views

urlpatterns = [

    path('add-employee/', views.add_employee),
    path('apply-leave/', views.apply_leave),
    path('update-leave-status/', views.update_leave_status),
    path('leave-balance/', views.leave_balance),
    path('employees/', views.list_employees),

]
