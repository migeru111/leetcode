class Solution:
    def mergeAlternately(self,word1:str,word2:str)-> str:
        word1_len = len(word1)
        word2_len = len(word2)
        output=""
        if word1_len <= word2_len:
            cmn_len = word1_len
            longer = word2
            longer_len = word2_len
        else:
            cmn_len = word2_len
            longer = word1
            longer_len = word1_len

        for i in range(0,cmn_len):
            output = output+word1[i]
            output = output+word2[i]

        if cmn_len == longer_len:
            return output

        for i in range(cmn_len,longer_len):
            output = output+longer[i]
        return output
    

if __name__ == '__main__':
    sol = Solution()
    print(sol.mergeAlternately("abc","def"))