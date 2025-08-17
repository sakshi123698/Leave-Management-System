# from django.shortcuts import render

# # Create your views here.

# # from django.shortcuts import render
# def home(request):
#     return render(request, 'core/index.html')




# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Employee, LeaveRequest
# from .serializers import EmployeeSerializer, LeaveRequestSerializer
# from django.core.exceptions import ObjectDoesNotExist
# from datetime import datetime

# @api_view(['POST'])
# def add_employee(request):
#     serializer = EmployeeSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response({'message': 'Employee added', 'data': serializer.data}, status=201)
#     return Response(serializer.errors, status=400)

# @api_view(['POST'])
# def apply_leave(request):
#     email = request.data.get('email')
#     start_date_str = request.data.get('start_date')
#     end_date_str = request.data.get('end_date')
#     reason = request.data.get('reason', '')
#     try:
#         emp = Employee.objects.get(email=email)
#     except ObjectDoesNotExist:
#         return Response({'error': 'Employee not found'}, status=404)
#     try:
#         start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
#         end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
#     except Exception:
#         return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)
#     if start_date < emp.joining_date:
#         return Response({'error': 'Cannot apply for leave before joining date'}, status=400)
#     if end_date < start_date:
#         return Response({'error': 'End date cannot be before start date'}, status=400)
#     days = (end_date - start_date).days + 1
#     if days > emp.leave_balance:
#         return Response({'error': 'Applying for more days than available balance'}, status=400)
#     overlapping = LeaveRequest.objects.filter(
#         employee=emp,
#         status='Approved',
#         start_date__lte=end_date,
#         end_date__gte=start_date
#     )
#     if overlapping.exists():
#         return Response({'error': 'Overlapping leave request exists'}, status=400)
#     leave_req = LeaveRequest.objects.create(
#         employee=emp,
#         start_date=start_date,
#         end_date=end_date,
#         reason=reason,
#         status='Pending'
#     )
#     return Response({'message': 'Leave request submitted', 'leave_id': leave_req.id}, status=201)

# @api_view(['POST'])
# def update_leave_status(request):
#     leave_id = request.data.get('leave_id')
#     action = request.data.get('action')  # 'Approve' or 'Reject'
#     try:
#         leave_req = LeaveRequest.objects.get(id=leave_id)
#     except ObjectDoesNotExist:
#         return Response({'error': 'Leave request not found'}, status=404)
#     if leave_req.status != 'Pending':
#         return Response({'error': 'Request already processed'}, status=400)
#     if action == 'Approve':
#         days = (leave_req.end_date - leave_req.start_date).days + 1
#         if leave_req.employee.leave_balance < days:
#             return Response({'error': 'Not enough leave balance'}, status=400)
#         leave_req.employee.leave_balance -= days
#         leave_req.employee.save()
#         leave_req.status = 'Approved'
#     elif action == 'Reject':
#         leave_req.status = 'Rejected'
#     else:
#         return Response({'error': 'Invalid action'}, status=400)
#     leave_req.save()
#     return Response({'message': f'Leave {leave_req.status}'}, status=200)

# @api_view(['GET'])
# def leave_balance(request):
#     email = request.GET.get('email')
#     try:
#         emp = Employee.objects.get(email=email)
#         return Response({'leave_balance': emp.leave_balance}, status=200)
#     except ObjectDoesNotExist:
#         return Response({'error': 'Employee not found'}, status=404)
    










# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Employee
# from .serializers import EmployeeSerializer

# @api_view(['GET'])
# def list_employees(request):
#     employees = Employee.objects.all()
#     serializer = EmployeeSerializer(employees, many=True)
#     return Response(serializer.data)




from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, LeaveRequest
from .serializers import EmployeeSerializer, LeaveRequestSerializer
from django.core.exceptions import ObjectDoesNotExist
from datetime import datetime, date, timedelta


def home(request):
    return render(request, 'core/index.html')


@api_view(['POST'])
def add_employee(request):
    # Edge Case: Prevent duplicate employee email
    if Employee.objects.filter(email=request.data.get('email')).exists():
        return Response({'error': 'Employee with this email already exists.'}, status=400)

    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Employee added', 'data': serializer.data}, status=201)
    return Response(serializer.errors, status=400)


@api_view(['POST'])
def apply_leave(request):
    email = request.data.get('email')
    start_date_str = request.data.get('start_date')
    end_date_str = request.data.get('end_date')
    reason = request.data.get('reason', '')

    try:
        emp = Employee.objects.get(email=email)
    except ObjectDoesNotExist:
        return Response({'error': 'Employee not found'}, status=404)

    # Edge Case: Employee has not joined yet
    if emp.joining_date > date.today():
        return Response({'error': 'Employee has not joined yet.'}, status=400)

    try:
        start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
    except Exception:
        return Response({'error': 'Invalid date format. Use YYYY-MM-DD.'}, status=400)

    # Edge Case: Leave dates in the past
    today = date.today()
    if start_date < today or end_date < today:
        return Response({'error': 'Leave dates cannot be in the past.'}, status=400)

    # Edge Case: Cannot apply leave before joining date
    if start_date < emp.joining_date:
        return Response({'error': 'Cannot apply for leave before joining date'}, status=400)

    # Edge Case: End date before start date
    if end_date < start_date:
        return Response({'error': 'End date cannot be before start date'}, status=400)

    days = (end_date - start_date).days + 1

    # Edge Case: No leave balance
    if emp.leave_balance <= 0:
        return Response({'error': 'No leave balance to apply for leave.'}, status=400)

    # Edge Case: Applying for more days than available balance
    if days > emp.leave_balance:
        return Response({'error': 'Applying for more days than available balance'}, status=400)

    # Edge Case: Overlapping approved leave request
    overlapping = LeaveRequest.objects.filter(
        employee=emp,
        status='Approved',
        start_date__lte=end_date,
        end_date__gte=start_date
    )
    if overlapping.exists():
        return Response({'error': 'Overlapping approved leave request exists'}, status=400)

    # Edge Case: Overlapping pending leave request
    pending_overlap = LeaveRequest.objects.filter(
        employee=emp,
        status='Pending',
        start_date__lte=end_date,
        end_date__gte=start_date
    )
    if pending_overlap.exists():
        return Response({'error': 'You already have a pending overlapping leave request.'}, status=400)

    # Edge Case: Leave only on weekends (Saturday=5, Sunday=6)
    def is_weekend(d):
        return d.weekday() >= 5

    if all(is_weekend(start_date + timedelta(days=i)) for i in range(days)):
        return Response({'error': 'Leave cannot be applied only on weekends.'}, status=400)

    # Edge Case: Yearly leave limit 30 days
    year_start = date(start_date.year, 1, 1)
    year_end = date(start_date.year, 12, 31)
    approved_leaves_year = LeaveRequest.objects.filter(
        employee=emp,
        status='Approved',
        start_date__gte=year_start,
        end_date__lte=year_end
    )
    total_days_taken = sum(
        (lr.end_date - lr.start_date).days + 1 for lr in approved_leaves_year
    )
    if total_days_taken + days > 30:
        return Response({'error': 'Exceeded yearly leave limit of 30 days.'}, status=400)

    # All validations passed, create leave request
    leave_req = LeaveRequest.objects.create(
        employee=emp,
        start_date=start_date,
        end_date=end_date,
        reason=reason,
        status='Pending'
    )
    return Response({'message': 'Leave request submitted', 'leave_id': leave_req.id}, status=201)


@api_view(['POST'])
def update_leave_status(request):
    leave_id = request.data.get('leave_id')
    action = request.data.get('action')  # 'Approve' or 'Reject'

    try:
        leave_req = LeaveRequest.objects.get(id=leave_id)
    except ObjectDoesNotExist:
        return Response({'error': 'Leave request not found'}, status=404)

    # Edge Case: Prevent status change if already processed
    if leave_req.status != 'Pending':
        return Response({'error': 'Request already processed'}, status=400)

    if action == 'Approve':
        days = (leave_req.end_date - leave_req.start_date).days + 1
        if leave_req.employee.leave_balance < days:
            return Response({'error': 'Not enough leave balance'}, status=400)
        leave_req.employee.leave_balance -= days
        leave_req.employee.save()
        leave_req.status = 'Approved'
    elif action == 'Reject':
        leave_req.status = 'Rejected'
    else:
        return Response({'error': 'Invalid action'}, status=400)

    leave_req.save()
    return Response({'message': f'Leave {leave_req.status}'}, status=200)


@api_view(['GET'])
def leave_balance(request):
    email = request.GET.get('email')
    try:
        emp = Employee.objects.get(email=email)
        return Response({'leave_balance': emp.leave_balance}, status=200)
    except ObjectDoesNotExist:
        return Response({'error': 'Employee not found'}, status=404)


@api_view(['GET'])
def list_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)


