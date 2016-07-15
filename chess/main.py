import argparse
from chess.myLib import *


def main():
    parser = argparse.ArgumentParser(description='predict knight move path')
    parser.add_argument('--start',type = str, required = True, help='start position of knight, make sure first letter second numeric')
    parser.add_argument('--end', type =str, required = True, help = 'end position of knight, make sure first letter second numeric')

    args = parser.parse_args()

    start_position = args.start
    end_position = args.end

    knight = Knight()
    knight.jump(start_position,end_position)

if __name__ =='__main__':
    main()
    print ('*'*10)
    print ('Finished')