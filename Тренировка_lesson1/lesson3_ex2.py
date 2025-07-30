from lesson3_book import Book

library = [
    Book("Сказка", "Пушкин"),
    Book("Роман", "Лермонтов"),
    Book("Стихи", "Барто"),
]


for book in library:
    print(f"{book.title} - {book.author}")
