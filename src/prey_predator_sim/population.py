from .species import Creature


class Population:
    _instances: set[Creature]

    def __init__(self, n: int, **kwargs):
        self._instances = set(
            [Creature(**kwargs) for i in range(n)]
        )

        self.n = len(self._instances)

    def natural_selection(self):
        for creature in self._instances:
            creature.kill()

        self._instances = set([creature for creature in self._instances if creature.alive])
        self.n = len(self._instances)