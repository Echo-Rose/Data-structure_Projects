class ArrayStack :
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None]*self.capacity
        self.top = -1
    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.top == self.capacity-1
    def push(self, e):
        if not self.isFull() :
            self.top += 1
            self.array[self.top] = e
        else : pass
    def pop(self):
        if not self.isEmpty() :
            self.top -= 1
            return self.array[self.top+1]
        else : pass
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else : pass

map = [['1','1','1','1','1','1','1','1','0','0'],
       ['e','0','0','0','1','1','1','1','0','1'],
       ['1','0','1','0','1','1','1','1','0','1'],
       ['1','1','1','0','1','1','0','0','0','x'],
       ['1','1','1','0','1','1','0','1','1','1'],
       ['1','0','0','0','0','0','0','1','1','1'],
       ['1','0','1','0','1','1','1','1','1','1'],
       ['1','0','1','0','1','0','1','1','1','1'],
       ['1','1','1','0','0','0','1','1','1','1'],
       ['1','1','1','1','1','1','1','1','1','1']]
MAZE_SIZE = 10
MOVECNT = 0

def isValidPos(x, y):
    global MAZE_SIZE
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    if map[y][x] == '1' or map[y][x] == '.':
        return False
    return True
def DFS() :
    print('DFS : ')
    stack = ArrayStack(100)
    stack.push((0,1))

    while not stack.isEmpty() :
        here = stack.pop()
        print(here, end='->')
        (x,y) = here

        if(map[y][x] == 'x') :
            return True
        else :
            map[y][x] = '.'
            if isValidPos(x,y-1): stack.push((x,y-1))
            if isValidPos(x,y+1): stack.push((x,y+1))
            if isValidPos(x-1,y): stack.push((x-1,y))
            if isValidPos(x+1,y): stack.push((x+1,y))
        global MOVECNT
        MOVECNT+=1
        print('현재 스택 : ', stack)




result = DFS()
if result :
    print('--> 미로탐색 성공')
    print(str(MOVECNT)+"회 이동")
else : print('--> 미로탐색 실패')