from .species import Creature
import matplotlib.pyplot as plt

class Population:

    _instances: set[Creature]
    history: list[int]

    def __init__(
            self,
            population_data: dict[type[Creature], int],
            **kwargs
    ):
        # Klasa gatunku jest kluczem, a wartość to liczba osobników
        self._instances = {
            species_class(**kwargs)
            for species_class, count in population_data.items()
            for _ in range(count)
        }

        self.history = [self.n]

    def natural_selection(self):
        for creature in self._instances:
            creature.kill()

        # Zachowujemy tylko żywe osobniki
        self._instances = {
            creature for creature in self._instances
            if creature.alive
        }

        self.history.append(self.n)

    def plot_history(self):
        plt.figure()

        plt.plot(
            range(len(self.history)),
            self.history,
            label="Cała populacja"
        )

        plt.xlabel("Krok symulacji")
        plt.ylabel("Liczba osobników")
        plt.title("Liczebność populacji w czasie")
        plt.legend()
        plt.grid(True)

        plt.show()

    @property
    def n(self):
        return len(self._instances)
