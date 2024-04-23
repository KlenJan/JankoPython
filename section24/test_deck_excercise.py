from deck_excercise import Card
from deck_excercise import Deck
import unittest
import random as r


class TestCardDeck(unittest.TestCase):
    def setUp(self):
        self.d = Deck()

    def test_deck_size(self):
        """testing initial deck size is 52"""
        self.assertEqual(self.d.count(), 52)

    def test_deal_card(self):
        self.d.deal_card()
        self.assertEqual(self.d.count(), 51)

    def test_deal_card_out_of_bounds(self):
        self.d.cards = [("Hearts", "A")]
        self.d.deal_card()
        self.assertEqual(self.d.count(), 0)
        self.assertRaises(ValueError, self.d.deal_card)

    def test_deal_hand(self):
        self.d.deal_hand(4)
        self.assertEqual(self.d.count(), 48)

    def test_deal_hand_out_of_bound(self):
        self.d.deal_hand(52)
        self.assertEqual(self.d.count(), 0)
        self.assertRaises(ValueError, self.d.deal_hand, 5)

    def test_shuffle_full_deck(self):
        """testing full deck shuffle"""
        cards_original = self.d.cards.copy()
        self.d.shuffle()
        self.assertNotEqual(cards_original, self.d.cards)

    def test_shuffle_used_deck(self):
        """testing used deck shuffle, should not be able to do it"""
        self.d.deal_card()
        self.assertEqual(self.d.count(), 51)
        cards_original = self.d.cards.copy()
        self.assertRaises(ValueError, self.d.shuffle)
        self.assertEqual(cards_original, self.d.cards)


if __name__ == '__main__':
    unittest.main()
