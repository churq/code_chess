"""
all_knight_path: given start and end positions, calculate all the paths
knight: instance of knight class has jump() method, which calculate
all the next positions jumped from current position
"""
import re
from operator import itemgetter


class ChessPiece():
    def __init__(self):
        self.boardrange = 8
        self.rules = {}

    def _isvalid(self, x, y):
        inRange = lambda x: 1 <= x <= self.boardrange
        return inRange(x) and inRange(y)

    def _num_to_letter(self, num):
        return chr(num + 96)

    def _letter_to_num(self, letter):
        return ord(letter) - 96

    def jump(self, start_position, end_position):
        if self.rules:
            if self._analysis(start_position, end_position):
                result = [start_position]
                results = []
                self._paths_start_to_end(start_position, end_position, result, results)
                if results:
                    ordered_result = []
                    for r in results:
                        temp = [self._num_to_letter(i[0]) + str(i[1]) for i in r]
                        ordered_result.append(
                            ('-'.join(temp), ''.join([i[0] for i in temp]), ''.join([i[1] for i in temp])))
                    ordered_result = sorted(ordered_result, key=itemgetter(1, 2))
                    for i in ordered_result:
                        print(i[0])

                else:
                    print([])

                return results
            else:
                print("input argument is invalid, please follow the format: [a-f][0-9]")
                return None

        else:
            print("no rule is defined")
            return None

    def next_move(self, current_position):
        try:
            x = current_position[0]
            y = current_position[1]
        except:
            print("please make sure the input argument is the tuple/list of two elements (x,y)")
            return
        next_move_position = []
        for i in self.rules.values():
            if self._isvalid(x + i[0], y + i[1]):
                next_move_position.append((x + i[0], y + i[1]))

        if next_move_position:

            return next_move_position
        else:
            return None

    def _analysis(self, start_position, end_position):
        """
        check if start and end position are in the range of board
        return: True or False
        startp: e.g (1,1)
        endp: e.g (4,4)
        """
        if len(start_position) == 2 and len(end_position) == 2 and re.match(r'[a-z][0-9]', start_position) and re.match(
                r'[a-z][0-9]', end_position):
            start_position = (ord(start_position[0]) - 96, int(start_position[1]))
            end_position = (ord(end_position[0]) - 96, int(end_position[1]))

            return self._isvalid(start_position, end_position)
        else:
            return False

    def _paths_start_to_end(self, start_position, end_position, result, results):
        """
        start position:(1,1)
        end position
        result: parent node, initial value is [sp]
        results: reference of empty list which is going to store all the paths
        """
        candidatePos = self.next_move(start_position)
        if not result:
            return None

        try:
            for i in candidatePos:
                if len(result) >= 5:
                    return result[:-1]
                if i in result:
                    continue
                if i == end_position:
                    results.append(result + [i])
                    continue
                result.append(i)
                result = self._paths_start_to_end(i, end_position, result, results)
            return result[:-1]
        except:
            return None


class Knight(ChessPiece):
    def __init__(self):
        # all 8 possible positions
        super(Knight, self).__init__()
        self.rules = {
            'm1': (2, 1),
            'm2': (1, 2),
            'm3': (-1, 2),
            'm4': (-2, 1),
            'm5': (-2, -1),
            'm6': (-1, -2),
            'm7': (1, -2),
            'm8': (2, -1)
        }
