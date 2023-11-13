from django.contrib.auth.mixins import UserPassesTestMixin
from django.http import HttpResponseForbidden

class StaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseForbidden("You do not have permission to access this page.")

class NonStaffRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_staff

    def handle_no_permission(self):
        return HttpResponseForbidden("Access denied for staff members.")