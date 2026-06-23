"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

ACE = "A"
FACE_CARDS = ("J", "Q", "K")
FACE_CARD_VALUE = 10
ACE_LOW_VALUE = 1
ACE_HIGH_VALUE = 11
BLACKJACK_SCORE = 21
DOUBLE_DOWN_MIN = 9
DOUBLE_DOWN_MAX = 11


def value_of_card(card):
    """Determine the scoring value of a card."""
    if card in FACE_CARDS:
        return FACE_CARD_VALUE

    if card == ACE:
        return ACE_LOW_VALUE

    return int(card)


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand."""
    value_one = value_of_card(card_one)
    value_two = value_of_card(card_two)

    if value_one > value_two:
        return card_one

    if value_one < value_two:
        return card_two

    return (card_one, card_two)


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for an upcoming ace card."""
    if ACE in (card_one, card_two):
        return ACE_LOW_VALUE

    total = value_of_card(card_one) + value_of_card(card_two)

    if total + ACE_HIGH_VALUE <= BLACKJACK_SCORE:
        return ACE_HIGH_VALUE

    return ACE_LOW_VALUE


def is_blackjack(card_one, card_two):
    """Determine if the hand is a natural blackjack."""
    return (
        card_one == ACE and value_of_card(card_two) == FACE_CARD_VALUE
    ) or (
        card_two == ACE and value_of_card(card_one) == FACE_CARD_VALUE
    )


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands."""
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet."""
    total = value_of_card(card_one) + value_of_card(card_two)

    return DOUBLE_DOWN_MIN <= total <= DOUBLE_DOWN_MAX