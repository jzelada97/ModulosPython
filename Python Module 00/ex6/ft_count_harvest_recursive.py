def ft_count_harvest_recursive():
    n = int(input("Days until harvest: "))

    def count(current):
        if current > n:
            return
        print("Day " + str(current))
        count(current + 1)

    count(1)
    print("Harvest time!")
