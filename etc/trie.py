from collections import defaultdict

def enTrie(word, trie):
    len_word = len(word)
    now = trie
    for ch in word:
        now[len_word] += 1
        if ch not in now:
            now[ch] = defaultdict(int)
        now = now[ch]


def searchTrie(word, trie):
    len_word = len(word)
    now = trie
    for ch in word:
        if ch == '?':
            return now[len_word]
        if ch not in now:
            return 0
        now = now[ch]