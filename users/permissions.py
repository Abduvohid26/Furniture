# from django.contrib.auth.mixins import PermissionRequiredMixin
# from django.http.response import HttpResponseRedirect
# from django.shortcuts import redirect
# from .models import Admin
#
#
# class MyPermissionControl(PermissionRequiredMixin):
#     login_url = "/login/"
#     permission_required = ('main.add_resident', "main.add_payment")
#     permission_denied_message = "Bu bo'limga kirish uchun sizda tegishli ruxsat yo'q"
#
#     def handle_no_permission(self) -> HttpResponseRedirect:
#         user = self.request.user
#
#         if not user.is_authenticated:
#             return redirect("/login")
#         if user.position == 'cashier':
#             return redirect("finance/payments")
#         if user.position == 'admin':
#             return redirect("/")
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect


# class MyPermissionControl(PermissionRequiredMixin):
#     login_url = '/login'
#     permission_denied_message = (
#         "Bu bo'limga kirish uchun sizda tegishli ruxsat yo'q"
#                                  )
#
#     def handle_no_permission(self) -> HttpResponseRedirect:
#         user = self.request.user
#         if not user.is_authenticated:
#             return redirect('/login')
#         if user.user_roles == 'manager':
#             return redirect('/')
#
#         if user.user_roles == 'admin':
#             return redirect('/')
#
#         if user.user_roles == 'worker':
#             return redirect('core:orders')