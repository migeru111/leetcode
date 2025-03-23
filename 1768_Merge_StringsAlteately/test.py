import unittest
import solution

class TestMergeString(unittest.TestCase):
    def test_same_len(self):
        word1 = "abc"
        word2 = "def"
        sol = solution.Solution()
        assert sol.mergeAlternately(word1,word2)=="adbecf"
    def test_diff_len(self):
        word1 = "abc"
        word2 = "defgh"
        sol = solution.Solution()
        assert sol.mergeAlternately(word1=word1,word2=word2)=="adbecfgh"

if __name__ == '__main__':
    unittest.main()