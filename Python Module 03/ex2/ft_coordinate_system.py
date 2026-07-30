import math


def parse_coords(s: str) -> tuple[float, float, float]:
    parts = [p.strip() for p in s.split(',')]
    if len(parts) != 3:
        raise ValueError('Invalid syntax')
    try:
        x = float(parts[0])
        y = float(parts[1])
        z = float(parts[2])
    except ValueError as e:
        raise ValueError(f"Error on parameter'{parts[parts.index(next(p for p in parts if not is_float(p)))]}': {e}")
    return (x, y, z)


def is_float(s: str) -> bool:
    try:
        float(s)
        return True
    except Exception:
        return False


def get_player_pos() -> tuple[float, float, float]:
    while True:
        s = input("Enter new coordinates as floats in format'x,y,z': ")
        try:
            coords = parse_coords(s)
            return coords
        except Exception as e:
            print(e)


def dist(a: tuple[float, float, float], b: tuple[float, float, float]) -> float:
    return math.sqrt((b[0]-a[0])**2 + (b[1]-a[1])**2 + (b[2]-a[2])**2)


if __name__ == "__main__":
    print("=== Game Coordinate System ===")
    print("Get a first set of coordinates")
    c1 = get_player_pos()
    print(f"Got a first tuple: {c1}")
    print(f"It includes: X={c1[0]}, Y={c1[1]}, Z={c1[2]}")
    center = (0.0, 0.0, 0.0)
    print(f"Distance to center: {round(dist(c1, center), 4)}")

    print("Get a second set of coordinates")
    c2 = get_player_pos()
    print(f"Distance between the 2 sets of coordinates: {round(dist(c1, c2), 4)}")
