from typing import List
from collections import defaultdict
from datetime import datetime


class Twitter:
    def __init__(self):
        self.follower_mapping = defaultdict(set) # userId: {userId}
        # or just use a heap
        self.tweet_mapping = defaultdict(list) # userId: [(tweetId, ts)] 
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_mapping[userId].append((tweetId, self.timer))    
        self.timer+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        all_tweets = []
        for follower in set([userId, *self.follower_mapping[userId]]):
            all_tweets += self.tweet_mapping[follower]
        return [userId for userId, _ in sorted(all_tweets, key=lambda i: i[1], reverse=True)[:10]]    

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follower_mapping[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follower_mapping[followerId].discard(followeeId)

twitter = Twitter()
twitter.postTweet(1, 10) 
twitter.postTweet(2, 20) 
print(twitter.getNewsFeed(1))   
print(twitter.getNewsFeed(2))
twitter.follow(1, 2)     
print(twitter.getNewsFeed(1))
print(twitter.getNewsFeed(2))
twitter.unfollow(1, 2)   
print(twitter.getNewsFeed(1))
