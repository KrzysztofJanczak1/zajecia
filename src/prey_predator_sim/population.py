from .species import Creature
import matplotlib.pyplot as plt

class Population:

    _instances: set[Creature]
    history: list[int]

    def __init__(self, n: int, **kwargs):
        self._instances = set(
            [Creature(**kwargs) for i in range(n)]
        )

        self.history = [self.n]

    def natural_selection(self):
        for creature in self._instances:
            creature.kill()

        self._instances = set([creature for creature in self._instances if creature.alive])

        self.history.append(self.n)

    def plot_history(self):
        plt.figure()

        plt.plot(
            range(len(self.history)),
            self.history,
            label="Creature"
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
