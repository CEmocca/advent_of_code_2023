from utils import read_file
from functools import reduce

class Day6:

    def __init__(self, input: list[str]) -> None:
        self.formatted_data = self.format_data(input)

        self.part_2_data = [list(reduce(lambda x, y: [int(f'{x[0]}{y[0]}'), int(f'{x[1]}{y[1]}')], self.formatted_data))]


    def format_data(self, inputs: list[str]) -> list[list[int]]:
        formatted_data = []
        
        for input in inputs:
            stripped = input.split(':')[-1].strip().split()
        
            for i, v in enumerate(stripped):
                if len(formatted_data) <= i:
                    formatted_data.append([int(v)])
                else:
                    formatted_data[i].append(int(v))

        return formatted_data
    
    # should be able to do binary search to find min and max hold that beat the records before doing this solution
    def solution(self, inputs) -> str:
        win_ways = []
        for race in inputs:
            number_of_win = 0
            # skip first and last
            hold = 1
            while hold < race[0]:
                time_left = race[0] - hold
                distance = hold * time_left

                if distance > race[1]:
                    number_of_win += 1
                hold += 1
            win_ways.append(number_of_win)
        return reduce(lambda x, y: x * y, win_ways)

    

input_str = read_file('input_data/day_6.txt')

day6 = Day6(input_str)

print(day6.solution(day6.formatted_data))
print(day6.solution(day6.part_2_data))