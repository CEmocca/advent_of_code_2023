from utils import read_whole_file_as_string
from math import lcm

class Day8:

    def __init__(self, input: str) -> None:
        self.inputs = input.split('\n\n')

        self.instructions = self.inputs[0]

        self.paths = self.format_path(self.inputs[1])

    def format_path(self, input: str):
        paths = {}
        for line in input.split('\n'):
            path, l_r_paths = line.split(' = ')
            routes = l_r_paths.split(',')
            l_path = routes[0].replace('(', '').strip()
            r_path = routes[1].replace(')', '').strip()
            paths[path] = [l_path, r_path]

        return paths
    
    def part_1(self, start: str, target: str, instructions: str, possible_paths: dict[str, list[str]]):
        step = 0
        current = start
        len_instructions = len(instructions)
        while current != target:
            c_index = step % len_instructions
            c_instruction = instructions[c_index]

            if c_instruction == 'L':
                current = possible_paths[current][0]
            else:
                current = possible_paths[current][1]

            step += 1

        return step
    
    def part_2_f(self, start: str, instructions: str, possible_paths: dict[str, list[str]]):
        step = 0
        current = start
        len_instructions = len(instructions)
        while not current.endswith('Z'):
            c_index = step % len_instructions
            c_instruction = instructions[c_index]

            if c_instruction == 'L':
                current = possible_paths[current][0]
            else:
                current = possible_paths[current][1]

            step += 1
        return step

    def part_2(self):
        starts = []
        
        for node in self.paths.keys():
            if node.endswith('A'):
                starts.append(node)
        
        dist = []
        for start in starts:
            dist.append(self.part_2_f(start, self.instructions, self.paths))

        return lcm(*dist)


input_day8 = read_whole_file_as_string('input_data/day_8.txt')

day8 = Day8(input_day8)
# print(day8.instructions)
# print(day8.paths)
print(day8.part_1('AAA', 'ZZZ', day8.instructions, day8.paths))
print(day8.part_2())