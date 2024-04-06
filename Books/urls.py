from django.urls import path
from .views import BookList, BookDetail, BookCreate, BookUpdate, BookDelete, MemberList, MemberDetail, MemberCreate ,MemberUpdate,\
    MemberDelete, TransactionList, TransactionCreate, TransactionUpdate , TransactionDelete

urlpatterns = [
    path("", BookList.as_view(), name='books'),
    path('book/<int:pk>/', BookDetail.as_view(), name='book'),
    path('book-create', BookCreate.as_view(), name='book-create'),
    path('book-update/<int:pk>/', BookUpdate.as_view(), name='book-update'),
    path('book-delete/<int:pk>/', BookDelete.as_view(), name='book-delete'),
    # ------------------------Members---------------------------------#
    path('members/', MemberList.as_view(), name='members'),
    path('members/<int:pk>/', MemberDetail.as_view(), name='member'),
    path('member-create', MemberCreate.as_view(), name='member-create'),
    path('member-update/<int:pk>/', MemberUpdate.as_view(), name='member-update'),
    path('member-delete/<int:pk>/', MemberDelete.as_view(), name='member-delete'),
    # ------------------------Transaction---------------------------------#
    path('transaction/', TransactionList.as_view(), name='transactions'),
    path('transaction-create/', TransactionCreate.as_view(), name='transaction-create'),
    path('transaction-update/<int:pk>/', TransactionUpdate.as_view(), name='transaction-update'),
    path('transaction-delete/<int:pk>/', TransactionDelete.as_view(), name='transaction-delete'),

]
