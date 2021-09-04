from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class MyModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        if username is None:
            username = kwargs.get(User.USERNAME_FIELD)
        try:
            user = User.objects.filter(email=username).first()
        except User.DoesNotExist:
            return None
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user