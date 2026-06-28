from django.db import models
from django.utils import timezone


class user(models.Model):
    NAME = models.CharField(max_length=50)
    AGE = models.IntegerField()
    USERNAME = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    EMAIL = models.CharField(max_length=50)
    PHONENUMBER = models.IntegerField()
    STATUS=models.IntegerField(default=2)

    def __str__(self):
        return self.NAME

class makeupartist(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    phonenumber = models.IntegerField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    photo = models.FileField()
    email = models.CharField(max_length=50)
    license = models.FileField()
    location = models.CharField(max_length=40)
    time = models.CharField(max_length=50)
    ACTION = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class login(models.Model):
    USERNAME = models.CharField(max_length=50)
    PASSWORD = models.CharField(max_length=50)
    STATUS = models.CharField(max_length=50)


    def __str__(self):
             return self.USERNAME


class payments(models.Model):
    NAME = models.CharField(max_length=50)
    ARTISTNAME = models.CharField(max_length=50)
    EMAILID = models.CharField(max_length=50)
    DATE = models.DateField(default=timezone.now)
    # DATE = models.DateField(default=True)
    TIME = models.TimeField(default=True)
    AMOUNT = models.IntegerField()


    def __str__(self):
             return self.NAME

class booking(models.Model):
    NAME = models.CharField(max_length=50)
    USERNAME = models.CharField(max_length=50)
    # USERADDRESS = models.CharField(max_length=50)
    EMAIL = models.CharField(max_length=50)
    PHONENUMBER = models.IntegerField()
    ARTISTNAME = models.CharField(max_length=50)
    # ARTISTEMAIL = models.CharField(max_length=50)
    ADDSERVICE = models.CharField(max_length=10)
    APPOINTMENTDATE = models.DateField(default=True)
    APPOINTMENTTIME = models.TimeField(default=True)
    # PHONENUMBER = models.IntegerField(max_length=10)
    ACTION = models.CharField(max_length=50)



    def __str__(self):
        return self.NAME

class cancel(models.Model):
    REASONFORCANCELLATION = models.CharField(max_length=100)

    def __str__(self):
        return self.REASONFORCANCELLATION




# class order(models.Model):
#     NAME = models.CharField(max_length=50)
#     USERADDRESS = models.CharField(max_length=50)
#     USEREMAIL = models.CharField(max_length=50)
#     PHONENUMBER = models.IntegerField(max_length=10)
#     ARTISTNAME = models.CharField(max_length=50)
#     ARTISTEMAIL = models.CharField(max_length=50)
#     BOOKINGDESCRIPTION = models.IntegerField(max_length=10)
#     APPOINTMENTDATE = models.DateField(default=True)
#     APPOINTMENTTIME = models.TimeField(default=True)
#     PHONENUMBER = models.IntegerField()
#     STATUS = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.USERNAME

class PasswordReset(models.Model):
    user=models.ForeignKey(user,on_delete=models.CASCADE)
    token=models.CharField(max_length=4)



class complaint(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    makeupartistname = models.CharField(max_length=50)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    comp = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class feedback(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    makeupartistname=models.CharField(max_length=40)
    email = models.EmailField()
    phonenumber = models.IntegerField()
    fdbk = models.CharField(max_length=150)
    def __str__(self):
        return self.name



class service(models.Model):
    username = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    addservice = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    amount = models.IntegerField()

    def __str__(self):
        return self.name

class adpay(models.Model):
    username=models.CharField(max_length=60)
    amount=models.IntegerField()
    date = models.DateField(default=timezone.now)
    artistname=models.CharField(max_length=50)
    def __str__(self):
        return self.username

class appointment(models.Model):
    name=models.CharField(max_length=20)
    email=models.CharField(max_length=60)
    phone_num = models.IntegerField()
    username=models.CharField(max_length=20)
    artistname=models.CharField(max_length=30)
    booking_date=models.DateField(default=True)
    booking_time=models.TimeField(default=True)
    service=models.CharField(max_length=10)
    action=models.CharField(max_length=20)
    def __str__(self):
        return self.name

class gallery(models.Model):
    artistname = models.CharField(max_length=30)
    photo = models.FileField()
    def __str__(self):
        return self.artistname