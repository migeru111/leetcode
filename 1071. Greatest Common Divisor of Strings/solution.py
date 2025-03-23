class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = ""
        for i in range(1,len(str1)+1):
            temp_ans = ""
            substr1 = str1[0:i]
            if len(str1) % len(substr1) != 0:
                continue

            for j in range(len(str1) // len(substr1)):
                temp_ans = temp_ans + substr1

            if temp_ans != str1:
                continue

            temp_ans = ""
            if len(str2) % len(substr1) != 0:
                continue
            for j in range(len(str2) // len(substr1)):
                temp_ans = temp_ans + substr1
            if temp_ans != str2:
                continue

            ans = substr1
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.gcdOfStrings(str1="abcabc", str2="abc"))
    print(sol.gcdOfStrings(str1="abc", str2="abcabc"))
    
