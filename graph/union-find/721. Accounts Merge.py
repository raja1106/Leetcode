class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.size = [1] * size
        self.components = size

    def find(self, x):
        if x == self.parent[x]:
            return x
        self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        rootX = self.find(x)
        rootY = self.find(y)

        if rootX != rootY:
            # Union by size
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]
            self.components -= 1
from collections import defaultdict

class Solution:
    def accountsMerge(self, accountList):
        uf = UnionFind(len(accountList))

        email_to_index = {}
        index_to_emails = defaultdict(list)

        # Step 1: Union accounts with the same emails
        for i, account in enumerate(accountList):
            # account example: ["John", "john@example.com", "john2@example.com"]
            for email in account[1:]:
                if email in email_to_index:
                    uf.union(i, email_to_index[email])
                email_to_index[email] = i

        # Step 2: Group emails by the root account index
        for email, index in email_to_index.items():
            root = uf.find(index)
            index_to_emails[root].append(email)

        # Step 3: Build the final merged accounts
        merged_accounts = []
        for root, emails in index_to_emails.items():
            # accountList[root][0] is the name (e.g. "John")
            merged_accounts.append([accountList[root][0]] + sorted(emails))

        return merged_accounts
