from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers.common import UserSerializer

class AccountView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request):
        user = request.user
        serialized_user = UserSerializer(user, data=request.data, partial=True)
        serialized_user.is_valid(raise_exception=True)
        serialized_user.save()
        return Response(serialized_user.data)

    def delete(self, request):
        user = request.user
        user.delete()
        return Response(status=204)