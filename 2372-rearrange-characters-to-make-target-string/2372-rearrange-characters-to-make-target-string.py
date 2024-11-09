class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        h1=Counter(target)
        h2=Counter(s)
        return (min(h2[char] // h1[char] for char in target))
