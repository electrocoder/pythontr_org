# -*- coding: utf-8 -*-

from django.test import TestCase
from django.contrib.auth.models import User, Group

from django.core.urlresolvers import reverse
from django.core import mail

fixtures = ['groups.json', 'users.json', 'profiles.json', 'categories.json', 'posts.json']


class UserFunctionalTestsForAnonymousUser(TestCase):
    pass
     

class UserFunctionalTestsForAuthor(TestCase):
    pass


class UserFunctionalTestsForAuthenticatedUser(TestCase):
    pass


class UserUnitTests(TestCase):
    pass