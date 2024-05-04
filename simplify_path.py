class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')
        print(path)
        stack = []
        for n in path:
            if n == "..":
                if stack:
                    stack.pop()
            elif n != "." and n != "":
                stack.append(n)
        return "/" + "/".join(stack)

        
