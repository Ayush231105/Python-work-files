def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print(f"Move disk 1 from {source} to {target}")
        return
    tower_of_hanoi(n - 1, source, target, auxiliary)
    print(f"Move disk {n} from {source} to {target}")
    tower_of_hanoi(n - 1, auxiliary, source, target)


# Taking input from user
n = int(input("Enter number of disks: "))

print("The sequence of moves is:")
tower_of_hanoi(n, 'A', 'B', 'C')

print(f"Total moves required: {2**n - 1}")
