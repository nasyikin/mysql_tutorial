from django.db import models
from django.utils import timezone

# Create your models here.
class Summary(models.Model):
  doctor_id = models.ForeignKey('auth.User')
  rn = models.CharField(max_length=10)
  admit_date = models.DateTimeField()
  discharge_date = models.DateTimeField(blank=True, null=True)
  ward_id = models.CharField(max_length=3)
  physicians = models.TextField()
  chief_complaint = models.TextField()
  main_diagnosis = models.TextField()
  comorbidity = models.TextField()
  procedures = models.TextField()
  medications = models.TextField()
  advice = models.TextField()
  appointment = models.TextField()
  referrer = models.TextField()
  created_date = models.DateTimeField(default = timezone.now)
  published_date = models.DateTimeField(blank=True, null=True)

  def publish(self):
    self.published_date = timezone.now()
    self.save()

  def __str__(self):
    return self.rn