'''
first appro
2

121
22

11211
1212
2121
1221
222
'''
'''
second appro
https://leetcode.com/problems/generate-parentheses/discuss/154154/22-generate-parentheses-solution-in-c-java-python 참
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
'''

# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        sList = []
        s = ''
        start = 0
        end = 0
        self.backtrace(sList, s, start, end, n)
        return sList
    
    def backtrace(self, sList, s, start, end, n):
        if(len(s) == n * 2):
            sList.append(s)
            return
        # (((, (()(), (()), ()(()), ()()() 
        if start < n:
            self.backtrace(sList, s+"(", start+1, end, n)
        if end < start:
            self.backtrace(sList, s+")", start, end+1, n)
