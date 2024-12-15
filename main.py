from game import GoldRush


def play_game():
    print("Welcome to Gold Rush!")
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))

    game = GoldRush(rows, cols)
    game.load_board()
    game.print()

    while not game.winner:
        player = "player1"
        direction = input(f"{player}, enter your move (up, down, left, right): ").strip().lower()
        game.move_player(player, direction)
        game.print()
        if game.check_if_player_has_won(player):
            print(f"{player} wins!")
            break
        if game.check_if_game_is_tied():
            print("the game is tied!")
            break
        
        player = "player2"
        direction = input(f"{player}, enter your move (up, down, left, right): ").strip().lower()
        game.move_player(player, direction)
        game.print()
        if game.check_if_player_has_won(player):
            print(f"{player} wins!")
            break
        if game.check_if_game_is_tied():
            print("the game is tied!")
            break
        

if __name__ == "__main__":
    play_game()