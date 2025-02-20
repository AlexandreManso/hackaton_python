class GameException(Exception):  # noqa: N818
    """Exception super-class for all Snake exceptions."""

    def __init__(self, msg: str) -> None:
        """Object initialization."""
        super().__init__(msg)


class GameOver(GameException):
    """Exception class used to signal game over."""

    def __init__(self) -> None:
        """Object initialization."""
        super().__init__("Game over!")


class EnemyEncounter(GameException):
    """Exception Class used to signal ennemy encounters."""

    def __init__(self) -> None:
        """Object initialization."""
        super().__init__("Encountered ennemy!")


class GameError(Exception):
    """Exception super-class for all Snake errors."""

    def __init__(self, msg: str) -> None:
        """Object initialization."""
        super().__init__(msg)


class IntRangeError(GameError):
    """Exception for integer range error."""

    def __init__(self, label: str, value: int, low: int, high: int) -> None:
        """Object initialization."""
        super().__init__(
            f"{label} value must be between {low} and {high}."
            f" {value} is not allowed."
        )


class ColorError(GameError):
    """Exception for color format error."""

    def __init__(self, color: str) -> None:
        """Object initialization."""
        super().__init__(
            f'Color "{color}" does not respect the HTML' " hexadecimal format #rrggbb."
        )
