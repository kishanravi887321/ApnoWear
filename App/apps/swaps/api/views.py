from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from ..models import Purchase
from ..serializers import PurchaseSerializer

class MyPurchasesView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        purchases = Purchase.objects.filter(buyer=request.user).order_by('-purchased_at')
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data)
