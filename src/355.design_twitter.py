from typing import List
from collections import defaultdict
from queue import PriorityQueue

_auto_increment = 0


class Tweet:
    def __init__(self, id_):
        self.id = id_
        global _auto_increment
        self.auto_id = _auto_increment
        _auto_increment += 1

    def __lt__(self, other):
        """小顶堆比较函数, 最早的在堆顶"""
        return self.auto_id < other.auto_id


class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # user_id: [twitter_id]
        self.user_twitter = defaultdict(list)
        self.user_following = defaultdict(set)
        self.tweet = {}

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        """
        Compose a new tweet.
        """
        if tweet_id in self.tweet:
            raise ValueError('tweet_id already exist!')
        self.tweet[tweet_id] = Tweet(tweet_id)
        self.user_twitter[user_id].append(tweet_id)

    def getNewsFeed(self, user_id: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        queue = PriorityQueue(10)

        def put_tweet(u_id):
            for tweet_id in self.user_twitter[u_id][-10:]:
                if queue.full():
                    top_tweet = queue.get()
                    if top_tweet < self.tweet[tweet_id]:
                        nearly_tweet = self.tweet[tweet_id]
                    else:
                        nearly_tweet = top_tweet
                    queue.put(nearly_tweet)
                else:
                    queue.put(self.tweet[tweet_id])

        put_tweet(user_id)
        for uid in self.user_following[user_id]:
            if uid != user_id:
                put_tweet(uid)

        res = []
        while not queue.empty():
            tweet = queue.get()
            res.append(tweet.id)
        # 结果是最早到最近 需要翻转一下
        return res[::-1]

    def follow(self, follower_id: int, followee_id: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        self.user_following[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.user_following[follower_id].discard(followee_id)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(user_id,tweetId)
# param_2 = obj.getNewsFeed(user_id)
# obj.follow(follower_id,followee_id)
# obj.unfollow(follower_id,followee_id)


if __name__ == '__main__':
    inp1 = ["Twitter", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
            "postTweet",
            "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet",
            "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "postTweet", "getNewsFeed", "follow",
            "getNewsFeed", "unfollow", "getNewsFeed"]
    inp2 = [[], [1, 5], [2, 3], [1, 101], [2, 13], [2, 10], [1, 2], [1, 94], [2, 505], [1, 333], [2, 22], [1, 11],
            [1, 205],
            [2, 203], [1, 201], [2, 213], [1, 200], [2, 202], [1, 204], [2, 208], [2, 233], [1, 222], [2, 211], [1],
            [1, 2],
            [1], [1, 2], [1]]
    twitter = eval(f'{inp1[0]}()')
    for i in range(1, len(inp1)):
        print(eval(f'twitter.{inp1[i]}{tuple(inp2[i])}'))
