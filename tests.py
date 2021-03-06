"""Testsq for Balloonicorn's Flask app."""

import unittest
import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        """Code to run before every test."""

        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        """Can we reach the homepage?"""

        result = self.client.get("/")
        self.assertIn("having a party", result.data)

    def test_no_rsvp_yet(self):
        """Do users who haven't RSVPed see the correct view?"""

        # FIXME: Add a test to show we haven't RSVP'd yet
        result = self.client.get("/")
        self.assertIn("Please RSVP", result.data)

    def test_rsvp(self):
        """Do RSVPed users see the correct view?"""

        rsvp_info = {'name': "Jane", 'email': "jane@jane.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)
        self.assertIn("Party Details", result.data)
        self.assertNotIn("Please RSVP", result.data)

    def test_rsvp_mel(self):
        """Can we keep Mel out?"""

        rsvp_info = {'name': "Mel Melitopolski", 'email': "mel@ubermelon.com"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        self.assertNotIn("Party Details", result.data)

    def test_2_rsvp_mel(self):
        """Can we keep Mel out?"""

        rsvp_info = {'name': "mel MelITOPOlski", 'email': "MEL@UBERMELON.COM"}

        result = self.client.post("/rsvp", data=rsvp_info,
                                  follow_redirects=True)

        self.assertNotIn("Party Details", result.data)


if __name__ == "__main__":
    unittest.main()
