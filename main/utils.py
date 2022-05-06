from .models import Worker


def get_phone(phone):
    message = None
    if not phone:
        message = 'phone is required!'
    elif phone not in list(Worker.objects.all().values_list('phone', flat=True)):
        message = 'phone is invalid!'
    if message:
        return message
    else:
        return None

