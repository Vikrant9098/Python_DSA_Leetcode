class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        write = 0  # Write pointer for compressed result
        read = 0   # Read pointer for original array
        
        while read < len(chars):
            current_char = chars[read]
            count = 1
            
            # Count consecutive occurrences of current character
            while read + count < len(chars) and chars[read + count] == current_char:
                count += 1
            
            # Write the character
            chars[write] = current_char
            write += 1
            
            # If count > 1, write the count digits
            if count > 1:
                count_str = str(count)
                for digit in count_str:
                    chars[write] = digit
                    write += 1
            
            # Move read pointer to next different character
            read += count
        
        return write