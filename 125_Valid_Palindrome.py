class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower=str.ascii_lowercase
        lower_set=set(lower)
        upper=str.ascii_uppercase
        upper_set=set(upper)

        lower_to_upper={}
        formatted=[]
        
        for index in range(lower):
            lower_to_upper[lower[index]]=upper[index]

        for char in s:
            if char in lower_set:
                formatted.append(lower_to_upper[char])
            elif char in upper_set:
                formatted.append(char)
            else:
                continue
        
        if formatted == formatted[::-1]:
            return True
        else:
            return False