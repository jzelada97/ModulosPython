import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    players = ['Alice', 'Bob', 'Charlie', 'Dylan', 'Emma', 'Gregory', 'John', 'Kevin', 'Liam']
    capitalized = [p.capitalize() for p in players]
    only_capitalized = [p for p in players if p[0].isupper()]
    print(f"Initial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized}")
    print(f"New list of capitalized names only: {only_capitalized}")
    score_dict = {p: random.randint(0, 1000) for p in capitalized}
    avg = sum(score_dict.values()) / len(score_dict)
    highscores = {k: v for k, v in score_dict.items() if v > avg}
    print(f"Score dict: {score_dict}")
    print(f"Score average is {round(avg, 2)}")
    print(f"High scores: {highscores}")


if __name__ == "__main__":
    main()
