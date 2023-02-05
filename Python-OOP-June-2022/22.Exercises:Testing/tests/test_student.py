from project.student import Student

import unittest


class StudentTest(unittest.TestCase):
    STUDENT_NAME = "Gosho"

    def setUp(self) -> None:
        self.student = Student(self.STUDENT_NAME)
        self.student2 = Student(self.STUDENT_NAME, {'Python Basics': ['note1']})

    def test__init_without_courses__expect_to_create_instance(self):
        self.assertEqual(self.STUDENT_NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test__init_with_courses__expect_to_create_instance(self):
        courses = {'Python Basics': ['note1']}
        student = Student(self.STUDENT_NAME, courses)
        self.assertEqual(self.STUDENT_NAME, student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_when_course_name_in_courses__expect_adding_course_to_the_courses(self):
        course_name = 'Python Basics'
        notes = ['note2']
        add_course_notes = ""
        result = self.student2.enroll(course_name, notes, add_course_notes)
        self.assertEqual("Course already added. Notes have been updated.", result)

        expected_courses = {'Python Basics': ['note1', 'note2']}
        self.assertEqual(expected_courses, self.student2.courses)

    def test_enroll_when_add_course_notes__expect_updated_notes_Y(self):
        course_name = 'Python Basics'
        notes = ['note3']
        add_course_notes = "Y"
        result = self.student.enroll(course_name, notes, add_course_notes)
        self.assertEqual("Course and course notes have been added.", result)

        expected_courses = {course_name: notes}
        self.assertEqual(expected_courses, self.student.courses)

    def test_enroll_when_add_course_notes__expect_updated_notes(self):
        course_name = 'Python Basics'
        notes = ['note3']
        add_course_notes = ""
        result = self.student.enroll(course_name, notes, add_course_notes)
        self.assertEqual("Course and course notes have been added.", result)

        expected_courses = {course_name: notes}
        self.assertEqual(expected_courses, self.student.courses)

    def test_enroll_when_course_notes_arg_is_invalid__expect_adding_course_with_empty_notes(self):
        course_name = 'Python Fund'
        notes = ['note2']
        add_course_notes = "N"
        result = self.student.enroll(course_name, notes, add_course_notes)
        self.assertEqual("Course has been added.", result)

        expected_courses = {course_name: []}
        self.assertEqual(expected_courses, self.student.courses)

    def test_add_notes_when_course_is_valid__expect_added_notes_to_the_course(self):
        course_name = 'Python Basics'
        notes = 'note2'

        result = self.student2.add_notes(course_name, notes)
        self.assertEqual("Notes have been updated", result)

        expected_courses = {'Python Basics': ['note1', 'note2']}
        self.assertEqual(expected_courses, self.student2.courses)

    def test_add_notes_when_course_is_invalid__expect_exception(self):
        course_name = 'Python'
        notes = 'note2'

        with self.assertRaises(Exception) as context:
            self.student2.add_notes(course_name, notes)

        self.assertIsNotNone(context)
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_leave_course_when_course_name_is_invalid__expect_exception(self):
        course_name = 'Python'

        with self.assertRaises(Exception) as context:
            self.student2.leave_course(course_name)

        self.assertIsNotNone(context)
        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))

    def test_leave_course_when_course_name_is_valid__expect_remove_course(self):
        course_name = 'Python Basics'

        result = self.student2.leave_course(course_name)
        self.assertEqual("Course has been removed", result)
        expected_courses = {}
        self.assertEqual(expected_courses, self.student2.courses)


if __name__ == '__main__':
    unittest.main()
