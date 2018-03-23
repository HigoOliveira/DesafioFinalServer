from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, phone, password, **extra_fields):
      if not phone:
        raise ValueError('O telefone não pode ser nulo')
      
      user = self.model(phone=phone, **extra_fields)
      user.set_password(password)
      user.save(using=self._db)
      return user
    
    def create_user(self, phone, password=None, **extra_fields):
      extra_fields.setdefault('is_superuser', False)
      return self._create_user(phone, password, **extra_fields)

    def create_superuser(self, phone, password=None, **extra_fields):
      extra_fields.setdefault('is_superuser', True)

      if extra_fields.get('is_superuser') is not True:
        raise ValueError('O campo is_superuser tem que ser True')

      return self._create_user(phone, password, **extra_fields)