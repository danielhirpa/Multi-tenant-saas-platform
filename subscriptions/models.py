from django.db import models
from workspaces.models import Workspace

class Subscription(models.Model):
    workspace = models.OneToOneField(Workspace, on_delete=models.CASCADE, related_name='subscription')
    stripe_subscription_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('trialing', 'Trialing'),
            ('active', 'Active'),
            ('past_due', 'Past Due'),
            ('canceled', 'Canceled')
        ],
        default='trialing'
    )
    current_period_end = models.DateTimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.workspace.name} - {self.status}"