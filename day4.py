from utils import read_file

class Day4:

    def __init__(self, input: list[str]):
        self.input = input
        self.formatted_data = self.format_data(input)

    def format_data(self, inputs: list[str]):
        formatted_data = []
        for input in inputs:
            game_cards =  input.split(':')[1].split('|')
            winning_cards = set(game_cards[0].strip().split())
            my_cards = set(game_cards[1].strip().split())
            formatted_data.append([1, winning_cards, my_cards])

        return formatted_data

    # def part_1(self, card) -> tuple[int, int]:
    #     count, winning_cards, my_cards = card
    #     my_winning_cards = winning_cards.intersection(my_cards)

    #     number_of_winning_cards = len(my_winning_cards)

    #     if number_of_winning_cards == 0:
    #         return (0, 0)
    #     if number_of_winning_cards == 1:
    #         return (1, 1)
    #     else:
    #         power = number_of_winning_cards - 1
    #         return (2 ** power, number_of_winning_cards)

    def solution(self) -> int:
        
        sum = 0
        for index, card in enumerate(self.formatted_data):
            count, winning_cards, my_cards = card

            my_winning_cards = winning_cards.intersection(my_cards)
            
            number_of_winning_cards = len(my_winning_cards)

            if number_of_winning_cards == 0:
                sum += 0
            elif number_of_winning_cards == 1:
                sum += 1
            else:
                sum += 2 ** (number_of_winning_cards - 1)

            # add winning copy to the next n card
            for i in range(index + 1, index + 1 + number_of_winning_cards):
                self.formatted_data[i][0] += count

        return (sum, self.count_cards())
    
    def count_cards(self):
        count = 0
        for card in self.formatted_data:
            count += card[0]
        return count
    

input_str = read_file('input_data/day_4.txt')
day4 = Day4(input_str)

# part 1 answer: 20117
print(day4.solution())
# for a in day4.formatted_data:
#     print(a)
