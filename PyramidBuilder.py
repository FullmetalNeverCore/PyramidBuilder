class Slave:
    def __init__(self,height):
        self.height = height 
        self.cube = -1 
        self.height = 35 if self.height >= 35 and self.height <= 80 else self.height
        self.stabilization = self.height + 11
        self.x1 = int(round(float(self.height)/1.5))+1
        self.y2 = 0
        self.z3 = self.height - int(round(float(self.height)/1.5))
        self.brickcount = 0 
        self.aftereye = False
    
    def buildPyramid(self):
        for x in range(0,self.height):
            self.cube = self.cube + 2
            print()
            periter = True 
            periterpttrn = False 
            for y in range(self.stabilization,x-1,-1):
                #print(y)
                #print(x+self.y2)
                    if not self.x1 == 0: 
                        if y == x+self.y2:
                            #print('here')
                            print('¥',end='')
                            self.x1 = self.x1 - 1
                            self.y2 = self.y2 + 1
                            periterpttrn = True
                        elif periterpttrn == True: 
                            if y%2==0 and self.aftereye == True: 
                                print('\\',end='')
                            elif x == 4: 
                                if y%2==0:print('\\',end='')
                                else:print('.',end='')
                            else:print('.',end='')
                        else:print(' ',end='')
                    elif not self.z3 == 0 and periter == True and not x == int(round(float(self.height)/1.5)):
                        if y == x+self.y2-2: 
                            print('\\',end='')
                            self.z3 = self.z3 - 1
                            self.y2 = self.y2 - 2
                            periter = False
                            periterpttrn = True
                        elif periterpttrn == True:
                            if y%2==0:print('\\',end='')
                            else:print('.',end='')
                        else:print(' ',end='')
                    elif periterpttrn == True:
                        if y%2==0:print('\\',end='')
                        else:print('.',end='')
                    else:print(' ',end='')
            for z in range(self.cube,-1,-1):
                if z == 0:print('¥',end='')
                elif self.cube == 7:print('/ <()> ¥',end='');break 
                elif self.cube == 9:print('/________¥',end='');self.aftereye = True;break
                elif self.cube == z:print('/',end='')
                elif self.aftereye == True:
                    if self.brickcount < 3:
                            if x%2==0 and z == self.cube-1:print('_',end='')
                            if x%2==0 and z == self.cube-(self.cube-1):print('',end='')
                            else:print('_',end='')
                            self.brickcount = self.brickcount + 1
                    elif self.brickcount == 3:
                            if x%2==0 and z == self.cube-(self.cube-1):print('',end='')
                            else:
                                if z == 0:print('¥',end='')
                                else:print('I',end='')
                            self.brickcount = 0
                else:print(' ',end='')

Slave(int(input('Input Height: '))).buildPyramid()
