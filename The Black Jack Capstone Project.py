# the deck is unlimited in size.
# the are no jokers.
# the jack/queen /king all count as 10
# use the following list as the deck of cards
# creat a deal_card() function that uses the List below to *return*  random card.
import random
def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
# the cards in the list have equal probabilty of being drawn
# deal the user and computer 2 cards each using_deal()
def calculate_score(cards):
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    while not is_game_over:
#call calculate_score(). If the computer or the user has a blackjack (0) or ifbthe users score is over 21, then the game ends
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    print(f" Your cards: {user_cards}, current score: {user_score}")
    print(f" Computer first card: {computer_cards[0]}")


    if user_score == 0 or computer_score == 0 or user_score > 21:
        is_game_over = True
    else:
        user_should_deal = input("type 'y' to get another card, type 'n' to pass")
        if user_should_deal == "y":
           user_cards.append(deal_card())
        else:
            is_game_over = True

# create a function called calculate_score()  that takes the lists of cards and returns a score
# look up the sum() function to help you do this
# check for a blackjack(a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0
# inside calculate_score() check for an 11(ace). If the score is already over 21,remove the 11 and replace it with a 1. check append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

# call calculate_score(). If the computer or the user has a blackjack (0) or ifbthe users score is over 21, then the game ends


