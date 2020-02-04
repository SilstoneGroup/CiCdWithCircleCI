from django.test import TestCase
# from sample.nav_wrapper import
from sample.views import MockService
import mock
from django.core import mail
from django.core.mail import send_mail
import mandrill

# # Create your tests here.
# class UserTest(TestCase):
#     def setUp(self):
#         pass
#
#     def test_add(self):
#         self.assertEqual(2+2, 4)
#         # self.assertRais


def fake_print_name(self):
    return "Gunjan Mehta"


class MockTest(TestCase):
    def setUp(self):
        pass

    @mock.patch.object(MockService, 'print_name', fake_print_name)
    def test_mock_service_print_name(self):
        name = MockService().print_name()
        self.assertEqual(name, "Gunjan Mehta", "Ajnabee naam")
