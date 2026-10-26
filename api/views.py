import stripe
from django.conf import settings
from django.db import models
from rest_framework import viewsets, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Workspace, Invoice, Subscription
from .serializers import WorkspaceSerializer, InvoiceSerializer, SubscriptionSerializer

stripe.api_key = settings.STRIPE_SECRET_KEY

class WorkspaceViewSet(viewsets.ModelViewSet):
    serializer_class = WorkspaceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Workspace.objects.filter(models.Q(owner=user) | models.Q(members=user)).distinct()

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class InvoiceViewSet(viewsets.ModelViewSet):
    serializer_class = InvoiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_workspaces = Workspace.objects.filter(models.Q(owner=user) | models.Q(members=user))
        workspace_id = self.request.query_params.get('workspace_id')
        if workspace_id:
            return Invoice.objects.filter(workspace_id=workspace_id, workspace__in=user_workspaces)
        return Invoice.objects.filter(workspace__in=user_workspaces)

class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        user_workspaces = Workspace.objects.filter(models.Q(owner=user) | models.Q(members=user))
        return Subscription.objects.filter(workspace__in=user_workspaces)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_checkout_session(request):
    workspace_id = request.data.get('workspace_id')
    try:
        workspace = Workspace.objects.get(id=workspace_id)
        
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price': 'price_1xyz_your_stripe_price_id',
                'quantity': 1,
            }],
            mode='subscription',
            success_url='http://localhost:3000/dashboard?success=true',
            cancel_url='http://localhost:3000/dashboard?canceled=true',
            client_reference_id=str(workspace.id),
        )
        return Response({'url': checkout_session.url})
    except Exception as e:
        return Response({'error': str(e)}, status=400)