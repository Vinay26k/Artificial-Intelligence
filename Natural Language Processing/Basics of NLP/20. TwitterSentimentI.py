from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json

import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

import sentiment_mod as s
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
        #print(user+' - '+tweet.translate(non_bmp_map))
        sentiment_value, confidence = s.sentiment(tweet)
        print(user+' - '+tweet.translate(non_bmp_map),sentiment_value, confidence)

        if confidence*100>=80:
            output = open("twitter-out.txt","a")
            fp = open("twitter-tweet.txt","a")
            output.write(sentiment_value)
            fp.write(str(sentiment_value)+' '+str(tweet.encode('utf-8'))+'\n')
            output.write('\n')
            output.close()
            fp.close()
        
        return(True)

    def on_error(self, status):
        print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
print("Connected")
f = open("twitter-out.txt",'w')
f.close()

twitterStream.filter(track=["happy"])
