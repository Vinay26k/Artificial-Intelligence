from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
#print(x.translate(non_bmp_map))

#consumer key, consumer secret, access token, access secret.
import twitterCred as tc
ckey= tc.ckey
csecret= tc.csecret
atoken= tc.atoken
asecret= tc.asecret

class listener(StreamListener):

    def on_data(self, data):
        all_data = json.loads(data)
        user = all_data['user']['screen_name']
        tweet = all_data['text']
        print(user+' - '+tweet.translate(non_bmp_map))
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
print("Connected")
twitterStream.filter(track=["Happy"])
