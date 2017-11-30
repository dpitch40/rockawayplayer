from unittest import TestCase
from rockaway.models import Track

class TestTrackBasics(TestCase):

    def test_track_create_no_args(self):

        track = Track()
        self.assertFalse(track.hasDbEntry())
        self.assertFalse(track.hasFile())

    def test_track_create(self):

        args = {"Title": "Rockaway Beach",
                "Artist": "The Ramones", # FIXME--This and album will not just be strings
                "Album": "Rocket to Russia",
                "Year": 1977,
                "Genre": "Punk Rock",
                "Time": 126000}

        track = Track(**args)
        self.assertEqual(track.Title, args["Title"])
        self.assertEqual(track.Year, 1977)
        # Alternate ways of looking up attributes
        self.assertEqual(track.genre, track.Genre)
        self.assertEqual(track.Time, track["Time"])
