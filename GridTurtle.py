#2023-11-23

# (0,0) is top left corner of grid
# (size,0) is bottom left corner of grid

import turtle

def get_options(graph, pos):
  '''
  Checks if adjacent blocks to pos are open using graph. 
  
  Returns a list of length 4 with each element being either, -1 if that 
  direction is not open, or the [x,y] location of the block in that 
  direction. The list is in the order [up, right, down, left].

  graph : [ int [ ] ]
  pos : [int, int]
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

  graph : [ int [ ] ]
  start : [int, int]
  end : [int, int]
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

def draw_box(x, y, n, o):
  '''
  Draws a square with side length n and bottom-left corner at (x,y).
  Fills square gray if o is False.

  x : int
  y : int
  n : int
  o : bool
  '''
  t.hideturtle()
  t.speed(0)

  t.up()
  t.setpos(x,y)
  t.down()

  if o:
    t.fillcolor("white")
  else:
    t.fillcolor("gray")

  t.begin_fill()
  for side in range(4):
    t.forward(n)
    t.right(90)
  t.end_fill()

def up(n):
  t.setheading(90)
  t.forward(n)
def right(n):
  t.setheading(0)
  t.forward(n)
def down(n):
  t.setheading(270)
  t.forward(n)
def left(n):
  t.setheading(180)
  t.forward(n)

# canvas/grid setup
screen = turtle.Screen()
turtle.title("GPSBuddy Mock")
screen.setup(1.0, 1.0)
t = turtle.Turtle()
t.left(90)
grid_tester = [
  [1,0,1,1,0,1],
  [1,1,0,1,1,1],
  [1,0,0,1,1,1],
  [1,1,1,1,0,1],
  [1,0,1,0,1,1],
  [0,1,1,1,1,0]
]
campus = [
  [1,0,0,0,1,1,0,1,1],
  [0,1,1,1,1,1,1,1,1],
  [0,1,0,0,0,1,0,1,1],
  [1,0,1,1,0,1,1,0,0],
  [1,0,0,1,1,1,0,0,1],
  [1,0,1,1,1,1,1,0,1],
  [1,1,0,1,1,0,1,1,1],
  [1,0,1,1,1,1,0,0,1],
  [1,1,1,0,1,0,1,1,1]
]
grid = campus
spacing = 30
size = len(grid)
start = [-spacing*size/2,-spacing*size/2]
top_left = [-spacing*size/2+spacing/2,spacing*size/2-spacing/2]
for row in range(len(grid)):
  for col in range(len(grid[row])):
    x = start[1]+col*spacing
    y = start[0]+row*spacing
    draw_box(x, y, spacing, grid[size-1-row][col])

# starting position
t.up()
try:
  pos = list(map(int,input("Starting coordinates: ").split(",")))
  if pos[0]<0 or pos[0]>=size or pos[1]<0 or pos[0]>=size:
    print("Out of range, starting at (0,0)")
    pos = [0,0]
except Exception:
  print("Invalid input, starting at (0,0)")
  pos = [0,0]
t.goto(top_left[0]+pos[1]*spacing,top_left[1]-pos[0]*spacing)
t.showturtle()
t.shape("square")
t.fillcolor("green")
t.shapesize(spacing/40,spacing/40*1.2,0)
t.speed(1)

#main
running = True
while running:
  try:
    newPos = input("Destination: ")
    if newPos.strip() == "exit":
      done = True
    else:
      newPos = newPos.split(",")
      newPos = [int(newPos[0]), int(newPos[1])]
      if newPos[0]<0 or newPos[0]>=size or newPos[1]<0 or newPos[1]>=size:
        print("Coordinate not in range.")
      else:
        print("calculating path...")
        instructions = bfs_robot(grid, pos, newPos)
        for i in instructions:
          if i == 0:
            up(spacing)
          elif i == 1:
            right(spacing)
          elif i == 2:
            down(spacing)
          elif i == 3:
            left(spacing)
          elif i == -1:
            print("Unable to reach destination.")
            break
        else:
          pos = newPos
  except ValueError:
    print("Invalid input.")
  
print("Program ended.")
