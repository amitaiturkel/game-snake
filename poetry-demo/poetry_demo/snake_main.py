import argparse
import game_utils
from snake_game import SnakeGame
from game_display import GameDisplay
from constants import MOVES
from helper import make_something_move

def main_loop(gd: GameDisplay, args: argparse.Namespace) -> None:
    # INIT OBJECTS
    game = SnakeGame(args)
    gd.show_score(game.score)
    # DRAW BOARD
    game.draw_board(gd)
    # ROUND 0
    prev_move = "Up"
    game.update_objects("Up")
    game.draw_board(gd)
    game.end_round()
    gd.end_round()


    while not game.is_over():
        gd.show_score(game.score)
        # CHECK KEY CLICKS
        key_clicked = gd.get_key_clicked()
        game.read_key(key_clicked)
        # UPDATE OBJECTS
        if not key_clicked or make_something_move(MOVES[key_clicked], MOVES[prev_move]) == (0, 0):
            key_clicked = prev_move
        game.update_objects(key_clicked)
        prev_move = key_clicked if key_clicked else prev_move
        # DRAW BOARD
        game.draw_board(gd)
        # WAIT FOR NEXT ROUND:
        game.end_round()
        gd.end_round()


