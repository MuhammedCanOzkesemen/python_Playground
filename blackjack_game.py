import random

def deal_card():
    cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
    return random.choice(cards)

def calculate_score(hand):
    score = sum(hand)

    if score == 21 and len(hand) == 2:
        return 0

    if 11 in hand and score > 21:
        hand.remove(11)
        hand.append(1)

    return score

def compare(player, dealer):
    if player > 21:
        return "You lose"
    if dealer > 21:
        return "You win"
    if player == dealer:
        return "Draw"
    if player == 0:
        return "Blackjack! You win"
    if dealer == 0:
        return "Dealer Blackjack! You lose"
    if player > dealer:
        return "You win"
    return "You lose"

def game():
    print("BLACKJACK GAME")

    player_hand = [deal_card(), deal_card()]
    dealer_hand = [deal_card(), deal_card()]

    game_over = False

    while not game_over:
        player_score = calculate_score(player_hand)
        dealer_score = calculate_score(dealer_hand)

        print(f"Your hand: {player_hand}, score: {player_score}")
        print(f"Dealer first card: {dealer_hand[0]}")

        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True
        else:
            choice = input("Type 'y' to draw another card, 'n' to pass: ")
            if choice == "y":
                player_hand.append(deal_card())
            else:
                game_over = True

    while dealer_score != 0 and dealer_score < 17:
        dealer_hand.append(deal_card())
        dealer_score = calculate_score(dealer_hand)

    print(f"\nFinal hands:")
    print(f"Your hand: {player_hand}, score: {player_score}")
    print(f"Dealer hand: {dealer_hand}, score: {dealer_score}")

    print(compare(player_score, dealer_score))

if __name__ == "__main__":
    game()