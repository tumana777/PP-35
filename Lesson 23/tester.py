import unittest
# from main import add, sub, mul, div, is_even
from main import Student

# class Test(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(2, 3), 5)
#         self.assertEqual(add(-7, -8), -15)
#         self.assertEqual(add(-7, 9), 2)
#         self.assertEqual(add(7, -8), -1)
#         self.assertNotEqual(add(2, 3), 9)
#
#     def test_sub(self):
#         self.assertEqual(sub(2, 3), -1)
#         self.assertEqual(sub(-7, -8), 1)
#         self.assertEqual(sub(-7, 9), -16)
#         self.assertEqual(sub(7, -8), 15)
#         self.assertNotEqual(sub(2, 3), 0)
#
#     def test_mul(self):
#         self.assertEqual(mul(2, 3), 6)
#         self.assertEqual(mul(-7, -8), 56)
#         self.assertEqual(mul(-7, 9), -63)
#         self.assertEqual(mul(7, -8), -56)
#         self.assertNotEqual(mul(2, 3), 0)
#
#     def test_div(self):
#         self.assertEqual(div(2, 1), 2)
#         self.assertEqual(div(-8, -2), 4)
#         self.assertEqual(div(-15, 3), -5)
#
#         # self.assertRaises(ZeroDivisionError, div, 2, 0)
#
#         with self.assertRaises(ZeroDivisionError):
#             div(7, 0)
#
#     def test_is_even(self):
#         self.assertTrue(is_even(2))
#         self.assertFalse(is_even(3))
#         self.assertTrue(is_even(0))

class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student1 = Student("John", "Doe", 1000)
        self.student2 = Student("Jane", "Smith", 2000)

    def test_get_full_name(self):
        # student1 = Student("John", "Doe", 1000)
        # student2 = Student("Jane", "Smith", 2000)

        self.assertEqual(self.student1.get_full_name, "John Doe")
        self.assertEqual(self.student2.get_full_name, "Jane Smith")

    def test_get_email(self):
        # student1 = Student("John", "Doe", 1000)
        # student2 = Student("Jane", "Smith", 2000)

        self.assertEqual(self.student1.get_email("gmail.com"), "John.Doe@gmail.com")
        self.assertEqual(self.student1.get_email("yahoo.com"), "John.Doe@yahoo.com")
        self.assertEqual(self.student2.get_email("mail.ru"), "Jane.Smith@mail.ru")
        self.assertEqual(self.student2.get_email("mail.ge"), "Jane.Smith@mail.ge")

        self.student1.first_name = "Bob"
        self.student2.last_name = "White"

        self.assertEqual(self.student1.get_email("gmail.com"), "Bob.Doe@gmail.com")
        self.assertEqual(self.student2.get_email("mail.ge"), "Jane.White@mail.ge")

    def test_get_pay(self):
        # student1 = Student("John", "Doe", 1000)
        # student2 = Student("Jane", "Smith", 2000)

        self.student1.get_pay()
        self.student2.get_pay()

        self.assertEqual(self.student1.pay, 900)
        self.assertEqual(self.student2.pay, 1800)

if __name__ == '__main__':
    unittest.main()