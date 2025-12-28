
### Dungeon Adventure

A simple text-based dungeon exploration game written in Python.
Explore rooms, fight monsters, heal, flee, and survive as long as possible.

### Features

- Randomly generated rooms
- Multiple monster types with different health values
- Turn-based combat system
- Critical hit mechanic
- Healing events during exploration
- Simulation mode (auto-play)
- Optional delays for immersion
- End-game statistics summary

### Gameplay Overview
- Player starts with 100 HP
- Exploring may result in:
  * Nothing happening
  * Healing
  * Monster encounter
- During combat:
  * Attack the monster
  * Flee from the fight
- Game ends when:
  * Player HP reaches 0
  * Player leaves the dungeon

### Combat System

- Base player damage: 15
- Critical hit chance: 20%
- Critical damage bonus: +30
- Damage is slightly randomized
- Bonus damage may apply if player HP is lower than enemy HP
- Monsters attack after the player if still alive

### Healing System

- 40% chance to heal on exploration
- Base heal amount: 20 HP
- Heal amount is randomized
- Maximum HP is capped at 100
- Total healed HP is tracked

### Delays

- Optional delays using time.sleep
- Can be enabled at startup
- Disabled by default for fast gameplay

### End Game Stats

- Total encounters
- Total kills
- Total healed HP
