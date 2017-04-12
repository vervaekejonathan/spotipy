import pprint
import sys

import spotipy
import spotipy.util as util

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-read-playback-state'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    devices = sp.player_devices()
    device_ids = devices['devices'][0]['id']
    currentplaying = sp.player_update(device_ids)
else:
    print("Can't get token for", username)