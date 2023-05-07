from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from user_app.models import FriendshipRequest, Friendship
from django.db.models import Q


class CreateProfileTestCase(TestCase):
    """
    The test creates a user and checks the correctness of the process
    """
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create(username='dj_tester', password='123')

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def test_create_profile(self):
        expected_user = User.objects.get(username='dj_tester')
        self.assertEqual(expected_user, self.user)


class SendRequestTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tester_sender = User.objects.create(username='tester_sender', password='123')
        cls.tester_receiver = User.objects.create(username='tester_receiver', password='123')

    def setUp(self):
        self.client.force_login(self.tester_sender)

    @classmethod
    def tearDownClass(cls):
        cls.tester_sender.delete()
        cls.tester_receiver.delete()

    def test_send_request(self):
        response = self.client.post(reverse("user_app:account", kwargs={"pk": self.tester_receiver.pk}),
                                    data={"send_request": True})
        expexted_request = FriendshipRequest.objects.get(request_from=self.tester_sender, request_to=self.tester_receiver)
        self.assertIsNotNone(expexted_request)


class AutoReceivingTwoRequestsTestCase(TestCase):
    """
    The test checks the system of automatic acceptance of two-way applications and the formation of friendship
    """
    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create(username='tester_sender', password='123')
        cls.user_2 = User.objects.create(username='tester_receiver', password='123')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()
        cls.user_2.delete()

    def test_auto_receiving_two_requests(self):
        self.client.force_login(self.user_1)
        response = self.client.post(reverse("user_app:account", kwargs={"pk": self.user_2.pk}),
                                    data={"send_request": True})

        self.assertRedirects(response, reverse("user_app:account", kwargs={"pk":  self.user_2.pk}))
        request_from_1 = FriendshipRequest.objects.get(request_from=self.user_1, request_to=self.user_2)
        self.assertIsNotNone(request_from_1)
        self.client.force_login(self.user_2)
        response = self.client.post(reverse("user_app:account", kwargs={"pk": self.user_1.pk}),
                                    data={"send_request": True})
        self.assertRedirects(response, reverse("user_app:account", kwargs={"pk":  self.user_1.pk}))
        request_from_2 = FriendshipRequest.objects.get(request_from=self.user_2, request_to=self.user_1)
        self.assertIsNotNone(request_from_2)
        friendship = Friendship.objects.filter(Q(member_1=self.user_1, member_2=self.user_2) |
                                               Q(member_1=self.user_2, member_2=self.user_2))
        self.assertEqual(friendship.first(), friendship.last())
        new_friendship = friendship.first()
        self.assertEqual(new_friendship.member_1, self.user_1)
        self.assertEqual(new_friendship.member_2, self.user_2)
        self.client.logout()


class RequestReceivingTestCase(TestCase):
    """
    The test checks the system acceptance of the application and the creation of friendship
    """
    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create(username='tester_sender', password='123')
        cls.user_2 = User.objects.create(username='tester_receiver', password='123')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()
        cls.user_2.delete()

    def test_request_receiving(self):
        self.client.force_login(self.user_1)
        response = self.client.post(reverse("user_app:account", kwargs={"pk": self.user_2.pk}),
                                    data={"send_request": True})
        self.assertRedirects(response, reverse("user_app:account", kwargs={"pk":  self.user_2.pk}))
        request = FriendshipRequest.objects.get(request_from=self.user_1, request_to=self.user_2)
        self.assertIsNotNone(request)
        self.client.force_login(self.user_2)
        response = self.client.post(reverse("user_app:account", kwargs={"pk": self.user_1.pk}),
                                    data={"accept_request": True})
        self.assertRedirects(response, reverse("user_app:account", kwargs={"pk":  self.user_1.pk}))
        friendship = Friendship.objects.filter(Q(member_1=self.user_1, member_2=self.user_2) |
                                               Q(member_1=self.user_2, member_2=self.user_2))
        self.assertEqual(friendship.first(), friendship.last())
        new_friendship = friendship.first()
        self.assertEqual(new_friendship.member_1, self.user_1)
        self.assertEqual(new_friendship.member_2, self.user_2)
        self.client.logout()


class RequestRejectionTestCase(TestCase):
    """
    The test checks the application rejection system
    """
    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create(username='tester_sender', password='123')
        cls.user_2 = User.objects.create(username='tester_receiver', password='123')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()
        cls.user_2.delete()

    def test_request_rejection(self):
        self.client.force_login(self.user_1)
        response = self.client.post(reverse("user_app:account", kwargs={"pk": self.user_2.pk}),
                                    data={"send_request": True})
        self.assertRedirects(response, reverse("user_app:account", kwargs={"pk":  self.user_2.pk}))
        request = FriendshipRequest.objects.get(request_from=self.user_1, request_to=self.user_2)
        self.assertIsNotNone(request)
        self.client.force_login(self.user_2)
        response = self.client.post(reverse("user_app:account", kwargs={"pk": self.user_1.pk}),
                                    data={"reject_request": True})
        self.assertRedirects(response, reverse("user_app:account", kwargs={"pk":  self.user_1.pk}))
        friendship = Friendship.objects.filter(Q(member_1=self.user_1, member_2=self.user_2) |
                                               Q(member_1=self.user_2, member_2=self.user_2))
        self.assertEqual(friendship.first(), friendship.last())
        new_friendship = friendship.first()
        self.assertEqual(new_friendship, None)
        self.client.logout()


class CancelReceiversRequestTestCase(TestCase):
    """
    The test checks the system of cancellation of the sent application by the sender
    """
    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create(username='tester_sender', password='123')
        cls.user_2 = User.objects.create(username='tester_receiver', password='123')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()
        cls.user_2.delete()

    def test_cancel_receivers_request(self):
        self.client.force_login(self.user_1)
        response = self.client.post(reverse("user_app:account", kwargs={"pk": self.user_2.pk}),
                                    data={"send_request": True})
        self.assertRedirects(response, reverse("user_app:account", kwargs={"pk":  self.user_2.pk}))
        is_request = FriendshipRequest.objects.filter(request_from=self.user_1, request_to=self.user_2).exists()
        self.assertTrue(is_request)
        response = self.client.post(reverse("user_app:account", kwargs={"pk": self.user_2.pk}),
                                    data={"cancel_request": True})
        self.assertRedirects(response, reverse("user_app:account", kwargs={"pk":  self.user_2.pk}))
        is_request = FriendshipRequest.objects.filter(request_from=self.user_1, request_to=self.user_2).exists()
        self.assertFalse(is_request)
        self.client.logout()


class RemoveFromFriendsTestCase(TestCase):
    """
    The test checks the removal system from friends
    """
    @classmethod
    def setUpClass(cls):
        cls.user_1 = User.objects.create(username='tester_sender', password='123')
        cls.user_2 = User.objects.create(username='tester_receiver', password='123')

    @classmethod
    def tearDownClass(cls):
        cls.user_1.delete()
        cls.user_2.delete()

    def test_request_rejection(self):
        self.client.force_login(self.user_1)
        self.client.post(reverse("user_app:account", kwargs={"pk": self.user_2.pk}),
                         data={"send_request": True})
        self.client.force_login(self.user_2)
        self.client.post(reverse("user_app:account", kwargs={"pk": self.user_1.pk}),
                         data={"accept_request": True})
        is_friendship = Friendship.objects.filter(Q(member_1=self.user_1, member_2=self.user_2) |
                                                  Q(member_1=self.user_2, member_2=self.user_2)).exists()
        self.assertTrue(is_friendship)
        self.client.post(reverse("user_app:account", kwargs={"pk": self.user_1.pk}),
                         data={"remove_friend": True})
        is_friendship = Friendship.objects.filter(Q(member_1=self.user_1, member_2=self.user_2) |
                                                  Q(member_1=self.user_2, member_2=self.user_2)).exists()
        self.assertFalse(is_friendship)
        self.client.logout()
