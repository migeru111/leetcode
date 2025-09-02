import pytest
import sol

def test_sol():
    solution=sol.Solution()
    test_case1=[[1,2],[2,3],[3,4],[1,3]]
    ans1=1
    test_case2=[[1,2],[1,2],[1,2]]
    ans2=2
    test_case3=[[1,2],[2,3]]
    ans3=0

    assert(solution.eraseOverlapIntervals(test_case1)==ans1)
    assert(solution.eraseOverlapIntervals(test_case2)==ans2)
    assert(solution.eraseOverlapIntervals(test_case3)==ans3)
    