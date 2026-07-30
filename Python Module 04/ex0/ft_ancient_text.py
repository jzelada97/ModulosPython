import sys
from typing import Tuple


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file'{filename}'")
    try:
        f = open(filename, 'r', encoding='utf-8')
    except Exception as e:
        print(f"Error opening file'{filename}': {e}")
        return
    try:
        print('---')
        for line in f:
            print(line.rstrip('\n'))
        print('---')
    finally:
        try:
            f.close()
            print(f"File'{filename}'closed.")
        except Exception:
            pass


if __name__ == "__main__":
    main()
