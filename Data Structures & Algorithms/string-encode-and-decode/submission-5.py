class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        i = j = 0
        result = []
        while i < len(s):
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            i = j + 1
            j = i + size
            result.append(s[i:j])
            i = j
        return result
