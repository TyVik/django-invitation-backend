import os
from django.conf import settings
from django.test import TestCase

from invitation.users import UserModel

class BaseTestCase(TestCase):
    def setUp(self):
        super(BaseTestCase, self).setUp()
        settings.TEMPLATE_DIRS = (
            os.path.join(os.path.dirname(__file__), 'templates'),
        )
        UserModel().objects.create_user('testuser',
                                 'testuser@example.com',
                                 'testuser')

    def user(self):
        return UserModel().objects.get(username='testuser')
