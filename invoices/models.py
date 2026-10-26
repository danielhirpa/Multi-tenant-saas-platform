from django.db import models
from workspaces.models import Workspace

class Invoice(models.Model):
    workspace = models.ForeignKey(Workspace, on_delete=models.CASCADE, related_name='invoices')
    invoice_number = models.CharField(max_length=50)
    client_name = models.CharField(max_length=150)
    client_email = models.EmailField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(
        max_length=20,
        choices=[('draft', 'Draft'), ('sent', 'Sent'), ('paid', 'Paid')],
        default='draft'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Invoice #{self.invoice_number} - {self.workspace.name}"
