from .species import Creature


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

        self.n = len(self._instances)
        self.history.append(self.n)

    def plot_history(self):
        pass
    @property
    def n(self):
        return len(self._instances)
