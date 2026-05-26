class Solution {
    public int numberOfSpecialChars(String word) {
        int lower = 0;
        int upper = 0;

        for (char ch : word.toCharArray()) {

            // Check if character is lowercase
            if (Character.isLowerCase(ch)) {
                lower |= (1 << (ch - 'a'));
            }
            // Otherwise it is uppercase
            else {
                upper |= (1 << (ch - 'A'));
            }
        }

        // Find common characters present in both lowercase and uppercase
        int common = lower & upper;

        // Count number of set bits
        return Integer.bitCount(common);
    }
}