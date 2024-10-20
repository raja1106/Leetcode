from collections import defaultdict


class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))  # Initialize parent array
        self.rank = [0] * size  # Initialize rank array
        self.components = size  # Number of connected components
    def find(self, x):
        # return root as usual after doing path compression
        # Base case
        if x == self.parent[x]:
            return x
        # Recursive case
        root_x = self.find(self.parent[x])  # Path compression
        self.parent[x] = root_x
        return root_x
    def union(self, x, y):
        rootX = self.find(x)  # Find root of x
        rootY = self.find(y)  # Find root of y

        if rootX != rootY:
            # Union by size: Attach the smaller tree under the larger tree
            if self.size[rootX] < self.size[rootY]:
                self.parent[rootX] = rootY
                self.size[rootY] += self.size[rootX]  # Update the size of rootY
            else:
                self.parent[rootY] = rootX
                self.size[rootX] += self.size[rootY]  # Update the size of rootX
            # Decrease the number of components after a successful union
            self.components -= 1



class Solution:
    def accountsMerge(self, accountList):
        uf = UnionFind(len(accountList))  # Initialize Union-Find for each account

        email_to_index = {}  # Map email to the index of the account
        index_to_emails = defaultdict(list)  # To store emails by the root index of accounts

        # Step 1: Union accounts with the same emails
        for i, account in enumerate(accountList):
            account_name = account[0]
            emails = account[1:]

            for email in emails:
                if email in email_to_index:
                    # Union the current account with the one that contains the same email
                    uf.union(i, email_to_index[email])
                email_to_index[email] = i

        # Step 2: Group emails by the root account after unions
        for email, index in email_to_index.items():
            root = uf.find(index)
            index_to_emails[root].append(email)

        # Step 3: Build the final result
        merged_accounts = []
        for root, emails in index_to_emails.items():
            name = accountList[root][0]  # Get the name from the root account
            merged_accounts.append([name] + sorted(emails))  # Sort emails and add name

        return merged_accounts
