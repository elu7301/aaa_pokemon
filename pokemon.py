from abc import ABC, abstractmethod

class PokemonTrainInterface(ABC):
    """An abstract base class defining an interface for training Pokemons."""

    @classmethod
    @abstractmethod
    def increase_experience(self, value: int) -> None:
        """Increases the experience of the Pokemon by the given value.

        Args:
            value (int): The value to increase the experience by.
        """
        pass

    @property
    @abstractmethod
    def experience(self) -> int:
        """int: The experience of the Pokemon."""
        pass


class BasePokemon(PokemonTrainInterface):
    """A base class representing a Pokemon."""

    def __init__(self, name: str, poketype: str):
        """Initializes a BasePokemon instance.

        Args:
            name (str): The name of the Pokemon.
            poketype (str): The type of the Pokemon.
        """
        self.name = name
        self.poketype = poketype
        self._experience = 100

    def increase_experience(self, value: int) -> None:
        """Increases the experience of the Pokemon by the given value.

        Args:
            value (int): The value to increase the experience by.
        """
        self._experience += value

    @property
    def experience(self) -> int:
        """int: The experience of the Pokemon."""
        return self._experience


if __name__ == '__main__':
    bulbasaur = BasePokemon(name='Bulbasaur', poketype='grass')
    bulbasaur.increase_experience(100)
    assert bulbasaur.experience == 200, 'Try harder, Neeman'