import weakref
from abc import ABC, abstractmethod
from random import shuffle


class Entity(ABC):
    name: str
    _health: int
    _max_health: int

    def __init__(self, name: str, max_health: int) -> None:
        super().__init__()
        self.name = name
        self._max_health = max_health
        self._health = self._max_health

    def __add__(self, value: int):
        self._health += value
        if self._health < 0:
            self._health = 0
        elif self._health > self._max_health:
            self._health = self._max_health

    def __sub__(self, value: int):
        self._health -= value
        if self._health < 0:
            self._health = 0
        elif self._health > self._max_health:
            self._health = self._max_health

    def get_health(self) -> int:
        return self._health

    def get_max_health(self) -> int:
        return self._max_health

    def apply_damage(self, damage):
        if damage <= 0:
            return
        self._health -= damage
        if self._health < 0:
            self._health = 0

    def heal(self, healing):
        if healing <= 0:
            return
        self._health += healing
        if self._health > self._max_health:
            self._health = self._max_health

    def get_health_percentage(self) -> float:
        return self._health / self._max_health

    def is_alive(self) -> bool:
        return self._health > 0

    def is_dead(self) -> bool:
        return self._health <= 0

    @abstractmethod
    def act(self, battle: "Battle"):
        pass


class Character(Entity, ABC):
    def __init__(self, name: str, max_health: int) -> None:
        super().__init__(name, max_health)

    def __str__(self) -> str:
        if self.is_dead():
            return f"{self.name} - Muerto"
        return f"{self.name} - {round(self.get_health_percentage() * 100.0)}% ({round(self.get_health())}/{round(self.get_max_health())})"

    @abstractmethod
    def act(self, battle: "Battle"):
        pass


class Enemy(Entity, ABC):
    def __init__(self, name: str, max_health: int) -> None:
        super().__init__(name, max_health)

    def __str__(self) -> str:
        if self.is_dead():
            return f'Enemigo "{self.name}" - Muerto'
        return f'Enemigo "{self.name}" - {round(self.get_health_percentage() * 100.0)}%'

    @abstractmethod
    def act(self, battle: "Battle"):
        pass


class _NextTurnOrder:
    _initial_turn_number: int
    _turn_order: list[weakref.ref[Entity]]
    _current: int = 0

    def __init__(self, turn_number: int, turn_order: list[weakref.ref[Entity]]):
        self._initial_turn_number = turn_number
        self._turn_order = turn_order

    def __iter__(self):
        return self

    def __next__(self):
        while self._current < len(self._turn_order):
            result = self._turn_order[
                (self._initial_turn_number + self._current) % len(self._turn_order)
            ]()
            if result is None:
                continue
            self._current += 1
            if result.is_dead():
                continue
            return result
        else:
            # Tell the loop construct that iteration is complete
            raise StopIteration


class Battle:
    _characters: list[Character]
    _enemies: list[Enemy]
    _turn_order: list[weakref.ref[Entity]]
    _current_turn: int = 0

    def __init__(self, characters: list[Character], enemies: list[Enemy]) -> None:
        if len(characters) == 0:
            raise ValueError("Characters may not be empty")
        if len(enemies) == 0:
            raise ValueError("Enemies may not be empty")

        self._characters = characters
        self._enemies = enemies

        self._turn_order = []
        for enemy in enemies:
            self._turn_order.append(weakref.ref(enemy))
        shuffle(self._turn_order)
        for character in characters:
            self._turn_order.insert(0, weakref.ref(character))

    def get_enemies(self) -> list[Enemy]:
        return self._enemies

    def get_alive_enemies(self) -> list[Enemy]:
        result = list(self._enemies)
        for i in range(len(self._enemies) - 1, -1, -1):
            if self._enemies[i].is_dead():
                result.pop(i)
        return result

    def get_characters(self) -> list[Character]:
        return self._characters

    def get_alive_characters(self) -> list[Character]:
        result = list(self._characters)
        for i in range(len(self._characters) - 1, -1, -1):
            if self._characters[i].is_dead():
                result.pop(i)
        return result

    def get_current_turn(self) -> int:
        return self._current_turn

    def get_turn_order(self) -> list[weakref.ref[Entity]]:
        return self._turn_order

    def has_lost(self) -> bool:
        all_charas_dead = True
        for charas in self._characters:
            if charas.is_alive():
                all_charas_dead = False
                break

        if all_charas_dead:
            return True
        return False

    def defeated_all_enemies(self) -> bool:
        all_enemies_dead = True
        for enemy in self._enemies:
            if enemy.is_alive():
                all_enemies_dead = False
                break

        if all_enemies_dead:
            return True
        return False

    def has_won(self) -> bool:
        if not self.has_lost() and self.defeated_all_enemies():
            return True

        return False

    def is_finished(self) -> bool:
        if self.has_lost():
            return True

        if self.defeated_all_enemies():
            return True

        return False

    def next_turn(self) -> Entity:
        current_entity: Entity | None = self._turn_order[
            self._current_turn % len(self._turn_order)
        ]()
        assert current_entity is not None
        self._current_turn += 1
        return current_entity

    def get_next_turns(self) -> _NextTurnOrder:
        return _NextTurnOrder(self._current_turn, self._turn_order)

    def __iter__(self):
        return self

    def __next__(self):
        if self.is_finished():
            raise StopIteration
        return self.next_turn()
