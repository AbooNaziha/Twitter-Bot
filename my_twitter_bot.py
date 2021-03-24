import tweepy
import time

print("This is my twitter bot")

CONSUMER_KEY = '7ghiLqmm0BTIMLDMvDN73KV7s'
CONSUMER_SECRET = 'gF10Qd3q8xtBgcUV1zTcDsrANQ7Gg8KP1oWSJkOcBH81BPhXdX'
ACCESS_KEY = '1373509816715476992-8uQJ78DdIJU7hV1EugORGczRZPAfd1'
ACCESS_SECRET = 'BdnIE4d2hcLooYOWLdidI4f0ysG5k7ZNA0j9y7MS4JW6G'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

FILE_NAME = 'last_seen_id.txt'


def retrieve_last_seen_id(file_name):
    f_read = open(file_name, 'r')
    last_seen_id = int(f_read.read().strip())
    f_read.close()
    return last_seen_id


def store_last_seen_id(last_seen_id, file_name):
    f_write = open(file_name, 'w')
    f_write.write(str(last_seen_id))
    f_write.close()
    return


def reply_to_tweets():
    print('retrieving and replying to tweets...')
    # Note: use 1374647159220502531 for testing
    last_seen_id = retrieve_last_seen_id(FILE_NAME)
    mentions = api.mentions_timeline(last_seen_id, tweet_mode='extended')

    for mention in reversed(mentions):
        print(str(mention.id) + '-' + mention.full_text)
        last_seen_id = mention.id
        store_last_seen_id(last_seen_id, FILE_NAME)
        if '#machinelearning' in mention.full_text.lower():
            print('found #machinelearning!')
            print('responding back...')
            api.update_status('@' + mention.user.screen_name +
                              ' Welcome to #MachineLearning', mention.id)


while True:
    reply_to_tweets()
    time.sleep(15)
