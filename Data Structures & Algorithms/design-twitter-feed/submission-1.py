from collections import defaultdict
import heapq


# Approach:
# - Store each user's tweets in posting order with increasing timestamps.
# - Put each relevant user's newest tweet in a min-heap. Negate the timestamp
#   so the newest tweet comes out first.
# - After popping a tweet, add that author's next older tweet. Stop at 10.
class Twitter:
    def __init__(self):
        self.time = 0
        self.tweetMap = defaultdict(list)  # userId -> [(time, tweetId)]
        self.followMap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetMap[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> list[int]:
        feed, minHeap = [], []
        self.followMap[userId].add(userId)
        for authorId in self.followMap[userId]:
            tweets = self.tweetMap[authorId]
            if tweets:
                tweetIdx = len(tweets) - 1
                time, tweetId = tweets[tweetIdx]
                heapq.heappush(minHeap, (-time, tweetId, authorId, tweetIdx - 1))

        while minHeap and len(feed) < 10:
            _, tweetId, authorId, tweetIdx = heapq.heappop(minHeap)
            feed.append(tweetId)

            if tweetIdx >= 0:
                time, olderTweetId = self.tweetMap[authorId][tweetIdx]
                heapq.heappush(
                    minHeap, (-time, olderTweetId, authorId, tweetIdx - 1)
                )

        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].discard(followeeId)