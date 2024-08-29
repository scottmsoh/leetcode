

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = [[False]*len(image[0]) for _ in range(len(image))]
        BFS(image, visited, (sr,sc), color)
        return image

from collections import deque

def BFS(graph, visited, start, color):
    queue = deque([start])
    # visited = [([False] * len(graph[0])) for _ in len(graph)]
    m,n = len(graph), len(graph[0])
    start_color = graph[start[0]][start[1]]
    graph[start[0]][start[1]] = color
    visited[start[0]][start[1]] = True
    dx, dy = [-1,0,0,1], [0,-1,1,0]
    
    while queue:
        v = queue.popleft()
        for i in range(4):
            nx,ny = v[0]+dx[i], v[1]+dy[i]
            if 0<=nx<len(graph) and 0<=ny<len(graph[0]):
                if not visited[nx][ny] and graph[nx][ny] == start_color:
                    visited[nx][ny] = True
                    graph[nx][ny] = color
                    queue.append((nx,ny))
