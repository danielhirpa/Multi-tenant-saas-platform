from rest_framework import viewsets
from .models import Subscription
from .serializers import SubscriptionSerializer

class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()  # <--- Make sure this line is here
    serializer_class = SubscriptionSerializer

    def get_queryset(self):
        queryset = self.queryset
        workspace_id = self.request.query_params.get('workspace')
        if workspace_id is not None:
            queryset = queryset.filter(workspace_id=workspace_id)
        return queryset