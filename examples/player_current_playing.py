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
    currentplaying = sp.player_current_playing()
    print(currentplaying['item']['artists'][0]['name'])
    print(currentplaying['item']['name'])
else:
    print("Can't get token for", username)
