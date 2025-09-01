import heapq

class Solution(object):
    def maxAverageRatio(self, classes, extraStudents):
        """
        :type classes: List[List[int]]
        :type extraStudents: int
        :rtype: float
        """
        # Function to calculate the gain of adding one student
        def gain(passi, totali):
            return (float(passi + 1) / (totali + 1)) - (float(passi) / totali)
        
        # Create a max heap (store negative gain to use min-heap as max-heap)
        heap = []
        for passi, totali in classes:
            heapq.heappush(heap, (-gain(passi, totali), passi, totali))  # push (negative gain, pass, total)
        
        # Assign extra students one by one
        while extraStudents > 0:
            g, passi, totali = heapq.heappop(heap)  # pop class with max gain
            passi += 1   # add one student to pass
            totali += 1  # increase total students
            heapq.heappush(heap, (-gain(passi, totali), passi, totali))  # push updated class back
            extraStudents -= 1  # reduce count
        
        # Calculate the final average pass ratio
        total_ratio = 0.0
        while heap:
            _, passi, totali = heapq.heappop(heap)  # take each class
            total_ratio += float(passi) / totali   # add its pass ratio
        
        return total_ratio / len(classes)  # divide by number of classes
