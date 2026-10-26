from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import WorkspaceViewSet, InvoiceViewSet, SubscriptionViewSet, create_checkout_session

router = DefaultRouter()
router.register(r'workspaces', WorkspaceViewSet, basename='workspace')
router.register(r'invoices', InvoiceViewSet, basename='invoice')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')

urlpatterns = [
    path('', include(router.urls)),
    path('create-checkout-session/', create_checkout_session, name='create-checkout-session'),
]