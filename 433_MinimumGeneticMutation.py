class Solution(object):
    def minMutation(self, startGene, endGene, bank):
        """
        :type startGene: str
        :type endGene: str
        :type bank: List[str]
        :rtype: int
        """
        from collections import deque

        # Convert the bank list into a set for faster lookup
        bank_set = set(bank)
        
        # If endGene is not in the bank, we can’t reach it
        if endGene not in bank_set:
            return -1

        # Possible characters for mutation
        genes = ['A', 'C', 'G', 'T']

        # BFS queue initialized with startGene and mutation count 0
        queue = deque([(startGene, 0)])

        # BFS loop
        while queue:
            gene, step = queue.popleft()

            # If we reach the target gene, return the number of mutations
            if gene == endGene:
                return step

            # Try changing each character in the gene
            for i in range(len(gene)):
                for ch in genes:
                    # Mutate one character
                    mutated = gene[:i] + ch + gene[i+1:]
                    
                    # If mutated gene is valid and in bank
                    if mutated in bank_set:
                        # Remove to prevent revisiting
                        bank_set.remove(mutated)
                        # Add to queue with one more mutation step
                        queue.append((mutated, step + 1))

        # If we can’t reach endGene, return -1
        return -1
