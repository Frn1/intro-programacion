import random
from math import ceil, floor
from time import sleep
from typing import Sequence

from battle import Battle, Character, Enemy, Entity


def do_attack(
    source: Entity,
    target: Entity,
    min_normal: int,
    max_normal: int,
    min_crit: int,
    max_crit: int,
    crit_percent: float = 0.05,
):
    is_crit = False
    damage: int
    if random.random() < crit_percent:
        damage = random.randint(min_crit, max_crit)
        is_crit = True
    else:
        damage = random.randint(min_normal, max_normal)

    if is_crit:
        print("Crítico! ", end="")
    print(f"{source.name} le hace {damage} puntos de daño a {target.name}.")
    target.apply_damage(damage)
    print(f"Estado: {target}.")


class BasicEnemy(Enemy):
    def __init__(self, name: str, max_health: int) -> None:
        super().__init__(name, max_health)

    def act(self, battle: "Battle"):
        character_to_attack = random.choice(battle.get_alive_characters())
        do_attack(
            self,
            character_to_attack,
            min_normal=10,
            max_normal=20,
            min_crit=40,
            max_crit=60,
        )


def _enumerate_targets(targets: Sequence[Entity]):
    if len(targets) == 0:
        raise Exception("There are no valid targets to choose")
    for i, entity in enumerate(targets):
        print(f" {i + 1}: {entity.name}")


def _pick_target(
    targets: Sequence[Entity], target_type_name: str = "objetivo"
) -> Entity | None:
    _enumerate_targets(targets)
    target = input(f"Elige un {target_type_name}: ")
    if not target.isnumeric():
        return None
    target = int(target) - 1
    if target < 0 or target >= len(targets):
        return None
    return targets[target]


def _pick_alive_enemy(battle: Battle) -> Entity | None:
    enemies = battle.get_alive_enemies()
    target_enemy = _pick_target(enemies, "enemigo")
    return target_enemy


def _pick_alive_character(battle: Battle) -> Entity | None:
    characters = battle.get_alive_characters()
    target_character = _pick_target(characters, "personaje")
    return target_character


class ControllablePlayer(Character):
    def __init__(self, name: str, max_health: int) -> None:
        super().__init__(name, max_health)

    def act(self, battle: "Battle"):
        print()
        print("----- Siguientes turnos -----")
        for i, next in enumerate(battle.get_next_turns()):
            entity = next
            if entity is None:
                raise ValueError
            print(f"En {i + 1} turno{'s' if i != 0 else ''} le toca a {entity.name}")
        print()
        while True:
            print("----- Estado actual -----")
            for enemy in battle.get_enemies():
                print(enemy)
            print()
            for character in battle.get_characters():
                print(character)

            print()
            print("----- Menú -----")
            print(" 1. Puño")
            print(" 2. Patada")
            print(" 3. Curar")
            print()
            seleccion = int(input("Tu selección: "))

            print()
            match seleccion:
                case 1:
                    print("--- Elige a quien pegarle ---")
                    target = _pick_alive_enemy(battle)
                    while target is None:
                        print("Enemigo invalido, elije de nuevo.")
                        target = _pick_alive_enemy(battle)
                        continue
                    print()
                    do_attack(
                        self,
                        target,
                        min_normal=30,
                        max_normal=70,
                        min_crit=100,
                        max_crit=150,
                    )
                    if target.is_dead():
                        print(f"{target.name} fue derrotado!")
                    break

                case 2:
                    print("--- Elige a quien patear ---")
                    target = _pick_alive_enemy(battle)
                    while target is None:
                        print("Enemigo invalido, elije de nuevo.")
                        target = _pick_alive_enemy(battle)
                        continue
                    print()
                    do_attack(
                        self,
                        target,
                        20,
                        40,
                        min_crit=200,
                        max_crit=300,
                        crit_percent=0.15,
                    )
                    if target.is_dead():
                        print(f"{target.name} fue derrotado!")
                    break

                case 3:
                    print("--- Elige a quien curar ---")
                    target = _pick_alive_character(battle)
                    while target is None:
                        print("Personaje invalido, elije de nuevo.")
                        target = _pick_alive_character(battle)
                        continue
                    print()
                    heal_amount = random.randint(
                        floor(target.get_max_health() * 0.2),
                        ceil(target.get_max_health() * 0.4),
                    )
                    target.heal(heal_amount)
                    print(f"{self.name}", end="")
                    if target == self:
                        print(" se cura ", end="")
                    else:
                        print(f" cura a {target.name} ", end="")
                    print(
                        f"por {heal_amount} punto{'s' if heal_amount != 1 else ''} de vida"
                    )
                    break

                case _:
                    print("No reconozco esa opcion.")
                    sleep(0.3)


if __name__ == "__main__":
    battle = Battle(
        characters=[
            ControllablePlayer(name="Naranjita", max_health=random.randint(100, 150)),
        ],
        enemies=[
            BasicEnemy(name="Slime azul", max_health=random.randint(40, 70)),
            BasicEnemy(name="Slime rojo", max_health=random.randint(50, 70)),
            BasicEnemy(name="Slime verde", max_health=random.randint(50, 75)),
        ],
    )

    turnos = 1
    for current_entity in battle:
        if current_entity.is_dead():
            continue
        print(f"Turno {turnos}: {current_entity.name}")
        current_entity.act(battle)
        print()
        turnos += 1
        sleep(0.75)

    if battle.has_lost():
        print("Perdiste!")
    elif battle.defeated_all_enemies():
        print("Ganaste!")
    else:
        print("Empate?????")
