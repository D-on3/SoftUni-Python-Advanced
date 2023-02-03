from project.bookstore import Bookstore
import unittest

class BookstoreTests(unittest.TestCase):


    def setUp(self) -> None:
        self.bookstore = Bookstore(5)

    def test__init(self):
        self.assertEqual(5, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test_books_limit_setter(self):
        book_limit = 0
        with self.assertRaises(ValueError) as error:
            b = Bookstore(book_limit)
        message = f"Books limit of {book_limit} is not valid"
        self.assertIsNotNone(error)
        self.assertEqual(message, str(error.exception))

        new_limit = 3
        bb = Bookstore(new_limit)
        self.assertEqual(new_limit, bb.books_limit)

    def test__len(self):
        self.bookstore.receive_book('book1', 1)
        self.bookstore.receive_book('book2', 2)
        expected = 3
        self.assertEqual(expected, len(self.bookstore))

    def test_receive_book(self):
        message1 = self.bookstore.receive_book('book1', 1)
        expected1 = {'book1': 1}
        self.assertEqual(expected1, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual("1 copies of book1 are available in the bookstore.", message1)

        message2 = self.bookstore.receive_book('book2', 2)
        expected = {'book1': 1, 'book2': 2}
        self.assertEqual(expected, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual("2 copies of book2 are available in the bookstore.", message2)

        message3 = self.bookstore.receive_book('book1', 2)
        new_expected = {'book1': 3, 'book2': 2}
        self.assertEqual(new_expected, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual("3 copies of book1 are available in the bookstore.", message3)

        with self.assertRaises(Exception) as context:
            self.bookstore.receive_book('book1', 2)

        self.assertIsNotNone(context)
        message = "Books limit is reached. Cannot receive more books!"
        self.assertEqual(message, str(context.exception))

    def test_sell_book(self):
        book_title = 'book2'
        book_title_invalid = 'book3'
        self.bookstore.receive_book('book1', 1)
        self.bookstore.receive_book('book2', 2)

        # if the book is not available in the bookstore
        error_message = "Book book3 doesn't exist!"
        with self.assertRaises(Exception) as context:
            self.bookstore.sell_book(book_title_invalid, 3)
        self.assertIsNotNone(context)
        self.assertEqual(error_message, str(context.exception))

        # if there is not enough copies of that book to sell
        error_message_not_enough_copies = "book1 has not enough copies to sell. Left: 1"
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book("book1", 2)
        self.assertIsNotNone(error)
        self.assertEqual(error_message_not_enough_copies, str(error.exception))

        # if can sell successfully
        expected_message = "Sold 2 copies of book2"
        actual = self.bookstore.sell_book(book_title, 2)
        self.assertEqual(expected_message, actual)
        self.assertEqual(2, self.bookstore.total_sold_books)
        self.assertEqual({'book1': 1, 'book2': 0}, self.bookstore.availability_in_store_by_book_titles)


    def test__str__(self):
        self.bookstore.receive_book('book1', 1)
        self.bookstore.receive_book('book2', 2)
        self.bookstore.sell_book('book2', 2)

        expected = '''Total sold books: 2
Current availability: 1
 - book1: 1 copies
 - book2: 0 copies'''
        actual = str(self.bookstore)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
