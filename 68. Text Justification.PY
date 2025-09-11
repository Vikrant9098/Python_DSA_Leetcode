class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []   # Final result list of justified lines
        index = 0  # Pointer to track current word

        # Process words until all are placed in lines
        while index < len(words):
            total_chars = len(words[index])  # Count chars of first word
            last = index + 1  # Index of next word to try adding

            # Try to fit as many words as possible in current line
            while last < len(words):
                if total_chars + 1 + len(words[last]) > maxWidth:
                    break
                total_chars += 1 + len(words[last])  # Add word + space
                last += 1  # Move to next word

            line = []  # Build current line
            gaps = last - index - 1  # Number of spaces between words

            # Case 1: Last line OR only one word -> left justify
            if last == len(words) or gaps == 0:
                for i in range(index, last):
                    line.append(words[i])  # Add word
                    if i != last - 1:
                        line.append(" ")  # Add single space
                # Fill remaining spaces on right
                while len("".join(line)) < maxWidth:
                    line.append(" ")
            else:
                # Case 2: Fully justify (distribute spaces evenly)
                spaces = (maxWidth - total_chars) // gaps  # Even spaces
                extra = (maxWidth - total_chars) % gaps   # Extra spaces

                for i in range(index, last - 1):
                    line.append(words[i])  # Add word
                    line.append(" ")       # Base space
                    line.append(" " * spaces)  # Add even spaces
                    if extra > 0:
                        line.append(" ")   # Add extra space
                        extra -= 1
                line.append(words[last - 1])  # Add last word (no trailing space)

            res.append("".join(line))  # Join line into string and add to result
            index = last  # Move index to next word

        return res
