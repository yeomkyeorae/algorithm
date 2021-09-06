class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:        
        d = {}
        for p in prerequisites:
            if p[1] in d.keys():
                d[p[1]].append(p[0])
            else:
                d[p[1]] = [p[0]]
        
        visited = [0] * numCourses
        traced = [0] * numCourses
        
        def dfs(key):
            if traced[key]:
                return False
            
            if visited[key]:
                return True
                        
            if key in d.keys():
                traced[key] = 1
                for candidate in d[key]:
                    if not dfs(candidate):
                        return False
                traced[key] = 0
                visited[key] = 1
            
            return True
                
                
        for k in d.keys():
            if not dfs(k):
                return False

        return True
        