import math
import random
cards = []
symbols = ["H", "C", "S", "D"]
for i in range(2, 15):
    for j in symbols:
        card = f"{i}{j}"
        cards.append(card)
        
print(cards)

print(len(cards))

player1 = []
player2 = []

index1 = random.randint(0, len(cards) - 1)
card1 = cards[index1]
del cards[index1]


index2 = random.randint(0, len(cards) - 1)
card2 = cards[index2]
del cards[index2]



index3 = random.randint(0, len(cards) - 1)
card3 = cards[index3]
del cards[index3]

index4 = random.randint(0, len(cards) - 1)
card4 = cards[index4]
del cards[index4]

print(len(cards))

player1.append(card1)
player1.append(card2)
player2.append(card3)
player2.append(card4)

print(player1)
print(player2)

flop = []

for i in range(3):
    index = random.randint(0, len(cards) - 1)
    flop_card = cards[index]
    del cards[index]
    flop.append(flop_card)
    
print(f"Flop: {flop}")
print(len(cards))

from itertools import combinations

combinations_possible = int(math.factorial(len(cards)) / (math.factorial(2) * math.factorial(len(cards) - 2)))


# Example list of 45 elements
elements = [cards[i] for i in range(0, len(cards))]

# Generate all pairs of elements
pairs = list(combinations(elements, 2))

# Print the total number of pairs
print(f"Total pairs: {len(pairs)}")

hand_player_1 = [pairs[0]]
hand_player_1.append(player1)
hand_player_1.append(flop)

player_1_hand = [str(item) for group in hand_player_1 for item in group]
#print(player_1_hand)

from collections import Counter

def flush(hand):
    letters = []
    for item in hand:
        letter = item[-1]
        letters.append(letter)
        
    # Count occurrences of each element
    counts = Counter(letters)

    # Check if any element appears at least 5 times
    at_least_five_equal = any(count >= 5 for count in counts.values())
    if at_least_five_equal == True:
        
        strength = 6
    else:
        strength = 0
    
    return at_least_five_equal, strength
    
    
def straight_flush(hand):
    letters = []
    numbers = []
    for item in hand:
        letter = item[-1]
        letters.append(letter)
        
    counts = Counter(letters)
        
    # Find the element that appears at least 5 times
    element_to_find = next((elem for elem, count in counts.items() if count >= 5), None)

    if element_to_find:
        # Find the indices of the element that appears at least 5 times
        indices = [i for i, item in enumerate(letters) if item == element_to_find]
        #print("Indices of the equal elements:", indices)
        for index in indices:
            card = hand[index]
            number = ''.join([char for char in card if char.isdigit()])
            numbers.append(int(number))
            
        numbers.sort()
        
        #print(numbers)
        
        # Check if the numbers are consecutive
        is_consecutive = all(numbers[i] + 1 == numbers[i+1] for i in range(len(numbers)-1))
        
        
    else:
        #print("No element appears at least 5 times.")
        status = False
        is_consecutive = False
    
    if is_consecutive == True:
        highest = max(numbers)
        strength = [9, highest]
        status = True
    else:
        strength = 0
        status = False
    
    return status, strength

def royal_flush(hand):
    letters = []
    numbers = []
    for item in hand:
        letter = item[-1]
        letters.append(letter)
        
    counts = Counter(letters)
        
    # Find the element that appears at least 5 times
    element_to_find = next((elem for elem, count in counts.items() if count >= 5), None)

    if element_to_find:
        # Find the indices of the element that appears at least 5 times
        indices = [i for i, item in enumerate(letters) if item == element_to_find]
        print("Indices of the equal elements:", indices)
        for index in indices:
            card = hand[index]
            number = ''.join([char for char in card if char.isdigit()])
            numbers.append(int(number))
            
        numbers.sort()
        is_consecutive = all(numbers[i] + 1 == numbers[i+1] for i in range(len(numbers)-1))
    else:
        #print("No element appears at least 5 times.")
        is_consecutive = False
        
        
    

    # Check if the numbers are consecutive
    
    
    if is_consecutive:
        # If the numbers are consecutive, check if the highest number is 14
        highest_number = max(numbers)
        is_highest_14 = highest_number == 14
        print(is_highest_14)  # True if the highest number is 14, False otherwise
    else:
        is_highest_14 = False  # If the numbers are not consecutive, return False
        
    if is_highest_14 == True:
        strength = 10
    else:
        strength = 0
    
    return is_highest_14, strength
          
def four_of_a_kind(hand):
    numbers = []
    for card in hand:
        number = ''.join([char for char in card if char.isdigit()])
        numbers.append(number)
    
    # Count occurrences of each element
    counts = Counter(numbers)
    #print(numbers)
    # Check if any element appears at least 4 times
    is_four_same = any(count >= 4 for count in counts.values())
    four_times_numbers = [num for num, count in counts.items() if count >= 4]
    # If there's a number that appears 4 times, remove it from the list
    if four_times_numbers:
        number_to_remove = int(four_times_numbers[0])  # Get the number that appears 4 times
        numbers = [num for num in numbers if num != number_to_remove]  # Filter out that number
    
    # Convert numbers to integers and find the highest
    numbers = list(map(int, numbers))  # Convert all numbers to integers
    if numbers:  # Ensure there are numbers left in the list
        highest = max(numbers)
    else:
        highest = None  # If the list is empty, return None
    
    if is_four_same == True:
        strength = [8, int(four_times_numbers[0]), highest]
    else:
        strength = 0
    
    return is_four_same, strength
    
    
def straight(hand):
    
    numbers = []
    
    # Extract numbers from the hand (assuming each card is in the form like '2H', '10D', '4S', etc.)
    for card in hand:
        number = int(''.join([char for char in card if char.isdigit()]))
        
        if number not in numbers:
            numbers.append(int(number))
        
    numbers.sort()
    #print(numbers)

    # Check if there are at least 5 consecutive numbers
    for i in range(len(numbers) - 4):  # We need at least 5 numbers in a row
        # Check if the next 5 numbers are consecutive
        if all(numbers[i+j] + 1 == numbers[i+j+1] for j in range(4)):
            status = True
            strength = 5
            return True, 5
        
            status = False # If we find such a sequence, return True
            strength = 0
    return False, 0
   
    
    
def three_of_a_kind(hand):
    numbers = []
    for card in hand:
        number = ''.join([char for char in card if char.isdigit()])
        numbers.append(number)
    
    # Count occurrences of each element
    counts = Counter(numbers)

    # Check if any element appears at least 4 times
    is_three_same = any(count >= 3 for count in counts.values())
    four_times_numbers = [num for num, count in counts.items() if count >= 3]
    
    

    if is_three_same == True:
        # If there's a number that appears 4 times, remove it from the list
        if four_times_numbers:
            number_to_remove = int(four_times_numbers[0])  # Get the number that appears 4 times
            numbers = [num for num in numbers if num != number_to_remove]  # Filter out that number
        
        # Convert numbers to integers and find the highest
        # Convert all numbers to integers
        numbers_int = []
        for number in numbers:
            if int(number) != number_to_remove:
                numbers_int.append(int(number))
            
        numbers_int.sort(reverse=True)
        print(numbers_int)
        if numbers_int:  # Ensure there are numbers left in the list
            
            highest = numbers_int[0]
            second_highest = numbers_int[1]
        else:
            highest = None  # If the list is empty, return None
        strength = [4, int(four_times_numbers[0]), highest, second_highest]
    else:
        strength = 0
    return is_three_same, strength
    
    
def pair(hand):
    numbers = []
    for card in hand:
        number = ''.join([char for char in card if char.isdigit()])
        numbers.append(number)
    
    # Count occurrences of each element
    counts = Counter(numbers)

    # Check if any element appears at least 4 times
    is_pair = any(count >= 2 for count in counts.values())
    four_times_numbers = [num for num, count in counts.items() if count >= 2]
    # If there's a number that appears 4 times, remove it from the list
    if four_times_numbers:
        number_to_remove = int(four_times_numbers[0])  # Get the number that appears 4 times
        numbers = [num for num in numbers if num != number_to_remove]  # Filter out that number
    
    numbers_int = []
    for number in numbers:
        if int(number) != number_to_remove:
            numbers_int.append(int(number))
          
    numbers_int.sort(reverse=True)
    print(numbers_int)
    if numbers_int:  # Ensure there are numbers left in the list
        
        highest = numbers_int[0]
        second_highest = numbers_int[1]
        third_highest = numbers_int[2]
    else:
        highest = None  # If the list is empty, return None
    
    if is_pair == True:
        
        strength = [2, int(four_times_numbers[0]), highest, second_highest, third_highest]
    else:
        strength = 0
    return is_pair, strength
    
def two_pair(hand):
    
    numbers = []
    
    # Extract numbers from the hand
    for card in hand:
        number = ''.join([char for char in card if char.isdigit()])
        numbers.append(number)
    
    # Count occurrences of each number
    counts = Counter(numbers)
    
    # Count how many numbers appear at least twice (pairs)
    pair_count = sum(1 for count in counts.values() if count >= 2)
    
    # Check if there are at least two pairs
    has_two_pairs = pair_count >= 2
    
    if has_two_pairs == True:
        strength = 3
    else:
        strength = 0
    
    return has_two_pairs, strength # True if there are two pairs, False otherwise

def full_house(hand):
    numbers = []
    
    # Extract numbers from the hand
    for card in hand:
        number = ''.join([char for char in card if char.isdigit()])
        numbers.append(number)
    
    # Count occurrences of each number
    counts = Counter(numbers)
    
    # Count how many numbers appear exactly twice (pair) and exactly three times (three-of-a-kind)
    pair_count = sum(1 for count in counts.values() if count == 2)
    three_of_a_kind_count = sum(1 for count in counts.values() if count == 3)
    
    # Check if there is at least one pair and one three-of-a-kind
    has_pair_and_three = pair_count >= 1 and three_of_a_kind_count >= 1
    
    if has_pair_and_three == True:
        strength = 7
    else:
        strength = 0
    
    return has_pair_and_three, strength  # True if there is one pair and one three-of-a-kind, False otherwise
    

hands_players = [["10C", "11C", "14D", "10C", "12D", "13D", "2C"], ["14S", "14H", "10D", "10C", "14C", "11C", "7C"]]

players_strengths = []
for hand in hands_players:

    status_2, strength_2 = pair(hand)
    status_3, strength_3 = two_pair(hand)
    status_4, strength_4 = three_of_a_kind(hand)
    status_5, strength_5 = straight(hand)
    status_6, strength_6 = flush(hand)
    status_7, strength_7 = full_house(hand)
    status_8, strength_8 = four_of_a_kind(hand)
    status_9, strength_9 = straight_flush(hand)
    status_10, strength_10 = royal_flush(hand)

    player_1_status = [status_2, status_3, status_4, status_5, status_6, status_7, status_8, status_9, status_10]
    player_1_strength = [strength_2, strength_3, strength_4, strength_5, strength_6, strength_7, strength_8, strength_9, strength_10]

    abs_strength = 0
    for i in range(9):
        
        if player_1_status[i] == True:
            abs_strength = player_1_strength[i]
            
    players_strengths.append(abs_strength)

print(players_strengths)


