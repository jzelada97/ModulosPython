import sys
from typing import List


def read_file_lines(filename: str) -> List[str]:
    with open(filename, 'r', encoding='utf-8') as f:
        return [line.rstrip('\n') for line in f]


def main() -> None:
    # Use sys.stdin to get input instead of input()
    args = sys.argv[1:]
    if not args:
        print("Usage: ft_stream_management.py <file>")
        return
    filename = args[0]
    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file '{filename}'")
    try:
        lines = read_file_lines(filename)
    except Exception as e:
        print(f"[STDERR] Error opening file'{filename}': {e}", file=sys.stderr)
        return
    print('---')
    for line in lines:
        print(line)
    print('---')
    print(f"File '{filename}' closed.")
    # Transform
    print('Transform data:')
    print('---')
    transformed = [line + '#' for line in lines]
    for line in transformed:
        print(line)
    print('---')
    # Prompt via stdout and read via stdin
    sys.stdout.write('Enter new file name (or empty): ')
    sys.stdout.flush()
    new_name = sys.stdin.readline().rstrip('\n')
    if not new_name:
        print('Not saving data.')
        return
    print(f"Saving data to'{new_name}'")
    try:
        with open(new_name, 'w', encoding='utf-8') as out:
            for line in transformed:
                out.write(line + '\n')
    except Exception as e:
        print(f"[STDERR] Error opening file'{new_name}': {e}", file=sys.stderr)
        print('Data not saved.')
        return
    print(f"Data saved in file '{new_name}'.")


if __name__ == "__main__":
    main()
