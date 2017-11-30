import uuid

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf

(TARGET_ENTRY_TEXT, TARGET_ENTRY_PIXBUF) = range(2)
(COLUMN_TEXT, COLUMN_PIXBUF) = range(2)

DRAG_ACTION = Gdk.DragAction.MOVE

class DragSource(Gtk.EventBox):

    registry = {}

    def __init__(self, **kwargs):
        super(Gtk.EventBox, self).__init__(**kwargs)
        self.uuid = uuid.uuid4().hex
        self.registry[self.uuid] = self
        self.set_above_child(True)

        self.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
        self.connect("drag-data-get", self.drag_begin_handler)
        self.drag_source_add_text_targets()

        self.connect("destroy", self.destroy) # May have to be emitted manually

    def destroy(self, w):
        del self.registry[self.uuid]

    def drag_begin_handler(self, widget, context, data, info, time):

        data.set_text(self.uuid, 32)

class DragDest(Gtk.Grid):

    def __init__(self, *args, **kwargs):

        super(Gtk.Grid, self).__init__(*args, **kwargs)

        self.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)
        self.connect("drag-data-received", self.drag_received_handler)
        self.drag_dest_add_text_targets()

    def drag_received_handler(self, widget, context, x, y, data, info, time):
        
        uuid = data.get_text()
        source = DragSource.registry[uuid]

        print(x, y)

        # parent = source.get_parent()
        # parent.remove(source)
        # widget.pack_start(source, False, False, 0)

        Gtk.drag_finish(context, True, True, time)

class DragDropWindow2(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Drag and Drop Demo")

        hbox = Gtk.Grid(orientation=Gtk.Orientation.HORIZONTAL)
        hbox.set_column_spacing(12)

        left_vbox = DragDest(orientation=Gtk.Orientation.VERTICAL)
        left_vbox.set_row_spacing(10)
        hbox.add(left_vbox)
        right_vbox = DragDest(orientation=Gtk.Orientation.VERTICAL)
        right_vbox.set_row_spacing(10)
        hbox.add(right_vbox)

        self.labels = list()
        for i in range(10):
            l = Gtk.Button.new_with_label("Label number %d" % i)
            source = DragSource()
            source.add(l)

            if i % 2 == 0:
                left_vbox.add(source)
            else:
                right_vbox.add(source)

        self.add(hbox)

# class DragDropWindow(Gtk.Window):

#     def __init__(self):
#         Gtk.Window.__init__(self, title="Drag and Drop Demo")

#         hbox = Gtk.Box(spacing=12)

#         left_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
#         left_vbox.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)
#         left_vbox.connect("drag-data-received", self.drag_received_handler)
#         left_vbox.drag_dest_add_text_targets()
#         hbox.pack_start(left_vbox, True, True, 0)
#         right_vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
#         right_vbox.drag_dest_set(Gtk.DestDefaults.ALL, [], DRAG_ACTION)
#         right_vbox.connect("drag-data-received", self.drag_received_handler)
#         right_vbox.drag_dest_add_text_targets()
#         hbox.pack_start(right_vbox, True, True, 0)

#         # hbox.pack_start(self.iconview, True, True, 0)
#         # hbox.pack_start(self.drop_area, True, True, 0)

#         self.labels = list()
#         for i in range(10):
#             l = Gtk.Button.new_with_label("Label number %d" % i)

#             l.drag_source_set(Gdk.ModifierType.BUTTON1_MASK, [], DRAG_ACTION)
#             l.connect("drag-data-get", self.drag_begin_handler, i)
#             l.drag_source_add_text_targets()

#             self.labels.append(l)

#             if i % 2 == 0:
#                 left_vbox.pack_start(l, False, False, 0)
#             else:
#                 right_vbox.pack_start(l, False, False, 0)

#         self.add(hbox)

#     def drag_begin_handler(self, widget, context, data, info, time, i):

#         data.set_text(str(i), -1)

#     def drag_received_handler(self, widget, context, x, y, data, info, time):

#         label = self.labels[int(data.get_text())]
#         parent = label.get_parent()
#         parent.remove(label)
#         widget.pack_start(label, False, False, 0)

#         Gtk.drag_finish(context, True, True, time)

def main():
    win = DragDropWindow2()
    win.connect("delete-event", Gtk.main_quit)
    win.show_all()
    Gtk.main()

if __name__ == "__main__":
    main()
