import csv
from .models import Book

def import_books(csv_file_path):
    # Remove previous data
    Book.objects.all().delete()
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            Book.objects.create(
                Book_id=row['Book_Id'],
                Book_name=row['Book_name'],
                Author_name=row['Author_name'],
                isbn=row['isbn'],
                pages=row['pages'],
                publisher=row['publisher']
            )

import_books(r"C:\Users\Carlos\OneDrive\Desktop\books.csv")