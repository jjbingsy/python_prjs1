import mpv

player = mpv.MPV()
player.loadfile("R:/141016-cheers.webm")
player.play()

player.wait_for_playback()