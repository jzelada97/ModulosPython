from typing import List, Dict


def artifact_sorter(artifacts: List[Dict]) -> List[Dict]:
    return sorted(artifacts, key=lambda a: a.get('power', 0), reverse=True)


def power_filter(mages: List[Dict], min_power: int) -> List[Dict]:
    return list(filter(lambda m: m.get('power', 0) >= min_power, mages))


def spell_transformer(spells: List[str]) -> List[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: List[Dict]) -> Dict[str, float]:
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    max_p = max(mages, key=lambda m: m.get('power', 0))['power']
    min_p = min(mages, key=lambda m: m.get('power', 0))['power']
    powers = list(map(lambda m: m.get('power', 0), mages))
    avg_p = round(sum(powers) / len(powers), 2)
    return {'max_power': max_p, 'min_power': min_p, 'avg_power': avg_p}


def main() -> None:
    print('Testing artifact sorter...')
    artifacts = [
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
    ]
    sorted_art = artifact_sorter(artifacts)
    first = sorted_art[0]
    second = sorted_art[1]
    print(
        f"{first['name']} ({first['power']} power) comes before "
        f"{second['name']} ({second['power']} power)"
    )

    print('Testing spell transformer...')
    spells = ['fireball', 'heal', 'shield']
    print(' '.join(spell_transformer(spells)))


if __name__ == '__main__':
    main()
