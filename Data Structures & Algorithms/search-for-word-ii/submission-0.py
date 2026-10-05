class TrieNode:
    __slots__ = ("children", "isWord")

    def __init__(self):
        self.children = {}
        self.isWord = False

    def addWord(self, word: str) -> None:
        node = self

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.isWord = True


class Solution:
    def findWords(
        self, board: List[List[str]], words: List[str]
    ) -> List[str]:
        root = TrieNode()

        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        result = set()

        def dfs(r, c, parent, path):
            char = board[r][c]
            node = parent.children.get(char)

            if node is None:
                return

            path += char

            if node.isWord:
                result.add(path)

            board[r][c] = "#"

            for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    dfs(nr, nc, node, path)

            board[r][c] = char

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(result)