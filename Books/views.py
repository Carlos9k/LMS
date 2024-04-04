from django.db.models import Q
from django.shortcuts import render
from .models import Book, Members, Transaction
from .serialezers import bookserialzer, Memberserializer, Transactionserializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# decrators is a somrthing u but above your function to describe its functionality
# Create your views here.
# --------------------------------------Book------------------------------------------------
@api_view(['GET', 'POST'])
def book_list(request):
    # get all data
    # serialize them
    # return jason
    if request.method == 'GET':
        # Get the search query parameter 'q' from the request
        query = request.GET.get('q')
        # If there's a search query
        if query:
            # Filter books by title or authors containing the search query (case-insensitive)
            books = Book.objects.filter(Q(title__icontains=query) | Q(authors__icontains=query))
        # If there's no search query
        else:
            # Get all books
            books = Book.objects.all()
        return render(request, 'Book/book_list.html', {'books': books})  # Render the HTML template with the books data

    # add book to database,it is going to be the same process but in the reverse order
    if request.method == 'POST':
        # take the data from the request
        serializer = bookserialzer(data=request.data)
        # check the method if it is valid
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return render(request, 'Book/book_list.html', {'books': serializer})



# the Response it commes from django frame work and its better to show up some functionality for a better data browsing

@api_view(['GET', 'PUT', 'DELETE'])
def Book_details(request, id):
    # so we could get the book by its id
    # first we have to throw an exceptin mmkn el id yb2a msh mwgood

    try:
        book = Book.objects.get(pk=id)
    except book.DoesNotExist:
        # so now when the id is not found the error msg will popup
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return render(request, 'Book/book_details.html', {'book': book})

    elif request.method == 'PUT':
        serializer = bookserialzer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------------------------------------------Members---------------------------------------------
@api_view(['GET', 'POST'])
def Members_list(request):
    if request.method == 'GET':
        members = Members.objects.all()  # Get all the data
        return render(request, 'Member/members_list.html', {'members': members})

    elif request.method == 'POST':
        # Initialize a serializer with the data from the request
        serializer = Memberserializer(data=request.data)

        # Check if the serializer is valid
        if serializer.is_valid():
            # If valid, save the data to the database
            serializer.save()

            # Retrieve the updated list of members from the database
            members = Members.objects.all()

            # Render the members list template with the updated list of members
            return render(request, 'Member/members_list.html', {'members': members})
        else:
            # If the serializer is not valid, render the members list template
            # with the original list of members and the serializer to display errors
            return render(request, 'Member/members_list.html',
                          {'members': Members.objects.all(), 'serializer': serializer})


@api_view(['GET', 'PUT', 'DELETE'])
def Members_details(request, id):
    try:
        member = Members.objects.get(pk=id)
    except member.DoesNotExist:
        # so now when the id is not found the error msg will popup
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return render(request, 'Member/members_details.html', {'member': member})

    elif request.method == 'PUT':
        serializer = Memberserializer(member, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return render(request, 'Member/members_details.html', {'member': serializer})

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        member.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ----------------------------------------------Records------------------------------

@api_view(['GET', 'POST'])
def transaction_list(request):
    if request.method == 'GET':
        transactions = Transaction.objects.all()
        # Pass the book titles and member names to the template context
        return render(request, 'Transaction/transaction_list.html', {'transactions': transactions})
        #serializer = Transactionserializer(transactions, many=True)


    elif request.method == 'POST':
        serializer = Transactionserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            #transaction=Transaction.objects.all()
            return render(request, 'Transaction/transaction_list.html', {'transactions': serializer})
        else:
            return render(request, 'Transaction/transaction_list.html',
                          {'transaction': Transaction.objects.all(), 'serializer': serializer})


@api_view(['GET', 'PUT', 'DELETE'])
def transaction_details(request, id):
    try:
        transaction = Transaction.objects.get(pk=id)
    except Transaction.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        return render(request, 'Transaction/transaction_list.html', {'transactions':transaction})

    elif request.method == 'PUT':
        serializer = Transactionserializer(transaction, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return render(request, 'Transaction/transaction_list.html', {'transactions': serializer})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        transaction.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




