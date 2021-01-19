import os
import numpy as np
from collections import deque

from PIL import Image


# np.set_printoptions(threshold=sys.maxsize)
maze = np.zeros((200, 200))
S = []
F = []
with open("3.txt", "r") as f:
    while True:
        strand = f.readline().split()
        if strand:
            xy = strand[0].split(",")
            x = int(xy[0])
            y = int(xy[1])

            try:
                path = strand[1].split(",")
                for d in path:
                    maze[x][y] = 1
                    if d == "U":
                        y -= 1
                    elif d == "D":
                        y += 1
                    elif d == "L":
                        x -= 1
                    elif d == "R":
                        x += 1
                    elif d == "S":
                        S.append((x,y))
                        # break
                    elif d == "F":
                        F.append((x,y))
                        # break
                    # maze[x][y] = 0
            except:
                maze[x][y] = 1
                continue

        else:
            break
# maze = (maze * 255).astype(np.uint8)
# im = Image.fromarray(maze, mode="P")
# im.show()


row = [(-1,"L"),(0,"U"),(0,"D"),(1,"R")]
col = [0, -1, 1, 0]

def isValid(mat, visited, row, col):
    return (row >= 0) and (row < 200) and (col >= 0) and (col < 200) \
           and mat[row][col] == 1 and not visited[row][col]
 
 
# Find Shortest Possible Route in a matrix mat from source
# cell (i, j) to destination cell (x, y)
def BFS(mat, i, j, x, y):
    route = ""
    # construct a matrix to keep track of visited cells
    visited = [[False for x in range(200)] for y in range(200)]
 
    # create an empty queue
    q = deque()
 
    # mark source cell as visited and enqueue the source node
    visited[i][j] = True
    
 
    # (i, j, dist) represents matrix cell coordinates and its
    # minimum distance from the source
    q.append((i, j, 0, route))
 
    # stores length of longest path from source to destination
    min_dist = float('inf')
 
    # loop till queue is empty
    while q:
 
        # pop front node from queue and process it
        (i, j, dist, route) = q.popleft()
 
        # (i, j) represents current cell and dist stores its
        # minimum distance from the source
 
        # if destination is found, update min_dist and stop
        if i == x and j == y:
            min_dist = dist
            break
 
        # check for all 4 possible movements from current cell
        # and enqueue each valid movement
        for k in range(4):
            # check if it is possible to go to position
            # (i + row[k], j + col[k]) from current position
            if isValid(mat, visited, i + row[k][0], j + col[k]):
                # mark next cell as visited and enqueue it
                visited[i + row[k][0]][j + col[k]] = True
                q.append((i + row[k][0], j + col[k], dist + 1, route + row[k][1]))
 
    if min_dist != float('inf'):
        print("The shortest path from source to destination has length", min_dist)
        print(route)
    else:
        print("Destination can't be reached from given source")

for s in S:
    for f in F:
        BFS(maze, s[0], s[1], f[0], f[1])