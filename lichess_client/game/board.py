from chess import Board


class CustomBoard(Board):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_vectors(self):
        board_state_rows = self.__str__().split('\n')
        # TODO: write board representation for Neural Network