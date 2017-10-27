from django.test.client import Client
from django.test import TestCase
from model_mommy import mommy
from django.core.urlresolvers import reverse
from users.models import Lageruser, Department

from users.models import Lageruser


class UserTests(TestCase):

    def setUp(self):
        '''method for setting up a client for testing'''
        self.client = Client()
        my_admin = Lageruser.objects.create_superuser('test', 'test@test.com', "test")
        self.client.login(username="test", password="test")

    def test_User_list(self):
        '''method for testing the presentation and reachability of the list of users over several pages'''
        user = mommy.make(Lageruser, _quantity=40)

        # testing if loading of device-list-page was successful (statuscode 2xx)
        url = reverse("user-list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

        # testing the presentation of only 30 results of query on one page
        self.assertEqual(len(resp.context["user_list"]), 30)
        self.assertEqual(resp.context["paginator"].num_pages, 2)

        # doesn't work
        # # testing the successful loading of second page of device-list (statuscode 2xx)
        # url = reverse("user-list", kwargs={"page": 2, "department":"my"})
        # resp = self.client.get(url)
        # self.assertEqual(resp.status_code, 200)



class LageruserTests(TestCase):
    def setUp(self):
        self.client = Client()
        myadmin = Lageruser.objects.create_superuser('test', "test@test.com", "test")
        self.client.login(username = "test", password = "test")

    def test_lageruser_creation(self):
        user1 = mommy.make(Lageruser, first_name = "a", last_name = "a")
        user2 = mommy.make(Lageruser, first_name = "", last_name = "a")
        self.assertEqual(user1.__unicode__(), u"{0} {1}".format(user1.first_name, user1.last_name) )
        self.assertEqual(user2.__unicode__(), user2.username)
        self.assertEqual(user1.get_absolute_url(), reverse('userprofile', kwargs={'pk': user1.pk}) )
        user1.clean()
        self.assertEqual(user1.expiration_date, None)


class DepartmentTests(TestCase):
    def setUp(self):
        self.client = Client()
        myadmin = Lageruser.objects.create_superuser('test', "test@test.com", "test")
        self.client.login(username = "test", password = "test")

    def test_department_creation(self):
        department = mommy.make(Department)
        self.assertEqual(department.__unicode__(), department.name)
