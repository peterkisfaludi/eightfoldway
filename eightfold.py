def print_board(board):
    for r in board:
        rowstr=''
        for c in r:
            ch=c
            if ch is None: ch='?'
            rowstr+=str(ch)+' '
        print(rowstr)


class Piece:
    def __init__(self, h, w, idx):
        self.h=h
        self.w=w
        self.idx=idx
        self.rot=False
        self.used=False
        self.origin=[None,None]
    def __str__(self):
        return str(self.h)+'x'+str(self.w)+' rot:'+str(self.rot)+' usd:'+str(self.used)
        
class Solution:
    def __init__(self):
        self.R=8
        self.C=8
    def scan(self):
        for r in range(self.R):
            for c in range(self.C):
                if self.board[r][c] is None:
                    return r,c
        return None,None
    def place(self,r,c,pc):
        #print('place',r,c,pc)
        h=pc.h
        w=pc.w
        if pc.rot:
            h=pc.w
            w=pc.h
        for y in range(r,r+h):
            if y==self.R: return False
            for x in range(c,c+w):
                if x==self.C: return False
                if self.board[y][x] is not None:
                    return False
        return True
    def kill(self,pc):
        pc.used=False
        h=pc.h
        w=pc.w
        if pc.rot:
            h=pc.w
            w=pc.h
        r=pc.origin[0]
        c=pc.origin[1]
        for y in range(r,r+h):
            for x in range(c,c+w):
                self.board[y][x]=None
        pc.origin=[None,None]
    def fill(self,r,c,pc):
        pc.used=True
        #print('fill',r,c,pc)
        pc.origin=[r,c]
        h=pc.h
        w=pc.w
        if pc.rot:
            h=pc.w
            w=pc.h
        for y in range(r,r+h):
            for x in range(c,c+w):
                self.board[y][x]=pc.idx
    def whos_next(self, pc):
        #print('whos_next of ',pc,'?')
        if pc is None:
            return self.pieces[0]
        if not pc.used:
            if not pc.rot:
                self.pieces[pc.idx].rot=True
                return self.pieces[pc.idx]
            else:
                self.pieces[pc.idx].rot=False
        if pc.idx==len(self.pieces)-1: return None
        return self.pieces[pc.idx+1]
        
    def place_obstacles(self,a,b,c):
        #1x1
        self.board[a[0]][a[1]]='X'
        #1x2
        self.board[b[0]][b[1]]='Y'
        if b[2]==False:
            self.board[b[0]][b[1]+1]='Y'
        else:
            self.board[b[0]+1][b[1]]='Y'
        
        self.board[c[0]][c[1]]='Z'
        if c[2]==False:
            self.board[c[0]][c[1]+1]='Z'
            self.board[c[0]][c[1]+2]='Z'
        else:
            self.board[c[0]+1][c[1]]='Z'
            self.board[c[0]+2][c[1]]='Z'
        
    def solve(self,a,b=None,c=None):
        self.board=[[None]*self.C for _ in range(self.R)]
        self.pieces=[Piece(1,4,0),Piece(1,5,1),Piece(2,2,2),Piece(2,3,3),Piece(2,4,4),Piece(2,5,5),Piece(3,3,6),Piece(3,4,7)]
        print('8 fold way solver')
        self.place_obstacles(a,b,c)
        print('original board:')
        print_board(self.board)

        placement=[]
        pc=None
        while True:
            r,c = self.scan()
            if r is None: return self.board, placement #win!
            while True:
                pc = self.whos_next(pc)
                #print('picked',pc)
                if pc is None: 
                    #print('backtrack...')
                    if len(placement)==0: return None, None #lose :(
                    pc=placement[-1]
                    self.kill(placement.pop())
                    #print(self.board)
                    break
                if pc.used: continue
                if self.place(r,c,pc):
                    placement.append(pc)
                    self.fill(r,c,pc)
                    pc=None
                    #print(self.board)
                    break
        
sol=Solution()
riddles=[
    [[5,5,False],[0,4,True],[3,2,False]],
    [[2,2,False],[6,4,True],[0,0,False]],
    [[5,1,False],[3,6,False],[5,4,True]],#M53
    [[5,3,False],[5,4,False],[1,2,True]],#M56
    [[0,0,False],[0,3,False],[4,1,False]],#M58
]

for riddle in riddles:
    board, placement = sol.solve(riddle[0],riddle[1],riddle[2])
    if board is not None:
        print('--Solved!--')
        print_board(board)
    else:
        print('no solution :(')
    
    
    
    
    
