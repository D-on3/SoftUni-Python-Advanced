from project.library import Library

import unittest


class LibraryTests(unittest.TestCase):
    NAME = 'City Library'
    BOOKS_BY_AUTHORS = {'author1': ['book1'], 'author2': ['book3']}
    READERS = {'reader1': [], 'reader2': []}

    def setUp(self) -> None:
        self.library = Library(self.NAME)

    def test__init__whit_books_and_readers__expect_instance(self):
        self.library.books_by_authors = self.BOOKS_BY_AUTHORS
        self.library.readers = self.READERS

        self.assertEqual(self.NAME, self.library.name)
        self.assertEqual(self.BOOKS_BY_AUTHORS, self.library.books_by_authors)
        self.assertEqual(self.READERS, self.library.readers)

    def test_name_setter_when_invalid__expect_ValueError(self):
        # name = 'ChangeName'
        # self.library.name = name
        # self.assertTrue(hasattr(self.library, '_Library__name'))
        # self.assertEqual(getattr(self.library, '_Library__name'), name)
        # self.assertEqual(self.library.name, name)

        with self.assertRaises(ValueError) as error:
            Library('')

        self.assertIsNotNone(error)
        error_message = "Name cannot be empty string!"
        self.assertEqual(error_message, str(error.exception))

    def test_name_setter_when_name_valid__expect_instance(self):
        name = 'valid_name'
        lib = Library(name)
        self.assertEqual(name, lib.name)
        self.assertEqual({}, lib.books_by_authors)
        self.assertEqual({}, lib.readers)

    def test_add_book__expect_adding_to_the_list(self):
        author = 'author1'
        title = 'book1'
        title2 = 'book2'

        self.library.add_book(author, title)
        self.library.add_book(author, title)
        expected = {author: [title]}
        self.assertEqual(expected, self.library.books_by_authors)

        self.library.add_book(author, title2)
        expected = {author: [title, title2]}
        self.assertEqual(expected, self.library.books_by_authors)

    def test_add_book_when_author_and_book_added__expect_None(self):
        self.library.books_by_authors = self.BOOKS_BY_AUTHORS
        self.library.readers = self.READERS
        author = 'author1'
        book = 'book1'

        result = self.library.add_book(author, book)
        expected = {'author1': ['book1'], 'author2': ['book3']}
        self.assertEqual(expected, self.library.books_by_authors)
        self.assertIsNone(result)

    def test_add_reader_when_not_added__expect_adding(self):
        self.library.books_by_authors = self.BOOKS_BY_AUTHORS
        self.library.readers = self.READERS
        reader = 'reader3'

        self.library.add_reader(reader)
        expected = {'reader1': [], 'reader2': [], 'reader3': []}
        self.assertEqual(expected, self.library.readers)

    def test_add_reader_when_is_added__expect_message(self):
        self.library.books_by_authors = self.BOOKS_BY_AUTHORS
        self.library.readers = self.READERS

        added_reader = 'reader1'

        expected = {'reader1': [], 'reader2': []}

        message_actual = self.library.add_reader(added_reader)
        message_expected = f"{added_reader} is already registered in the {self.library.name} library."
        self.assertEqual(message_expected, message_actual)
        self.assertEqual(expected, self.library.readers)

    def test_rent_book_when_reader_not_in_readers__expect_message(self):
        self.library.books_by_authors = self.BOOKS_BY_AUTHORS
        self.library.readers = self.READERS
        reader = 'reader55'
        author = 'author1'
        book = 'book1'
        actual = self.library.rent_book(reader, author, book)
        expected = f"{reader} is not registered in the {self.library.name} Library."
        self.assertEqual(expected, actual)

    def test_rent_book_when_author_not_in_authors__expect_message(self):
        self.library.books_by_authors = self.BOOKS_BY_AUTHORS
        self.library.readers = self.READERS
        reader = 'reader1'
        author = 'author55'
        book = 'book1'
        actual = self.library.rent_book(reader, author, book)
        expected = f"{self.library.name} Library does not have any {author}'s books."

        self.assertEqual(expected, actual)

    def test_rent_book_when_title_not_in_books__expect_message(self):
        self.library.books_by_authors = self.BOOKS_BY_AUTHORS
        self.library.readers = self.READERS
        reader = 'reader1'
        author = 'author1'
        book = 'book55'
        actual = self.library.rent_book(reader, author, book)
        expected = f"""{self.library.name} Library does not have {author}'s "{book}"."""

        self.assertEqual(expected, actual)

    def test_rent_book_when_all_valid__expect_updating_reader_and_remove_book_from_author(self):
        self.library.books_by_authors = {'author1': ['book1'], 'author2': ['book3']}
        self.library.readers = {'reader1': [], 'reader2': []}
        reader = 'reader1'
        author = 'author1'
        book = 'book2'
        self.library.add_book(author, book)
        result = self.library.rent_book(reader, author, book)
        expected_readers = {'reader1': [{'author1': 'book2'}], 'reader2': []}
        expected_authors = {'author1': ['book1'], 'author2': ['book3']}

        self.assertEqual(expected_readers, self.library.readers)
        self.assertEqual(expected_authors, self.library.books_by_authors)
        self.assertIsNone(result)


if __name__ == '__main__':
    unittest.main()
