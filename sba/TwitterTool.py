import sys
import logging
from sba.models import Tweet, SearchTerm, Region, Topic
sys.path.append("tweepy/".encode("utf-8"))
import tweepy
logging.basicConfig(level=logging.DEBUG)
modStrConKey = "m8gDPJLNhJevZusJQ7pxA"
modStrConSec = "3CNxg3fi7GLFqAnKG9kMXBtwi8o4L7m4gEdcvA5Iw"
modStrAccKey = "28868957-BB6Cn48MwWlqkIMBIWPe97XQZ7SzBjPuCUWxmK24"
modStrAccSec = "96KjPEdIXiCtwS2SOr7U7UOQt3Slk2d5ZIdYxxdvRE"

modAuth = tweepy.OAuthHandler(modStrConKey, modStrConSec)
modAuth.set_access_token(modStrAccKey, modStrAccSec)
modTwitterApi = tweepy.API(modAuth)
# modTwitterApi.


class StreamListener(tweepy.StreamListener):
    wex = Region.create("Wexford")

    count = 0
    strCleanedTweet = ""
    def on_status(self, tweet):

        if(self.count < 100):

            if("RT @" not in tweet.text):  # remove retweets
                Tweet.create(tweet.text, self.wex)  # store tweet
                self.count += 1

        else:
            return False


    def on_timeout(self):
        print  'Timeout...'
        return True  # Don't kill the stream

    def on_error(self, status_code):
        print('Error Test: ' + repr(status_code))
        return False








def Run():

    l = StreamListener()
    setTerms = []
    obtopic = Topic.objects.get(name="Top Four")
    qs = SearchTerm.objects.filter(topic=obtopic)
    for item in qs.values():
        setTerms.append(item['term'])
    try:
        streamer = tweepy.Stream(auth=modAuth, listener=l)
        streamer.filter(track=setTerms)

    except AttributeError:
        print(sys.exc_info()[0])
        streamer.disconnect()
        logging.exception("Att Exc!")


# if __name__=="__main__":
#     Run()
# collect tweets given geocode and search terms
# def CollectTweets(lstStrSearchTerms, strGeocode, intItems):
#   lstOfLstsTweetValues = []
#   lstOfIds = []
#   InitTweetUtils()
#   intLastId = GetValueFromDB("lastid")
#   count = 0
#   logging.info(lstStrSearchTerms)
#   logging.info(intLastId)
#   for result in tweepy.Cursor(modTwitterApi.search, q=lstStrSearchTerms, since_id=intLastId, geocode='%s,%s,%s' % (53.000, -8, '270km')).items(200):
#     count = count + 1
#     lstOfLstsTweetValues.append([result.text, result.__getstate__().get("location", "noLocat").encode("utf-8")])
#     lstOfIds.append(result.id)
#   logging.info("Count: %d" % (count))
#   if sum(lstOfIds) > 0:
#     WriteValueToDB([("lastid", max(lstOfIds))])
#   logging.info(lstOfLstsTweetValues)
#   return lstOfLstsTweetValues
#
# def InitTweetUtils():
#   if modDbTweetUtilsManager.CheckHasEntities() == False:
#      modDbTweetUtilsManager.InitTweetUtils([("lastid", 0)])
#
#   else:
#     return
#
# def CollectTweets(strHashTag, intItems):
#   for result in tweepy.Cursor(modTwitterApi.search, q=strHashTag, locale="Ireland"):
#     logging.info(result.user)
#
# def GetValueFromDB(strKey):
#   # Return value
#   return modDbTweetUtilsManager.ReturnPropertyOfTweetUtils(strKey)
#
# def WriteValueToDB(lstUpdateValues):
#   modDbTweetUtilsManager.UpdateTweetUtils(lstUpdateValues)

