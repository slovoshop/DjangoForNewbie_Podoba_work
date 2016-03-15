
from django.test import TestCase
from django.http import HttpRequest
from datetime import datetime

from students.models.students import Student
from students.models.groups import Group

from students.util import get_current_group


class UtilsTestCase(TestCase):
    """Test functions from util module"""

    def setUp(self):
        # create 2 groups
        group1, created = Group.objects.get_or_create(
            id=1,
            title="Group1")
        group2, created = Group.objects.get_or_create(
            id=2,
            title="Group2")

        # create student
        student, created = Student.objects.get_or_create(
            id=1,
            first_name="Vitaliy",
            last_name="Podoba",
            birthday=datetime.today(),
            ticket='12345')
        
        # set student as leader for group1
        group1.leader = student
        group1.save()

    def test_get_current_group(self):
        # prepare request object to pass to utility function
        request = HttpRequest()

        # test with no group set in cookie
        request.COOKIES['current_group'] = ''
        self.assertEqual(None, get_current_group(request))

        # test with invalid group id
        request.COOKIES['current_group'] = '12345'
        self.assertEqual(None, get_current_group(request))

        # test with proper group identificator
        group = Group.objects.filter(title='Group2')[0]
        request.COOKIES['current_group'] = str(group.id)
        self.assertEqual(group, get_current_group(request))

