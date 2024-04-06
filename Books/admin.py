from django.contrib import admin
from .models import Book, Members, Transaction

# Register your models here.


admin.site.site_header = "Library Managment System"
admin.site.site_title = "LMS"


# @admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    fields = ('title', 'authors', 'average_rating', 'isbn', 'isbn13', 'language_code', 'num_pages',
              'ratings_count',
              'text_reviews_count', 'publication_date',
              'publisher', 'stock')  # control which fields are displayed in the admin interface
    list_display = Book.DisplayFields
    search_fields = Book.SearchFields
    list_display_links = ['stock']


admin.site.register(Book, BookAdmin)


# @admin.register(Members)
class MemberAdmin(admin.ModelAdmin):
    fields = ['Member_name']
    list_display = Members.DisplayFields
    search_fields = Members.SearchFields


admin.site.register(Members, MemberAdmin)


# @admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    fields = ('member', 'book', 'return_date', 'rent_fee')
    list_display = Transaction.DisplayFields
    list_display_links = ['return_date']


admin.site.register(Transaction, TransactionAdmin)
