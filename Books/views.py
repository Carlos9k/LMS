from django.db.models import Q
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book, Members, Transaction


# class view looking for prifex which is function name and suffix with is the template name

# Create your views here.
class BookList(ListView):
    model = Book
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        search_input = self.request.GET.get('Search-area') or ''
        if search_input:
            # Filter tasks where title or author starts with the search input
            context['books'] = context['books'].filter(
                Q(title__startswith=search_input) | Q(authors__startswith=search_input)
            )
        else:
            context['books'] = context['books'].all()  # If no search input, return all tasks

        context['search-input'] = search_input

        return context


class BookDetail(DetailView):
    model = Book
    context_object_name = 'book'


class BookCreate(CreateView):
    model = Book
    fields = '__all__'  # listout all the the fields
    # so when we create an item redirect the user to books -- "book_list"
    success_url = reverse_lazy('books')


class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'
    success_url = reverse_lazy('books')


class BookDelete(DeleteView):
    model = Book
    fields = '__all__'
    context_object_name = 'book'
    success_url = reverse_lazy('books')


# ------------------------------------------Members--------------------------------#
class MemberList(ListView):
    model = Members
    context_object_name = 'members'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     search_input = self.request.GET.get('Search-area') or ''
    #     if search_input:
    #         # Filter tasks where title or author starts with the search input
    #         context['books'] = context['books'].filter(
    #             Q(title__startswith=search_input) | Q(authors__startswith=search_input)
    #         )
    #     else:
    #         context['books'] = context['books'].all()  # If no search input, return all tasks
    #
    #     context['search-input'] = search_input
    #
    #     return context


class MemberDetail(DetailView):
    model = Members
    context_object_name = 'member'


class MemberCreate(CreateView):
    model = Members
    fields = ('Member_name',)  # listout all the the fields
    # so when we create an item redirect the user to books -- "book_list"
    success_url = reverse_lazy('members')


class MemberUpdate(UpdateView):
    model = Members
    fields = '__all__'
    success_url = reverse_lazy('members')


class MemberDelete(DeleteView):
    model = Members
    fields = '__all__'
    context_object_name = 'member'
    success_url = reverse_lazy('members')


# --------------------------------------------Transactions -----------------------------#
class TransactionList(ListView):
    model = Transaction
    context_object_name = 'transactions'


class TransactionDetail(DetailView):
    model = Transaction
    context_object_name = 'transaction'


class TransactionCreate(CreateView):
    model = Transaction
    fields = '__all__'  # listout all the the fields
    # so when we create an item redirect the user to books -- "book_list"
    success_url = reverse_lazy('transactions')


class TransactionUpdate(UpdateView):
    model = Transaction
    fields = '__all__'
    success_url = reverse_lazy('transactions')


class TransactionDelete(DeleteView):
    model = Transaction
    fields = '__all__'
    context_object_name = 'transaction'
    success_url = reverse_lazy('transactions')
