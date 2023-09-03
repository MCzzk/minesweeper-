from random import randint
import time
def new_map():
    map=[]
    for x in range(11):
        map.append([]) 
        for y in range(10):
            map[x].append('- ')
    return map
    
def draw():
    print('  0 1 2 3 4 5 6 7 8 9')
    for i in range(10):
        print(i,map[i][0]+map[i][1]+map[i][2]+map[i][3]+map[i][4]+map[i][5]+map[i][6]+map[i][7]+map[i][8]+map[i][9]+'\b',i)
    print('  0 1 2 3 4 5 6 7 8 9')
def dig_mines():
    mines=[]
    while len(mines)<10:
      mine=[randint(0,9),randint(0,9)]
      if mine not in mines:
         mines.append(mine)
    return mines
def dig_mine(x, y, mines):
    if [x,y] in mines:
        map[x][y] = 'x ' 
        return
    sum_mine = 0
    for xd, yd in CO:
        new_x = x
        new_y = y
        new_x += xd
        new_y += yd
        if 0<=new_x<=9 and 0<=new_y<10:
            if [new_x, new_y] in mines:
                sum_mine += 1
    map[x][y] = str(sum_mine)+' '
    if sum_mine == 0:
        map[x][y] = '  '
        for xd, yd in CO:
            new_x = x
            new_y = y
            new_x += xd
            new_y += yd
            if 0<=new_x<=9 and 0<=new_y<level:
                if map[new_x][new_y] != '  ':
                    dig_mine(new_x, new_y, mines)

def is_lose(map, mines):
    for i, j in mines:
        if map[i][j] == 'x ':
            for x, y in mines: 
                map[y][x] = 'x ' 
            draw() 
            print('BOOM！你踩到雷了呜呜呜 T_T')
            return True
    return False
def is_win(map):
    winlist=[]
    for i in range(10):
        for j in range(10):
            if map[i][j]=='- ':
               winlist.append(1)
    if len(winlist)==10:
       duration = round(time.time() - start_time)
       print(f'哇！你赢了，真厉害，用时{duration}秒')
       return True 
while True:
      level=10
      num_mines=10
      map=new_map()
      mines=dig_mines()
      start_time = time.time()
      while True:
        CO = [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]
        draw()
        y=int(input('请输入横坐标')) 
        x=int(input('请输入纵坐标'))            
        dig_mine(x, y, mines)
        if is_lose(map, mines):
           exit()
        if is_win(map):
           exit()          

        
        
        
        