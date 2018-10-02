#!/usr/bin/env python3

import random

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""

moves = ['rock', 'paper', 'scissors']

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        pass


class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)

    def learn(self, my_move, their_move):
        pass


class HumanPlayer(Player):
    def move(self):
        invalid_move = True

        while invalid_move:
            throw_choice = input("What would you like to throw? Choose from: 'rock', 'paper', or 'scissors'")
            if throw_choice not in moves:
                invalid_move = True
            else:
                invalid_move = False
                return throw_choice

    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.p1_score = 0
        self.p2_score = 0

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()

        print(f"Current Score: Player 1: {self.p1_score} Player 2: {self.p2_score}")
        
        print(f"Player 1: {move1}  Player 2: {move2}")
        
        if move1 == move2:
            print("It's a TIE!")
        elif beats(move1, move2):
            print("Player 1 won this round!")
            self.p1_score += 1
        elif beats(move2, move1):
            print("Player 2 won this round!")
            self.p2_score += 1
        
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")

        for round in range(3):
            print(f"Round {round + 1}:")
            self.play_round()
        
        print("Game over!")
        print(f"Final Score: Player 1: {self.p1_score}  Player 2: {self.p2_score}")


if __name__ == '__main__':
    game = Game(HumanPlayer(), RandomPlayer())
    game.play_game()
