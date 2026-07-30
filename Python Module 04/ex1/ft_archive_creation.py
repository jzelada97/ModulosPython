import sys
from typing import List


def read_file_lines(filename: str) -> List[str]:
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: ft_archive_creation.py <file>")
        return
    filename = sys.argv[1]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file'{filename}'")
    try:
        lines = read_file_lines(filename)
    except Exception as e:
        print(f"Error opening file'{filename}': {e}")
        return
    print('---')
    for l in lines:
        print(l)
    print('---')
    print(f"File'{filename}'closed.")
    # Transform
    print('Transform data:')
    print('---')
    transformed = [l + '#' for l in lines]
    for l in transformed:
        print(l)
    print('---')
    new_name = input('Enter new file name (or empty): ')
    if not new_name:
        print('Not saving data.')
        return
    print(f"Saving data to'{new_name}'")
    try:
        with open(new_name, 'w', encoding='utf-8') as out:
            for l in transformed:
                out.write(l + '\n')
    except Exception as e:
        print(f"Error saving data to'{new_name}': {e}")
        return
    print(f"Data saved in file'{new_name}'.")


if __name__ == "__main__":
    main()
