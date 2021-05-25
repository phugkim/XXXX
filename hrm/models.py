from django.db import models
from django.utils import timezone

# Create your models here.
# models.CharField(max_length=255)
# models.TextField()
# models.IntegerField()
# models.BigIntegerField()
# models.PositiveIntegerField()
# models.FloatField()
# models.BooleanField()
# models.OneToOneField()
# models.ForeignKey()

class Person(models.Model):
    name = models.CharField(max_length=255, unique=True, null=False, blank=True)
    description = models.TextField()
    phone_number = models.PositiveIntegerField()
    is_live = models.BooleanField()
    amount = models.FloatField()
    extra_name = models.CharField(max_length=250, editable=False, default="null")
    create_at = models.DateTimeField(default=timezone.now())
    update_at = models.DateTimeField(default=timezone.now())

    #Các model dựng sẵn của Django: delete(), save, __str__,...
    def __str__(self):
        return f"{self.name}"
        #return f"{self.name} - {self.phone_number} - {self.update_at.strftime('%m/%d/%Y, %H:%M:%S')}"
        #return self.name
        class Meta:
            ordering= {"-create_at"}
    def save(self,*args,**kwargs):
        self.extra_name = f"{self.name} - {self.phone_number}"
        super().save(*args, **kwargs)
class ModelX(models.Model):
    test_content = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="Person")
    mileage = models.FloatField()
    create_at = models.DateTimeField(default=timezone.now())
    update_at = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return f"{self.test_content} - {self.mileage}"
