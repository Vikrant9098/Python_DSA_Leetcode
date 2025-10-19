class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # If either number is "0", the product is "0"
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)           # Lengths of num1 and num2
        pos = [0] * (m + n)                    # Array to store intermediate results

        # Loop through each digit of num1 from end to start
        for i in range(m - 1, -1, -1):
            # Loop through each digit of num2 from end to start
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))  # Multiply digits
                p1 = i + j           # Tens position
                p2 = i + j + 1       # Ones position
                sum_ = mul + pos[p2] # Add existing value in pos

                pos[p2] = sum_ % 10   # Store ones place
                pos[p1] += sum_ // 10 # Add carry to tens place

        # Build the final string, skipping leading zeros
        result = ""
        for p in pos:
            if not (len(result) == 0 and p == 0):  # Skip leading zeros
                result += str(p)

        return result  # Return the final product string
