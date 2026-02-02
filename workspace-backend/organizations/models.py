from django.db import models
from django.conf import settings
import uuid 
# Create your models here.

class Organization(models.Model):
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return self.name


class Membership(models.Model):
    class Role(models.TextChoices):
        OWNER = "OWNER", "owner"
        ADMIN = "ADMIN", "admin"
        MEMBER = "MEMBER", "member" 

 
    id = models.UUIDField(primary_key=True,default=uuid.uuid4, editable=False,unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name="memberships")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="memberships")
    role = models.CharField(max_length = 10, choices=Role.choices, default=Role.MEMBER)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes =[
            models.Index(fields=["organization","user"])
        ]
        constraints = [
            models.UniqueConstraint(fields=["organization","user"],  name="uniq_membership_org_user")
          
        ]

    def __str__(self):
         return f"{self.user_id} in {self.organization_id} ({self.role})"
