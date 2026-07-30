import random
from typing import Generator


def gen_event(players=('alice','bob','charlie','dylan'), actions=('run','eat','sleep','grab','move','swim','climb','use','release')) -> Generator[tuple[str,str], None, None]:
    while True:
        yield (random.choice(players), random.choice(actions))


def consume_event(lst: list[tuple[str,str]]):
    while lst:
        idx = random.randrange(len(lst))
        ev = lst.pop(idx)
        yield ev


if __name__ == "__main__":
    print("=== Game Data Stream Processor ===")
    g = gen_event()
    for i in range(1000):
        name, act = next(g)
        print(f"Event {i}: Player {name} did action {act}")
    ten = [next(g) for _ in range(10)]
    print(f"Built list of 10 events: {ten}")
    for ev in consume_event(ten):
        print(f"Got event from list: {ev}")
        print(f"Remains in list: {ten}")
