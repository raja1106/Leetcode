class TrieNode:
    def __init__(self):
        self.children = {}      # name → TrieNode
        self.isFile = False
        self.content = ""

class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def _traverse(self, path: str) -> TrieNode:
        node = self.root
        if path == "/":
            return node
        parts = path.strip("/").split("/")
        for part in parts:
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
        return node

    def ls(self, path: str) -> list[str]:
        node = self._traverse(path)
        if node.isFile:
            return [path.strip("/").split("/")[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self._traverse(path)  # Just creates intermediate directories

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self._traverse(filePath)
        node.isFile = True
        node.content += content

    def readContentFromFile(self, filePath: str) -> str:
        node = self._traverse(filePath)
        return node.content
