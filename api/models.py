from django.db import models
from django.contrib.auth.models import User

class Workspace(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owned_workspaces')
    members = models.ManyToManyField(User, related_name='workspaces', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Invoice(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='invoices', null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    due_date = models.DateField()
    status = models.CharField(max_length=50, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice #{self.id} - ${self.amount}"

class Subscription(models.Model):
    workspace = models.OneToOneField(Workspace, on_delete=models.CASCADE, related_name='subscription', null=True, blank=True)
    plan = models.CharField(max_length=50, default='Free Tier')
    status = models.CharField(max_length=50, default='Active')
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        plan_name = self.plan if self.plan else "No Plan"
        ws_name = self.workspace.name if self.workspace else "No Workspace"
        return f"{ws_name} - {plan_name}"