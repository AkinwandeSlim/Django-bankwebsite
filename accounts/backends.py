from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model

class UsernameOrIDBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        User = get_user_model()
        try:
            if username.isdigit():
                user = User.objects.get(account_id=username)
            else:
                user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, account_id):
        try:
            return get_user_model().objects.get(pk=account_id)
        except get_user_model().DoesNotExist:
            return None
