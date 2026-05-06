class Twitter:

    def __init__(self):
        self.time = 0
        self.posts = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts[userId].append((self.time, tweetId))
        self.time -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        merged = []
        self.following[userId].add(userId)
        for user in self.following[userId]:
            if user in self.posts:
                index = len(self.posts[user]) - 1
                count, tweet = self.posts[user][index]
                heapq.heappush(merged, [count, tweet, user, index - 1])
        result = []
        while len(merged) > 0 and len(result) < 10:
            count, tweet, user, index = heapq.heappop(merged)
            result.append(tweet)
            if index >= 0:
                count, tweet = self.posts[user][index]
                heapq.heappush(merged, [count, tweet, user, index - 1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.following[followerId]:
            self.following[followerId].remove(followeeId)
