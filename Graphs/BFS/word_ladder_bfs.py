from collections import deque

def word_ladder(beginWord, endWord, wordList):

    wordSet = set(wordList)

    if endWord not in wordSet:
        return 0

    q = deque()

    q.append((beginWord, 1))

    visited = set()
    visited.add(beginWord)

    while q:

        word, steps = q.popleft()

        if word == endWord:
            return steps

        # try changing every position
        for i in range(len(word)):

            # try all letters a-z
            for ch in 'abcdefghijklmnopqrstuvwxyz':

                newWord = word[:i] + ch + word[i+1:]

                if newWord in wordSet and newWord not in visited:

                    visited.add(newWord)

                    q.append((newWord, steps + 1))

    return 0
