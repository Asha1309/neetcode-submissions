class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        count = {}

        for word in words:
            for ch in word:
                count[ch] = 1 + count.get(ch, 0)

        for freq in count.values():
            if freq % len(words) != 0:
                return False

        return True
        