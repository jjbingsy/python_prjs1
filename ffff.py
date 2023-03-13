import os
import gi
gi.require_version('Gst', '1.0')
from gi.repository import Gst, GLib

Gst.init(None)

def on_pad_added(element, pad):
    # Link the newly created pad to the next element in the pipeline
    next_element = element.get_next()
    pad.link(next_element.get_static_pad('sink'))

def announce_media(client, path):
    # Get the list of video files in the directory
    files = [f for f in os.listdir(path) if f.endswith('.mp4')]
    client.send('\n'.join(files))

def stream_video(client, path, filename):
    # Create the pipeline for the video stream
    pipeline = Gst.ParsedLaunch.new(f'souphttpsrc location=file:///{os.path.join(path, filename)} ! decodebin ! videoconvert ! x264enc ! rtph264pay ! rtph264depay ! avdec_h264 ! autovideosink')
    pipeline.bus.add_signal_watch()
    pipeline.bus.connect('message', on_message)

    # Start the pipeline
    pipeline.set_state(Gst.State.PLAYING)

    # Run the main loop
    GLib.MainLoop().run()

def on_message(bus, message):
    # Handle messages from the pipeline
    t = message.type
    if t == Gst.MessageType.ERROR:
        err, debug = message.parse_error()
        print(err, debug)
        GLib.MainLoop().quit()
    elif t == Gst.MessageType.EOS:
        GLib.MainLoop().quit()

if __name__ == '__main__':
    # Stream the video
    stream_video('D:\\newtrust', 'ADN-421.mp4')
