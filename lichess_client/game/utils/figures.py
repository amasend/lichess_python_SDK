from enum import Enum


class FigureTypes(str, Enum):
    """Types of the available figures."""
    KING = 'K'
    QUEEN = 'Q'
    BISHOP = 'B'
    ROOK = 'R'
    KNIGHT = 'N'
