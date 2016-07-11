import argparse
import re
from operator import itemgetter
from myLib import *

def run(sp,ep):
    if analysis(sp,ep):
        k = knight()
        result = [sp]
        results = []
        all_knight_path(k, sp, ep, result, results)
        if results:
            ordered_result = []
            for r in results:
                temp = [chr(i[0] + 96) + str(i[1]) for i in r]
                ordered_result.append(('-'.join(temp),''.join([i[0] for i in temp]),''.join([i[1] for i in temp])))
            ordered_result = sorted(ordered_result,key = itemgetter(1,2))
            for i in ordered_result:
                print (i[0])

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