import json

from django.core.urlresolvers import reverse
from django.test import TestCase

from tierlist.models import Fighter

class FightersAPITests(TestCase):

    def setUp(self):
        Fighter.objects.get_or_create(id=1)

    def test_list(self):
        url = reverse("fighters\\api")
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        data = json.loads(response.content)
        self.assertEquals(len(data), 1)
