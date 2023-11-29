# ● Задача
# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.


class GameBoard:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # используем одномерный список для удобства

    def display_board(self):
        for i in range(0, 9, 3):
            print(f"{self.board[i]} | {self.board[i+1]} | {self.board[i+2]}")
            if i < 6:
                print("--+---+--")

    def is_space_free(self, position):
        return self.board[position] == ' '

    def is_board_full(self):
        return ' ' not in self.board

    def is_winner(self, symbol):
        return ((self.board[0] == symbol and self.board[1] == symbol and self.board[2] == symbol) or
                (self.board[3] == symbol and self.board[4] == symbol and self.board[5] == symbol) or
                (self.board[6] == symbol and self.board[7] == symbol and self.board[8] == symbol) or
                (self.board[0] == symbol and self.board[3] == symbol and self.board[6] == symbol) or
                (self.board[1] == symbol and self.board[4] == symbol and self.board[7] == symbol) or
                (self.board[2] == symbol and self.board[5] == symbol and self.board[8] == symbol) or
                (self.board[0] == symbol and self.board[4] == symbol and self.board[8] == symbol) or
                (self.board[2] == symbol and self.board[4] == symbol and self.board[6] == symbol))


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def make_move(self, board):
        while True:
            try:
                move = int(input(f"{self.name}, введите номер ячейки для своего символа ({self.symbol}): "))
                if 0 <= move <= 8 and board.is_space_free(move):
                    board.board[move] = self.symbol
                    break
                else:
                    print("Недопустимый ход. Попробуйте еще раз.")
            except ValueError:
                print("Некорректный ввод. Попробуйте еще раз.")


class TicTacToeGame:
    def __init__(self):
        self.board = GameBoard()
        self.player1 = Player("Игрок 1", "X")
        self.player2 = Player("Игрок 2", "O")

    def start_game(self):
        current_player = self.player1
        while not self.board.is_board_full():
            self.board.display_board()
            current_player.make_move(self.board)
            if self.board.is_winner(current_player.symbol):
                print(f"Поздравляем, {current_player.name}! Вы выиграли!")
                self.board.display_board()
                return
            current_player = self.player2 if current_player == self.player1 else self.player1
        print("Ничья!")
        self.board.display_board()


# Для запуска игры достаточно создать объект класса TicTacToeGame и вызвать метод start_game():
game = TicTacToeGame()
game.start_game()
