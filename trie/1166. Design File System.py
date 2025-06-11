class TrieNode:
    def __init__(self):
        self.children = {}
        self.val = None


class FileSystem:
    def __init__(self):
        self.root = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        parts = path.strip('/').split('/')
        node = self.root

        for i in range(len(parts)):
            part = parts[i]
            if part not in node.children:
                if i == len(parts) - 1:
                    node.children[part] = TrieNode()
                else:
                    return False  # Parent folder doesn't exist
            node = node.children[part]

        if node.val is not None:
            return False  # Path already exists

        node.val = value
        return True

    def get(self, path: str) -> int:
        parts = path.strip('/').split('/')
        node = self.root

        for part in parts:
            if part not in node.children:
                return -1
            node = node.children[part]

        return node.val if node.val is not None else -1
