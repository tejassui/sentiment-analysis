import tweepy
from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd

consumerkey = "xx"
consumersecret = "xx"
accesstoken = "xx"
accesstokensecret = "xx"

auth = tweepy.OAuthHandler(consumerkey, consumersecret)
auth.set_access_token(accesstoken, accesstokensecret) #accessrequest through object
api = tweepy.API(auth) #CONNECTIVITY ESTABLISHED

searchterm = input("enter keyword to search: ")
noofterms = int(input("enter no. of terms to search: "))

#becomes a list
public_tweets = tweepy.Cursor(api.search_tweets, q=searchterm, lang = "en").items(noofterms)
public_tweets = list(public_tweets)
print(len(public_tweets))


tweets_list = []
tweets_catg = []
pol = []
neutral = 0
pos = 0
neg = 0
cnt = 1

for tweet in public_tweets:
    print(cnt, tweet.text)
    cnt+=1
    analysis=TextBlob(tweet.text)
    print(analysis)
    tweets_list.append(tweet.text.replace("\n", " ").replace("\t", " ").strip())
    pol.append(analysis.sentiment.polarity)
    
    if analysis.sentiment.polarity==0:
        neutral+=1
        tweets_catg.append("Neutral")
    elif analysis.sentiment.polarity>0:
        pos+=1
        tweets_catg.append("Positive")
    elif analysis.sentiment.polarity<0:
        neg+=1
        tweets_catg.append("Negative")
    
print(neutral,pos,neg)

df = pd.DataFrame(tweets_list)
df.rename(columns={0:"Tweets"},inplace=True)
df["Polarity"] = pol
df["Review category"] = tweets_catg
df

df2 = pd.DataFrame(df["Review category"].value_counts())
df2


df2.plot(kind="bar").plot("bar")
#df2.plot(kind="kde").plot("kde")
#df2.plot(kind="box").plot("box")
#df2.plot(kind="density").plot("density")
#df2.plot(kind="area")
plt.show()
