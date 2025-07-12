import cloudinary
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from ..models import Item
from ..serializers import ItemSerializer

class ItemCreateView(generics.CreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        # 1. Upload image to Cloudinary
        image_file = request.FILES.get('image')
        if not image_file:
            return Response({"error": "Image file is required"}, status=status.HTTP_400_BAD_REQUEST)

        upload_result = cloudinary.uploader.upload(image_file)
        image_url = upload_result.get('secure_url')

        # 2. Prepare data for serializer
        data = request.data.copy()
        data['image_url'] = image_url

        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    


class MylistItemsView(generics.ListAPIView):
    serializer_class = ItemSerializer   
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        user=request.user
        my_items=Item.objects.filter(user=user).order_by('-created_at')
        seriralizer=ItemSerializer(my_items,many=True)
        return Response(seriralizer.data,status=200)

    
