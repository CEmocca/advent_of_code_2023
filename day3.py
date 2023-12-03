from utils import read_file
from collections import deque


# Optimize it by using adjacent matrix with BFS should be easier. Also it should be able to share the same code for part 2
class Day3:
    def __init__(self, input: list[str]):
        col = len(input[0])
        row = len(input)

        self.matrix: list[list[str]] = [[0 for x in range(col)] for y in range(row)]

        i = 0
        for line in input:
            j = 0
            while j < len(line):
                self.matrix[i][j] = line[j]
                j += 1
            i += 1

    def check_adjacent(self, i: int, j: int) -> bool:
        col_len = len(self.matrix[i]) 
        row_len = len(self.matrix) 

        if i - 1 >= 0 and (self.matrix[i - 1][j] != '.'):
            return True
        elif i - 1 >= 0 and j - 1 >= 0 and (self.matrix[i - 1][j - 1] != '.'):
            return True
        elif i - 1 >= 0 and j + 1 < col_len and (self.matrix[i - 1][j + 1] != '.'):
            return True
        elif j - 1 >= 0 and (self.matrix[i][j - 1] != '.' and not self.matrix[i][j - 1].isdigit()):
            return True
        elif j + 1 < col_len and (self.matrix[i][j + 1] != '.' and not self.matrix[i][j + 1].isdigit()):
            return True
        elif i + 1 < row_len and j - 1 >= 0 and (self.matrix[i + 1][j - 1] != '.'):
            return True
        elif i + 1 < row_len and j + 1 < col_len and (self.matrix[i + 1][j + 1] != '.'):
            return True
        elif i + 1 < row_len and (self.matrix[i + 1][j] != '.'):
            return True
        else:
            return False
        

    def find_adjacent(self):
        adjacent_number = []

        for i in range(len(self.matrix)):
            num = []
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j].isdigit():
                    is_adjacent = self.check_adjacent(i, j)
                    num.append((self.matrix[i][j], is_adjacent))
                    # print(f'({i}, {j}) num = {"".join(map(lambda x: x[0], num))} is_adjacent: {is_adjacent}')
                if not self.matrix[i][j].isdigit() or j == len(self.matrix[i]) - 1:
                    num_adjacent = False
                    number = ''
                    for item in num:
                        num_adjacent = num_adjacent or item[1]
                        number += item[0]
                    if num_adjacent == True:
                        adjacent_number.append(number)
                    num = []
                    continue
        return adjacent_number
    
    def solution_1(self):
        un_adjacent = self.find_adjacent()
        sum = 0
        for item in un_adjacent:
            sum += int(item)

        return sum
    
    def part_two_get_adjacent(self, i: int, j: int) -> list[tuple[int, int]]:
        col_len = len(self.matrix[i])
        row_len = len(self.matrix)

        digit_indexes = []

        if i - 1 >= 0 and self.matrix[i - 1][j].isdigit():
            digit_indexes.append((i - 1, j))
        if i - 1 >= 0 and j - 1 >= 0 and self.matrix[i - 1][j - 1].isdigit():
            digit_indexes.append((i - 1, j - 1))
        if i - 1 >= 0 and j + 1 < col_len and self.matrix[i - 1][j + 1].isdigit():
            digit_indexes.append((i - 1, j + 1))
        if j - 1 >= 0 and self.matrix[i][j - 1].isdigit():
            digit_indexes.append((i, j - 1))
        if j + 1 < col_len and self.matrix[i][j + 1].isdigit():
            digit_indexes.append((i, j + 1))
        if i + 1 < row_len and j - 1 >= 0 and self.matrix[i + 1][j - 1].isdigit():
            digit_indexes.append((i + 1, j - 1))
        if i + 1 < row_len and j + 1 < col_len and self.matrix[i + 1][j + 1].isdigit():
            digit_indexes.append((i + 1, j + 1))
        if i + 1 < row_len and self.matrix[i + 1][j].isdigit():
            digit_indexes.append((i + 1, j))
        
        return digit_indexes
        
    def part_two_get_full_number(self, adjacent_indexes: list[tuple[int, int]]) -> str:
        if len(adjacent_indexes) == 0:
            return 0
        numbers = []
        dedup_adjacents = [adjacent_indexes[0], adjacent_indexes[-1]]
        for i, j in dedup_adjacents:
            f_number = ''
            r_number = ''
            f_pointer = j
            r_pointer = j + 1
            
            while f_pointer >= 0:
                if self.matrix[i][f_pointer].isdigit():
                    f_number = self.matrix[i][f_pointer] + f_number
                    f_pointer -= 1
                else:
                    break
            
            while r_pointer < len(self.matrix[i]):
                if self.matrix[i][r_pointer].isdigit():
                    r_number += self.matrix[i][r_pointer]
                    r_pointer += 1
                else:
                    break
        
            
            numbers.append(int(f_number + r_number))
        if len(numbers) == 2 and numbers[0] != numbers[1]:
            return numbers[0] * numbers[1]
        else:
            return 0

    
    def part_two(self):
        sum = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if self.matrix[i][j] == '*':
                    adjacent_indexes = self.part_two_get_adjacent(i, j)
                    multipy = self.part_two_get_full_number(adjacent_indexes)
                    sum += multipy

        return sum




input_day3 = read_file('input_data/day_3.txt')
day3 = Day3(input_day3)

print(day3.solution_1())
print(day3.part_two())
