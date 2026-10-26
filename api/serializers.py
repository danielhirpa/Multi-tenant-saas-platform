from rest_framework import serializers
from .models import Workspace, Invoice, Subscription

class WorkspaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workspace
        fields = ['id', 'name', 'slug', 'owner', 'created_at']
        read_only_fields = ['owner']

class InvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'workspace', 'amount', 'due_date', 'status', 'created_at']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['id', 'workspace', 'plan', 'status', 'updated_at']