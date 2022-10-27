from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404


User = get_user_model()


def generate_and_send_confirmation_code(username):
    user = get_object_or_404(User, username=username)
    user.confirmation_code = default_token_generator.make_token(user)
    send_mail(
        'Код подтверждения',
        f'confirmation_code {user.confirmation_code}',
        settings.ADMIN_EMAIL,
        [f'{user.email}'],
        fail_silently=False,
    )
    user.save()
