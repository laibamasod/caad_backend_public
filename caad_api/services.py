from .models import *
import random
from rest_framework.response import Response
def generate_verification_code():
    return random.randint(1000, 9999)
def get_internship(std_cnic):
        try:
            student_registration = StudentRegistration.objects.get(std_cnic=std_cnic)
        except StudentRegistration.DoesNotExist:
           return Response({"message": "Student registration not found"}, status=404)
        try:
            internship = Internships.objects.get(registration_no=student_registration.reg_form_id)
        except internship.DoesNotExist:
           return Response({"message": "Internship not found"}, status=404)
        return internship


def get_identity(internship_id):
        try:
            identity = IdentitycardProforma.objects.get(internship_id=internship_id)
        except IdentitycardProforma.DoesNotExist:
           return Response({"message": "Identity not found"}, status=404)
        return identity