'''
GPS Buddy Path Finding
2023-11-30
'''

def get_options(graph, pos):
  '''
  Checks if adjacent blocks to pos are open (no obstacle). 
  
  Returns list in the order [up, right, down, left], with the [x,y] location of the
  block in that direction, or -1 if there is an obstacle.
  '''
  results = []
  n = len(graph)
  
  #look around
  options = [0,0,0,0]
  if pos[0]-1 >= 0 and graph[pos[0]-1][pos[1]]: #up
    options[0] = 1
  if pos[0]+1 < n and graph[pos[0]+1][pos[1]]: #down
    options[2] = 1
  if pos[1]-1 >= 0 and graph[pos[0]][pos[1]-1]: #right
    options[3] = 1
  if pos[1]+1 < n and graph[pos[0]][pos[1]+1]: #left
    options[1] = 1

  #add options
  if options[0]:
    results.append([pos[0]-1,pos[1]])
  else:
    results.append(-1)
  if options[1]:
    results.append([pos[0],pos[1]+1])
  else:
    results.append(-1)
  if options[2]:
    results.append([pos[0]+1,pos[1]])
  else:
    results.append(-1)
  if options[3]:
    results.append([pos[0],pos[1]-1])
  else:
    results.append(-1)
  return results  

def bfs_robot(graph, start, end):
  '''
  Perform a breadth-first search on the given graph to find the shortest 
  path from the start position to the end position.
  
  Returns a list representing the moves to reach the end position 
    (0 - up, 1 - right, 2 - down, 3 - left)
  or [-1] if no path is found.
  '''
  if end == start:
    return []
    
  visited = []
  queue = [(start, [])]

  while queue:
    current, path = queue.pop(0)
    visited.append(current)
    options = get_options(graph, current)
    for next in options:
      if next != -1:
        if next == end:
          return path + [options.index(next)]
        if next not in visited:
          queue.append((next, path + [options.index(next)]))
          visited.append(next)
  return [-1]

def compact(a):
  compacted = []
  step = [a[0],1]
  for i in range(1,len(a)):
    if a[i] == step[0]:
      step[1] += 1
    else:
      compacted.append(step)
      step = [a[i],1]
  compacted.append(step)
  return compacted

def forward(t):
  pass
def turn(turnRight):
  pass
def backward(t):
  pass

grid = [
  [1,1,1,0,1,1],
  [1,1,0,1,1,1],
  [1,1,1,1,0,1],
  [0,1,0,1,0,1],
  [0,1,1,1,1,1],
  [1,1,1,0,1,1]
]
size = len(grid)


# starting position
try:
  pos = list(map(int,input("Starting coordinates: ").split(",")))
  if pos[0]<0 or pos[0]>=size or pos[1]<0 or pos[0]>=size:
    print("Out of range, starting at (0,0)")
    pos = [0,0]
except Exception:
  print("Invalid input, starting at (0,0)")
  pos = [0,0]

#main
tile = 1 #amt of time to run for one tile
running = True
while running:
  try:
    newPos = input("Destination: ")
    if newPos.strip() == "exit":
      running = False
    else:
      newPos = newPos.split(",")
      newPos = [int(newPos[0]), int(newPos[1])]
      if newPos[0]<0 or newPos[0]>=size or newPos[1]<0 or newPos[1]>=size:
        print("Coordinate not in range.")
      else:
        print("calculating path...")
        instructions = bfs_robot(grid, pos, newPos)
        instructions = compact(instructions)
        print(instructions)

        for step in instructions:
          if step[0] == 0:
            forward(tile*step[1])
          elif step[0] == 1:
            turn(True)
            forward(tile*step[1])
            turn(False)
          elif step[0] == 2:
            backward(tile*step[1])
          elif step[0] == 3:
            turn(False)
            forward(tile*step[1])
            turn(True)
          elif step[0] == -1:
            print("Unable to reach destination.")
            break
        else:
          pos = newPos
  except ValueError:
    print("Invalid input.")
  
print("Program ended.")