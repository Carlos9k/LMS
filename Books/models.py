from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=1000)
    authors = models.CharField(max_length=1000)
    average_rating = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    isbn = models.CharField(max_length=10)
    isbn13 = models.CharField(max_length=13)
    language_code = models.CharField(max_length=100)
    num_pages = models.IntegerField()  # Assuming number of pages is an integer
    ratings_count = models.IntegerField()
    text_reviews_count = models.IntegerField()
    publication_date = models.DateField(null=True, blank=True)
    publisher = models.CharField(max_length=500)
    stock = models.IntegerField()
    DisplayFields = ['id', 'title', 'authors', 'average_rating', 'isbn', 'isbn13', 'language_code', 'num_pages',
                     'ratings_count',
                     'text_reviews_count', 'publication_date', 'publisher', 'stock']
    SearchFields = ['title', 'authors']

    def __str__(self):
        return self.title


# to create this table we have to make another migration

class Members(models.Model):
    id = models.AutoField(primary_key=True)
    Member_name = models.CharField(max_length=500)
    outstanding_debt = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    DisplayFields = ['id', 'Member_name', 'outstanding_debt']
    SearchFields = ['id', 'Member_name']

    def __str__(self):
        return self.Member_name


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Members, on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now_add=True)
    return_date=models.DateField(null=True, blank=True)
    rent_fee = models.DecimalField(max_digits=10, decimal_places=2)

    DisplayFields = ['id', 'book', 'member', 'issue_date', 'return_date', 'rent_fee']

    def __str__(self):
        return f"{self.book} issued to {self.member} on {self.issue_date} "

    def save(self, *args, **kwargs):
        # Decrease the stock of the book when the transaction is saved
        if self.pk is None:
            # Only decrease the stock for new transactions
            if self.book.stock > 0:
                self.book.stock -= 1
                self.book.save()
            else:
                raise ValueError("The book is out of stock")

        # Update member's outstanding debt for new transactions
        if self.pk is None:  # Check if an instance has already been saved to the database
            self.member.outstanding_debt += self.rent_fee  # Update outstanding debt
            self.member.save()  # Save the member instance to update outstanding debt

        # Check if the book is being returned
        if self.return_date is not None:
            # Increase stock of the book
            self.book.stock += 1
            self.book.save()

            # Update member's outstanding debt and reset rent fee to zero
            self.member.outstanding_debt -= self.rent_fee  # Remove rent fee from outstanding debt
            self.rent_fee = 0  # Set rent fee to zero
            self.member.save()  # Save the member instance to update outstanding debt

        # Call the superclass's save method
        super().save(*args, **kwargs)



