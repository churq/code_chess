"""
all_knight_path: given start and end positions, calculate all the paths
knight: instance of knight class has jump() method, which calculate
all the next positions jumped from current position
"""
class knight():
    def __init__(self):
        # all 8 possible positions
        self.rules = {'m1':(2,1),'m2':(1,2),'m3':(-1,2),'m4':(-2,1),'m5':(-2,-1),'m6':(-1,-2),'m7':(1,-2),'m8':(2,-1)}
        self.range = [8,8]

    def _isvalid(self,x,y):
        if (x>=1 and x<= self.range[0]) and (y>=1 and y <= self.range[1]):
            return True
        else:
            return False
    def _map(self,n):
        return chr(n+96)

    def jump(self,position):
        try:
            x = position[0]
            y = position[1]
        except:
            print ("please make sure the input argument is the tuple/list of two elements (x,y)")
            return
        all_position = []
        for i in self.rules.values():
            if self._isvalid(x+i[0],y+i[1]):
                all_position.append((x+i[0],y+i[1]))

        if all_position:
            #end_position = '-'.join(['{}{}'.format(self._map(p[0]),str(p[1])) for p in all_position ])
            #end_position = ['{}{}'.format(self._map(p[0]),str(p[1])) for p in all_position ]
            return all_position
        else:
            return None


def analysis(startp,endp):
    """
    check if start and end position are in the range of board
    return: True or False
    startp: e.g (1,1)
    endp: e.g (4,4)
    """

    if not (startp[0] in [1,2,3,4,5,6,7,8] and startp[1] in [1,2,3,4,5,6,7,8] and endp[0] in [1,2,3,4,5,6,7,8] and endp[1] in [1,2,3,4,5,6,7,8]):

        return False
    else:
        return True


def all_knight_path(k,sp,ep,result,results):
        """
        k:knight object
        sp: start position
        ep: end position
        result: parent node, initial value is [sp]
        results: reference of empty list which is going to store all the paths
        """
        candidatePos = k.jump(sp)
        if not result:
            return None

        try:
            for i in candidatePos:
                if len(result)>=5:
                    return result[:-1]
                if i in result:
                    continue
                if i ==ep:
                    results.append(result+[i])
                    continue
                result.append(i)
                result = all_knight_path(k,i,ep,result,results)
            return result[:-1]
        except:
            return None

