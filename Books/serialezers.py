# describe the process of going from python object to jason
from rest_framework import serializers

from .models import Book, Members, Transaction


class bookserialzer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class Memberserializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = '__all__'


class Transactionserializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
