class Solution:
    def interpret(self, command: str) -> str:
        e=""
        i = len(command)-1
        while i >= 0:
            if command[i] == ')' and command[i-1] == '(':
                e = 'o' + e
                i -= 2
            elif command[i] == ')' and command[i-1] != '(':
                e= command[i-2:i] + e
                i -= 4
            else:
                e = command[i] + e
                i -= 1
        return e
        
