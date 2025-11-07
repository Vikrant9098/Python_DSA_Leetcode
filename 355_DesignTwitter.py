import heapq  # used for priority queue (to get recent tweets easily)

class Twitter(object):

    def __init__(self):
        self.time = 0  # keeps track of tweet order (timestamp)
        self.tweets = {}  # stores user's tweets: userId -> list of (time, tweetId)
        self.following = {}  # stores follow relationships: userId -> set of followees

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        if userId not in self.tweets:  # if user has no tweets yet
            self.tweets[userId] = []  # create an empty list for tweets
        self.tweets[userId].append((self.time, tweetId))  # add tweet with timestamp
        self.time += 1  # increase time for next tweet

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """
        heap = []  # max heap to get tweets by most recent first

        # add user's own tweets to heap
        if userId in self.tweets:
            for t in self.tweets[userId]:  # loop through all tweets by user
                heapq.heappush(heap, (-t[0], t[1]))  # push (-time, tweetId) to heap

        # add tweets of users that this user follows
        if userId in self.following:
            for followee in self.following[userId]:  # loop through followees
                if followee in self.tweets:  # check if followee has tweets
                    for t in self.tweets[followee]:  # loop through followee's tweets
                        heapq.heappush(heap, (-t[0], t[1]))  # push to heap (most recent first)

        res = []  # list to store result tweets
        while heap and len(res) < 10:  # get up to 10 most recent tweets
            res.append(heapq.heappop(heap)[1])  # pop tweetId from heap and add to result

        return res  # return final news feed list

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId == followeeId:  # cannot follow self
            return
        if followerId not in self.following:  # if user has no follow list yet
            self.following[followerId] = set()  # create a new follow set
        self.following[followerId].add(followeeId)  # add followee to set

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.following:  # if follower exists in map
            self.following[followerId].discard(followeeId)  # safely remove followee if present


# Example usage:
# obj = Twitter()                           # create Twitter object
# obj.postTweet(1, 5)                       # user 1 posts tweet 5
# print(obj.getNewsFeed(1))                 # returns [5]
# obj.follow(1, 2)                          # user 1 follows user 2
# obj.postTweet(2, 6)                       # user 2 posts tweet 6
# print(obj.getNewsFeed(1))                 # returns [6, 5]
# obj.unfollow(1, 2)                        # user 1 unfollows user 2
# print(obj.getNewsFeed(1))                 # returns [5]
