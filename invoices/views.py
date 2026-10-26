from rest_framework import viewsets, permissions
from .models import Invoice, Subscription
from .serializers import InvoiceSerializer, SubscriptionSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Invoice.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Subscription.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Update or create user subscription when selecting a plan
        sub, created = Subscription.objects.update_or_create(
            user=self.request.user,
            defaults={'plan': self.request.data.get('plan', 'Pro'), 'status': 'Active'}
        )
        serializer.instance = sub