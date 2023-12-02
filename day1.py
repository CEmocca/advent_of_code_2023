import re

from utils import read_file

class Day1:

    def __init__(self) -> None:
        self.replace_dict = {
            'one': '1',
            'two': '2',
            'three': '3',
            'four': '4',
            'five': '5',
            'six': '6',
            'seven': '7',
            'eight': '8',
            'nine': '9',
            'eno': '1',
            'owt': '2',
            'eerht': '3',
            'ruof': '4',
            'evif': '5',
            'xis': '6',
            'neves': '7',
            'thgie': '8',
            'enin': '9',
        }
        pass

    def find_two_digits(self, input: str) -> int:
        i = 0
        j = len(input) - 1

        digit1 = None
        digit2 = None

        while i < len(input):
            if digit1 is None and input[i].isdigit():
                digit1 = input[i]
            
            if digit2 is None and input[j].isdigit():
                digit2 = input[j]

            if digit1 and digit2:
                break

            i += 1
            j -= 1

        if digit1 and digit2:
            return int(f"{digit1}{digit2}")
        elif digit1 is None and digit2:
            return int(f"{digit2}{digit2}")
        else:
            return int(f"{digit1}{digit1}")
        
    def replace_string(self, input: str) -> str:
        replaced_input = re.sub(r'(one|two|three|four|five|six|seven|eight|nine)', lambda m: f'{self.replace_dict[m.group(0)]}{m.group(0)}', input, 1)

        reversed_input = replaced_input[::-1]

        replaced_input = re.sub(r'(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)', lambda m: f'{self.replace_dict[m.group(0)]}{m.group(0)}', reversed_input, 1)

        replaced_input = replaced_input[::-1]

        return replaced_input
        
    def calibrated_value(self, lines: list[str]) -> int: 
        sum = 0
        for line in lines:
            replaced = self.replace_string(line)
            val = self.find_two_digits(replaced)
            sum += val

        return sum
    

day1 = Day1()

inputs = read_file('input_data/day_1.txt')
print(day1.calibrated_value(inputs))