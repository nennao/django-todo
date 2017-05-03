# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from accounts.serializers import UserSerializer


# Create your views here.

class UserView(APIView):
    """
    UserView handles the requests made to `/accounts/`
    """
    permission_classes = ()

    def post(self, request):
        """
        Handles the POST request made to the `/accounts/` URL.

        This view will take the `data` property from the `request` object,
        deserialize it into a `User` object and store in the DB.

        Returns a 201 (successfully created) if the user is successfully
        created, otherwise returns a 400 (bad request)
        """
        serializer = UserSerializer(data=request.data)

        # Check to see if the data in the `request` is valid.
        # If the cannot be deserialized into a Todo object then
        # a bad request respose will be returned.
        # Else, save the data and return the data and a successfully
        # created status
        if not serializer.is_valid():
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        else:
            data = serializer.data
            # Create a new user using the `username` contained in
            # the `data` dict
            user = User.objects.create(username=data["username"])
            # Use the `set_password` method to create a hashed password
            # using the password provided in the `data` dict
            user.set_password(data["password"])
            # Finally, save the new `user` object
            user.save()
            return Response(data, status=status.HTTP_201_CREATED)

    # def get(self, request, pk=None):
    #     """
    #     Handle the GET request for the `/todo/` endpoint.
    #     Checks to see if a primary key has been provided by the URL.
    #     If not, a full list of `todo` will be retrieved. If a primary key
    #     has been provided then only that instance will be retrieved
    #     Returns the serialized `todo` object(s).
    #     """
    #     if pk is None:
    #         user_items = User.objects.all()
    #         # Serialize the data retrieved from the DB and serialize
    #         # them using the `TodoSerializer`
    #         serializer = UserSerializer(user_items, many=True)
    #         # Store the serialized data `serialized_data`
    #         serialized_data = serializer.data
    #         return Response(serialized_data)
    #     else:
    #         # Get the object containing the pk provided by the URL
    #         user = User.objects.get(id=pk)
    #         # Serialize the `todo` item
    #         serializer = UserSerializer(user)
    #         # Store it in the serialized_data variable and return it
    #         serialized_data = serializer.data
    #         return Response(serialized_data)
