import random

from battle import Battle, Character, Enemy


class BasicEnemy(Enemy):
    def __init__(self, name: str, max_health: float) -> None:
        super().__init__(name, max_health)

    def act(self, battle: "Battle"):
        character_to_attack = random.choice(battle.get_alive_characters())
        if random.random() < 0.05:
            character_to_attack.damage(random.uniform(70.0, 120.0))
        else:
            character_to_attack.damage(random.uniform(10.0, 40.0))


class ControllablePlayer(Character):
    def __init__(self, name: str, max_health: float) -> None:
        super().__init__(name, max_health)

    def act(self, battle: "Battle"):
        enemy_to_attack = random.choice(battle.get_alive_enemies())
        if random.random() < 0.05:
            enemy_to_attack.damage(random.uniform(70.0, 120.0))
        else:
            enemy_to_attack.damage(random.uniform(10.0, 40.0))


if __name__ == "__main__":
    battle = Battle(
        characters=[
            ControllablePlayer(name="Naranjita", max_health=167),
            ControllablePlayer(name="Syl", max_health=167),
            ControllablePlayer(name=":3", max_health=167),
        ],
        enemies=[
            BasicEnemy(name="Slimo 1", max_health=60),
            BasicEnemy(name="Slimo 2", max_health=60),
            BasicEnemy(name="Slimo 3", max_health=60),
            BasicEnemy(name="Slimo 4", max_health=60),
        ],
    )

    for current_entity in battle:
        if current_entity.is_dead():
            continue
        print(f"Actuando: {current_entity}")
        current_entity.act(battle)

    if battle.has_lost():
        print("Perdiste!")
    elif battle.defeated_all_enemies():
        print("Ganaste!")
    else:
        print("Empate?????")
