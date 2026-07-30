import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    args = sys.argv[1:]
    if not args:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    scores = []
    for a in args:
        try:
            val = int(a)
            scores.append(val)
        except ValueError:
            print(f"Invalid parameter:'{a}'")
    if not scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return
    total = sum(scores)
    avg = total / len(scores)
    high = max(scores)
    low = min(scores)
    rng = high - low
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {avg}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {rng}")


if __name__ == "__main__":
    main()
