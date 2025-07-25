class Solution:
    def maxSum(self, nums):
        # Step 1: संपूर्ण लिस्टमधून जास्तीत जास्त (maximum) संख्या शोधा
        mx = max(nums)

        # Step 2: जर सगळ्या संख्या negative किंवा zero असतील, तर फक्त तीच संख्या परत करा
        if mx <= 0:
            return mx

        # Step 3: वापरलेल्या संख्यांवर लक्ष ठेवण्यासाठी 201 साईजचा boolean array वापरा
        # कारण संख्या -100 ते 100 पर्यंत असू शकतात, म्हणून index shift करतो (x + 100)
        used = [False] * 201

        # Step 4: अंतिम उत्तरासाठी answer चा सुरुवातीचा value 0 ठेवा
        ans = 0

        # Step 5: प्रत्येक संख्येसाठी loop चालवा
        for x in nums:
            # जर संख्या negative असेल किंवा आधीच वापरलेली असेल, तर continue करा
            if x < 0 or used[x + 100]:
                continue

            # संख्या answer मध्ये add करा
            ans += x

            # संख्या used म्हणून mark करा
            used[x + 100] = True

        # Step 6: उत्तर परत करा
        return ans
