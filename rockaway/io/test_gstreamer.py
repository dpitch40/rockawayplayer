# See https://brettviren.github.io/pygst-tutorial-org/pygst-tutorial.pdf

import argparse

import gi
gi.require_version('Gst', '1.0')
gi.require_version('Gtk', '3.0')
from gi.repository import Gst, Gtk, GObject
Gst.init(None)
GObject.threads_init()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("fname")
    args = parser.parse_args()

    fname = args.fname

    player = Gst.ElementFactory.make("playbin", None)
    player.set_property("uri", "file://" + fname)
    player.set_state(Gst.State.PLAYING)

    Gtk.main()

if __name__ == "__main__":
    main()