def create_deck():
    suits = ["Hearts", "Spades", "Clubs", "Diamonds"]
    ranks = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]
    deck = []

    for suit in suits:
        deck.extend(f"{rank} of {suit}" for rank in ranks)
    return deck
