from Company.models import Account

class AuthenticationBackends:
    def authenticate(self, email = None, password = None):
        try:
            user = Account.objects.get(email = email)
        except Exception:
            print 'no such user'
        else:
            if user.check_password(password):
                return user
        return None

    def get_user(self, user_id):
        try:
            return Account.objects.get(pk = user_id)
        except Exception:
            print 'no such user'
            return None
