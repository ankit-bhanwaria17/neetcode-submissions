class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []
        for word in strs:
            result.append(str(len(word)) + "#" + word)
        return "".join(result)

    def decode(self, s: str) -> List[str]:
        length = ""
        res = []
        i = 0
        while i < len(s):
            if s[i] == "#":
                word = s[i+1:i+1+int(length)]
                res.append(word)
                i = i+int(length)+1
                length = ""
            elif s[i].isdigit():
                length = length + s[i]
                i += 1
        return res
        