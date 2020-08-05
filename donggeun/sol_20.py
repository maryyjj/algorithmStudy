class Solution:
    def isValid(self, s):
        array = list(s)
        open=['(', '{', '[']
        close=[')', '}', ']']
        stack=[]
        for x in array :
            if x in open :
               stack.append(x)
            elif x in close :
                if stack==[]:
                    return False
                cur=stack.pop()
                if x == ']':
                    if cur!='[':
                        return False
                elif x == '}':
                    if cur != '{':
                        return False
                elif x == ')':
                    if cur != '(':
                        return False
        if stack!=[]:
            return False
        return True






