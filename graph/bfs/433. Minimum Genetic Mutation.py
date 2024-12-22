
from typing import List
import collections

class Solution_Same_template:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Edge case: no mutations needed
        if startGene == endGene:
            return 0

        # Use a set for quick lookup
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        # BFS queue: (current gene, number of mutations so far)
        queue = collections.deque([(startGene, 0)])

        # BFS traversal
        while queue:
            current_gene, mutations = queue.popleft()

            # Try all single-character mutations
            for i in range(len(current_gene)):
                for ch in 'ACGT':
                    # Generate new gene by mutating one character
                    new_gene = current_gene[:i] + ch + current_gene[i + 1:]

                    # Check if it's the target gene
                    if new_gene == endGene:
                        return mutations + 1

                    # Check if it's in the bank and valid
                    if new_gene in bank_set:
                        bank_set.remove(new_gene)  # Mark as visited
                        queue.append((new_gene, mutations + 1))

        # If no valid mutation sequence leads to the end gene
        return -1


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        if endGene not in bank_set:
            return -1

        # Edge case: if the start gene is the same as the end gene
        if startGene == endGene:
            return 0

        queue = deque([(startGene, 0)])  # (current_gene, mutations)

        while queue:
            current_gene, mutations = queue.popleft()

            if current_gene == endGene:
                return mutations

            for i in range(len(current_gene)):
                # Only change the i-th character
                for ch in 'ACGT':
                    if current_gene[i] != ch:  # Avoid changing to the same character
                        new_gene = current_gene[:i] + ch + current_gene[i + 1:]
                        if new_gene in bank_set:
                            bank_set.remove(new_gene)  # Prevent revisiting this gene
                            queue.append((new_gene, mutations + 1))

        return -1  # If no valid mutation path was found
