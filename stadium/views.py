from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Stadium,Bookings
from .serializers import StadiumSerializer,BookingsSerializer
from accounts.permissions import IsOwnerOrReadOnly,IsAdminOrOwner
from rest_framework.response import Response
from rest_framework.views import APIView

class UserStadiumListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stadiums = Stadium.objects.all()
        serializer = StadiumSerializer(stadiums, many=True)
        return Response(serializer.data)


class UserStadiumList(generics.ListAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [IsAuthenticated]
    
class OwnerFieldList(generics.ListCreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly,IsAdminOrOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OwnerFieldDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly,IsAdminOrOwner]



class OwnerBookingList(generics.ListCreateAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly,IsAdminOrOwner]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class OwnerBookingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly,IsAdminOrOwner]
    
class BookingsCreateView(generics.CreateAPIView):
    queryset = Bookings.objects.all()
    serializer_class = BookingsSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        stadium_id = self.kwargs.get('stadium_id')
        stadium = Stadium.objects.get(id=stadium_id)
        user = self.request.user
        serializer.save(user=user, stadium=stadium)