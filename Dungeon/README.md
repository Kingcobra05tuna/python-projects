========================================
        DUNGEON ADVENTURE (Python)
========================================

A simple text-based dungeon exploration game written in Python.
Explore rooms, fight monsters, heal, flee, and survive as long as possible.

----------------------------------------
FEATURES
----------------------------------------
- Randomly generated rooms
- Multiple monster types with different health values
- Turn-based combat system
- Critical hit mechanic
- Healing events during exploration
- Simulation mode (auto-play)
- Optional delays for immersion
- End-game statistics summary

----------------------------------------
GAMEPLAY OVERVIEW
----------------------------------------
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

----------------------------------------
MONSTERS
----------------------------------------
Goblin     - 25 HP
Giant      - 50 HP
Snake      - 15 HP
Zombie     - 30 HP
Skeleton   - 20 HP
Mouse      - 10 HP
Dragon     - 90 HP

----------------------------------------
COMBAT SYSTEM
----------------------------------------
- Base player damage: 15
- Critical hit chance: 20%
- Critical damage bonus: +30
- Damage is slightly randomized
- Bonus damage may apply if player HP is lower than enemy HP
- Monsters attack after the player if still alive

----------------------------------------
HEALING SYSTEM
----------------------------------------
- 40% chance to heal on exploration
- Base heal amount: 20 HP
- Heal amount is randomized
- Maximum HP is capped at 100
- Total healed HP is tracked

----------------------------------------
GAME MODES
----------------------------------------
NORMAL MODE
- Manual input
- Player chooses actions

SIMULATION MODE
- Automatic exploration and combat
- No player input
- Useful for testing and balancing

----------------------------------------
DELAYS
----------------------------------------
- Optional delays using time.sleep
- Can be enabled at startup
- Disabled by default for fast gameplay

----------------------------------------
END GAME STATS
----------------------------------------
- Total encounters
- Total kills
- Total healed HP

----------------------------------------
HOW TO RUN
----------------------------------------
Requirements:
- Python 3.x

Run:
python main.py

----------------------------------------
PROJECT STRUCTURE
----------------------------------------
.
|-- main.py
|-- README.txt
========================================
