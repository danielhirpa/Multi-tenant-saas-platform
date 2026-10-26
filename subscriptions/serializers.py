from rest_framework import serializers
from .models import Subscription

class SubscriptionSerializer(serializers.ModelSerializer):
    workspace_name = serializers.ReadOnlyField(source='workspace.name')

    class Meta:
        model = Subscription
        fields = ['id', 'workspace', 'workspace_name', 'stripe_subscription_id', 'status', 'current_period_end', 'created_at']