import os.path
from datetime import datetime

from test.db import Session
from test.constants import top_dir
from rockaway.models import Artist, Album, Track, Playlist, Artwork

resources_dir = os.path.join(top_dir, "resources")

combat_rock_cover = Artwork(Location=os.path.join(resources_dir, "220px-The_Clash_-_Combat_Rock.jpg"))

ramones = Artist(Name="Ramones")
the_clash = Artist(Name="The Clash", Rating=4)
talking_heads = Artist(Name="Talking Heads", Genre="New Wave")

ramones_album = Album(Artist=ramones, Title="Ramones", Date=1976, Genre="Punk Rock")
rocket_to_russia = Album(Artist=ramones, Title="Rocket to Russia", Date=1977, Rating=3, trackCount=14)
london_calling = Album(Artist=the_clash, Title="London Calling", Date=1979, Rating=5)
combat_rock = Album(Artist=the_clash, Title="Combat Rock", Date=1982, Artwork=combat_rock_cover)
remain_in_light = Album(Artist=talking_heads, Title="Remain in Light")
once_in_a_lifetime = Album(Artist=talking_heads, Title="Once in a Lifetime", Compilation=True,
                           DiscCount=3)

rockaway_beach = Track(Artist=ramones, Album=rocket_to_russia, Title="Rockaway Beach",
                       Location=,# TODO: Add track files
                       FileSize=, Time=126000, Genre="Punk Rock", BitRate=128,
                       TrackNum=2, Rating=4, PlayCount=12, SkipCount=3,
                       DateAdded=datetime(2017,11,21,12,14,47),
                       LastPlayed=datetime(2017,12,1,15,0,0))
