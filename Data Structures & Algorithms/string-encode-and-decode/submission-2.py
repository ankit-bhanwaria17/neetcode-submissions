class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ""
        for s in strs:
            code += str(len(s)) + "#" + s
        return code

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        size = ""
        while i < len(s):
            if s[i].isdigit():
                size += s[i]
                i += 1
            else:
                size = int(size)
                word = s[i+1:i+1+size]
                res.append(word)
                i = i+1+size
                size = ""

        return res
                

