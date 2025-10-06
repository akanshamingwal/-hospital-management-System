from django import template
from hospital import models

register = template.Library()

@register.filter
def get_doctor_name(doctor_id):
    try:
        doctor = models.Doctor.objects.get(user_id=doctor_id)
        return f"Dr. {doctor.user.first_name}"
    except models.Doctor.DoesNotExist:
        return "Unassigned"
