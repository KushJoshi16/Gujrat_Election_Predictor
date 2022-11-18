import json
import tweepy
import os
import time

def print_tweetdata(n,ith_tweet,scraped_data):

    d = {"Tweet Scraped":n,"Username":ith_tweet[0],"Description":ith_tweet[1],"Location":ith_tweet[2],"Followinf Count":ith_tweet[3],"Followers Count":ith_tweet[4],"Total Tweets":ith_tweet[5], "Retweet Count":ith_tweet[6],"Tweet Text":ith_tweet[7],"Hashtags Used":ith_tweet[8]}
    # for i in range(0,9):
    #     print(f"{i+1} : {ith_tweet[i]}")
    print(n)
    scraped_data.append(d)
    try:
        if not os.path.isdir('scraped_twitter'):
            os.mkdir('scraped_twitter')
        with open('scraped_twitter/scraped_data.json','w') as outfile:
            json.dump(scraped_data, outfile, indent=4)
    except:
        print("An exception occured")


def scrape(words, numtweet, scraped_data):
    tweets = tweepy.Cursor(api.search_tweets , q=words, lang='en', tweet_mode='extended').items(numtweet)
    list_tweets = [tweet for tweet in tweets]

    i = 1

    for tweet in list_tweets:
        username = tweet.user.screen_name
        description = tweet.user.description
        location = tweet.user.location
        following = tweet.user.friends_count
        followers = tweet.user.followers_count
        totaltweets = tweet.user.statuses_count
        retweetcount = tweet.retweet_count
        hashtags = tweet.entities['hashtags']

        try : 
            text = tweet.retweeted_status.full_text
        except AttributeError:
            text = tweet.full_text
        hashtext = list()
        for j in range(0, len(hashtags)):
            hashtext.append(hashtags[j]['text'])

        ith_tweet = [username,description,location,following,followers,totaltweets,retweetcount,text,hashtext]

        print_tweetdata(i,ith_tweet,scraped_data)

        i = i+1

if __name__ == "__main__":
    f = open('Bihar_Elec_Predict/auth.json')
    data = json.load(f)
    access_token = data["access_token"]
    access_token_secret = data["access_token_secret"]
    api_key = data["api_key"]
    api_key_secret = data["api_key_secret"]
    f.close()
    auth = tweepy.OAuthHandler(api_key,api_key_secret)
    auth.set_access_token(access_token,access_token_secret)
    api = tweepy.API(auth)
    f = open("Bihar_Elec_Predict/search_param.json",encoding="utf-8")
    data = json.load(f)
    words = data["hashtag"]
    f.close()
    numtweet = data["tweet_num"]
    scraped_data = []
    print("Fetching tweets...")
    # wait_timer(15)
    # for i in range(15):
    #     time.sleep(60)
    #     print(f"{i} min left")
    for word in words:
        # try:
        print(word)
        scrape(word,numtweet,scraped_data)
        # except:
        #     continue
    print("Scraping complete")




