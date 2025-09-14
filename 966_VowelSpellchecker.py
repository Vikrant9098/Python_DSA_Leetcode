class Solution(object):
    def spellchecker(self, wordlist, queries):
        """
        :type wordlist: List[str]
        :type queries: List[str]
        :rtype: List[str]
        """

        # 1. Create a set for exact matches (case-sensitive check)
        exact_set = set(wordlist)

        # 2. Create a dictionary for case-insensitive matches
        # Key = lowercase version of the word, Value = first word from wordlist
        case_map = {}
        for word in wordlist:
            lower_word = word.lower()              # convert word to lowercase
            if lower_word not in case_map:         # only store the first occurrence
                case_map[lower_word] = word        # map lowercase word -> original word

        # 3. Create a dictionary for vowel-error matches
        # Key = word with vowels replaced by '*', Value = first word from wordlist
        vowel_map = {}
        for word in wordlist:
            masked = self.mask(word)               # create masked version of the word
            if masked not in vowel_map:            # only store the first occurrence
                vowel_map[masked] = word           # map masked word -> original word

        # 4. Create a list to store the results of queries
        result = []

        # 5. Process each query one by one
        for q in queries:
            # Case 1: If exact match exists (case-sensitive), return query itself
            if q in exact_set:
                result.append(q)
            # Case 2: If lowercase version exists in case_map, return the original word
            elif q.lower() in case_map:
                result.append(case_map[q.lower()])
            # Case 3: If vowel-masked version exists, return the mapped word
            elif self.mask(q) in vowel_map:
                result.append(vowel_map[self.mask(q)])
            # Case 4: If no match, return empty string
            else:
                result.append("")
        
        # 6. Return the final list of results
        return result

    # Helper function: Replace vowels with '*'
    def mask(self, word):
        vowels = set("aeiou")                      # define set of vowels
        masked = []                                # list to build masked word
        for c in word.lower():                     # convert word to lowercase and check each char
            if c in vowels:                        # if char is a vowel
                masked.append('*')                 # replace vowel with '*'
            else:                                  # otherwise
                masked.append(c)                   # keep consonant as is
        return "".join(masked)                     # join list into string and return
