# -*- coding: utf -8-*-

from django.test import TestCase
from django.contrib.auth.models import User

from django.core.urlresolvers import reverse
from pythontr_org.polls.models import Poll, Vote, Choice


class PollFunctionalTestsForAnonymousUser(TestCase):
    pass


class PollFunctionalTestsForAuthenticatedUser(TestCase):
    pass


class VoteUnitTests(TestCase):
    pass