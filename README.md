# Introduction

Rockaway is a highly flexible, maximalist music player written in Python. I am writing it, first and foremost, for myself as an audiophile and a music lover with a large library. I initially used iTunes to organize and play my music, enjoying the large number of features and options it afforded for organizing my music. (But not its continually increasing size). I switched to Banshee when I stopped using Windows for everything except gaming, writing a variety of Python scripts that interact with its SQLite backend to recreate the iTunes capabilities it lacks. I have been happily using Banshee for the last six or so years, but am looking for something that is actively supported and with more of the power I enjoyed from iTunes, minus the cruft. As a Python programmer with over five years of software development experience, this seems like the perfect time to realize my old dream of writing my own music player.

## Development Goals

More succinctly, my priorities for Rockaway are the following:

* Power user features such as I used to enjoy in iTunes--defining smart playlists with arbitrary boolean expressions, assistance keeping music files and the database in sync
* Optimized performance on large (tens of thousands of songs) libraries.
* Python scripting capability to allow users to extend Rockaway even more easily than I extended Banshee.
* An flexible graphical interface with a fully customizable layout and a loose coupling to the backend.
* Customizable hotkeys, including the option to control the player while it is out of focus.
* Built-in analytics for exploring your listening history (maybe no one else is interested in this feature, but I am).
