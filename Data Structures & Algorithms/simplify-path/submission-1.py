class Solution:
    def simplifyPath(self, path: str) -> str:
        pathStack = []
        newPath = path.split('/')
        for dest in newPath:
            if dest == "..":
                if pathStack:
                    pathStack.pop()
            elif dest != '' and dest != '.':
                pathStack.append("/"+dest)
        print(newPath)

        return "".join(pathStack) if len(pathStack)!=0 else  '/'

