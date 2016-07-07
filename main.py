import argparse
import re

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
        # position is knight current position,tuple
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

    if not (startp[0] in [1,2,3,4,5,6,7,8] and startp[1] in [1,2,3,4,5,6,7,8] and endp[0] in [1,2,3,4,5,6,7,8] and endp[1] in [1,2,3,4,5,6,7,8]):

        return False
    else:
        return True


def all_knight_path(k,sp,ep,result,results):
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


def run(sp,ep):
    if analysis(sp,ep):
        k = knight()
        result = [sp]
        results = []
        all_knight_path(k, sp, ep, result, results)
        if results:
            for r in results:
                temp = [chr(i[0] + 96) + str(i[1]) for i in r]
                print('-'.join(temp))
        else:
            print ([])
    else:
        print('illegal position, please make sure both values are in the range of 1 and 8')
        return


def main():
    parser = argparse.ArgumentParser(description='predict knight path')
    parser.add_argument('--start',type = str, required = True, help='start position of knight, make sure first letter second numeric')
    parser.add_argument('--end', type =str, required = True, help = 'end position of knight, make sure first letter second numeric')
    args = parser.parse_args()
    start_position = args.start
    end_position = args.end
    if len(start_position)==2 and len(end_position) ==2 and re.match(r'[a-z][0-9]',start_position) and re.match(r'[a-z][0-9]',start_position):
        s = (ord(start_position[0])-96,int(start_position[1]))
        e = (ord(end_position[0])-96,int(end_position[1]))
        run(s,e)
    else:
        print ('input format is not correct, please follows the format:[a-z][0-9]')

if __name__ =='__main__':
    main()
    print ('*'*10)
    print ('Finished')