from django.db import models

# Create your models here.
class AllTeam(models.Model):
    team = models.CharField(max_length=255)
    team_type = models.CharField(max_length=255)
    team_name = models.CharField(max_length=255)
    team_description = models.CharField(max_length=6000)
    location_type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    work_type = models.CharField(max_length=255)

    def _str_(self):
        return self.team

    class Meta:
        db_table = 'teams'

class Application(models.Model):
    resume = models.FileField(upload_to='resumes/')
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    current_company = models.CharField(max_length=255)
    linkedin= models.CharField(max_length=255)
    github = models.CharField(max_length=255)
    websites = models.CharField(max_length=255)
    info = models.CharField(max_length=2000)
    title = models.CharField(max_length=255)
    job_name = models.CharField(max_length=255)
    def _str_(self):
        return self.name
    class Meta:
        db_table ='application_forms'

from django.db import models

class Job(models.Model):
    job_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "jobs"   # 👈 forces table name
