# https://leetcode.com/problems/word-ladder

class Solution:
    def isConnected(self, a: str, b: str) -> bool:
        diff = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                diff += 1
            if diff > 1:
                return False
        return True

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        # add beginWord to list
        wordList.append(beginWord)
        n = len(wordList)

        # build adjacency list graph
        graph = {word: [] for word in wordList}

        for i in range(n):
            for j in range(i + 1, n):
                if self.isConnected(wordList[i], wordList[j]):
                    graph[wordList[i]].append(wordList[j])
                    graph[wordList[j]].append(wordList[i])

        # BFS
        q = deque()
        q.append((beginWord, 1))
        vis = set()
        vis.add(beginWord)

        while q:
            curr, dist = q.popleft()
            if curr == endWord:
                return dist

            for word in graph[curr]:
                if word not in vis:
                    vis.add(word)
                    q.append((word, dist + 1))

        return 0