from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.


class MyAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, phone_number, password=None):
        if not email:
            raise ValueError("Email Missing")
        if not first_name:
            raise ValueError("First Name Missing")
        if not last_name:
            raise ValueError("Last Name Missing")
        if not phone_number:
            raise ValueError("Phone Number Missing")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, phone_number, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,

        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    first_name = models.CharField(max_length=24)
    last_name = models.CharField(max_length=24)
    phone_number = PhoneNumberField()
    date_joined = models.DateTimeField(
        auto_now_add=True, verbose_name='date joined')
    last_login = models.DateTimeField(
        auto_now=True, blank=True, null=True, verbose_name='last login')
    is_superuser = models.BooleanField(
        default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')
    is_staff = models.BooleanField(
        default=False, help_text='Designates whether the user can log into this admin site. Mine', verbose_name='staff status')
    is_admin = models.BooleanField(
        default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')
    is_active = models.BooleanField(
        default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number']

    object = MyAccountManager()

    def __str__(self):
        return self.first_name

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Menu(models.Model):
    food_item_name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return "%i, %s" % (self.id, self.food_item_name)


STATUS = [
    ('A', 'Received'),  # Red
    ('B', 'Accepted'),  # Yellow
    ('C', 'Ready'),  # Green
    ('F', 'Canceled'),  # Grey
]


class Order(models.Model):
    customer = models.ForeignKey(Account, on_delete=models.CASCADE)
    order_content = models.JSONField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    time = models.DateTimeField(
        auto_now_add=True, verbose_name='date joined')
    status = models.CharField(max_length=1, choices=STATUS)
    payment_id = models.CharField(
        max_length=255, verbose_name='PayPal paymentID')
    payer_id = models.CharField(max_length=255, verbose_name='PayPal payerID')
    last_modifed = models.DateTimeField(
        auto_now=True, blank=True, null=True, verbose_name='last modifed')
    comment = models.CharField(max_length=255)

    def __str__(self):
        return "%i, %s" % (self.id, self.customer)
