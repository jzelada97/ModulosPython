import random


def gen_player_achievements(all_achievements: list[str]) -> set[str]:
    k = random.randint(1, max(1, len(all_achievements)//3))
    return set(random.sample(all_achievements, k))


def main() -> None:
    print("=== Achievement Tracker System ===")
    all_achievements = [
        'Crafting Genius','World Savior','Master Explorer','Collector Supreme','Untouchable',
        'Boss Slayer','Strategist','Speed Runner','Survivor','Treasure Hunter','First Steps','Sharp Mind','Hidden Path Finder'
    ]
    players = ['Alice','Bob','Charlie','Dylan']
    data = {p: gen_player_achievements(all_achievements) for p in players}
    for p, s in data.items():
        print(f"Player {p}: {s}")
    union_all = set().union(*data.values())
    common = set.intersection(*data.values())
    print(f"All distinct achievements: {union_all}")
    print(f"Common achievements: {common}")
    for p in players:
        others = set().union(*(data[q] for q in players if q != p))
        only = data[p] - others
        print(f"Only {p} has: {only}")
    for p in players:
        missing = union_all - data[p]
        print(f"{p} is missing: {missing}")


if __name__ == "__main__":
    main()
