import sys


def main() -> None:
    print("=== Command Quest ===")
    argv = sys.argv
    prog = argv[0] if len(argv) > 0 else ""
    print(f"Program name: {prog}")
    args = argv[1:]
    if not args:
        print("No arguments provided!")
        print(f"Total arguments: {len(argv)}")
    else:
        print(f"Arguments received: {len(args)}")
        for i, a in enumerate(args, start=1):
            print(f"Argument {i}: {a}")
        print(f"Total arguments: {len(argv)}")


if __name__ == "__main__":
    main()
