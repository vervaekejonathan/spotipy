import pprint
import sys

import spotipy
import spotipy.util as util

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0],))
    sys.exit()

scope = 'user-modify-playback-state'
token = util.prompt_for_user_token(username, scope)

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    sp.player_play('1026b96e9661c05a750f0c06870b2aaa46f588e6')
else:
    print("Can't get token for", username)
