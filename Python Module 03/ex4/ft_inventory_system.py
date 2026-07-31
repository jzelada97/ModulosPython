import sys


def parse_param(p: str):
    if ':' not in p:
        raise ValueError(f"Error - invalid parameter '{p}'")
    name, qty = p.split(':', 1)
    if not name:
        raise ValueError(f"Error - invalid parameter '{p}'")
    try:
        q = int(qty)
    except ValueError as e:
        raise ValueError(f"Quantity error for '{name}': {e}")
    return name, q


def main() -> None:
    print("=== Inventory System Analysis ===")
    args = sys.argv[1:]
    inv: dict[str, int] = {}
    for p in args:
        try:
            name, q = parse_param(p)
            if name in inv:
                print(f"Redundant item '{name}' - discarding")
                continue
            inv[name] = q
        except ValueError as e:
            print(e)
    if not inv:
        print("Got inventory: {}")
        return
    print(f"Got inventory: {inv}")
    items = list(inv.keys())
    print(f"Item list: {items}")
    total = sum(inv.values())
    print(f"Total quantity of the {len(items)} items: {total}")
    for name, q in inv.items():
        pct = (q / total) * 100
        print(f"Item {name} represents {round(pct, 1)}%")
    most = max(inv.items(), key=lambda kv: kv[1])
    least = min(inv.items(), key=lambda kv: kv[1])
    print(f"Item most abundant: {most[0]} with quantity {most[1]}")
    print(f"Item least abundant: {least[0]} with quantity {least[1]}")
    inv['magic_item'] = 1
    print(f"Updated inventory: {inv}")


if __name__ == "__main__":
    main()
