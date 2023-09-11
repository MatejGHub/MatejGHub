"""
def main():
    try:
        x = int(input("Enter X: "))
        print("X squared is: ", squared(x))
    except ValueError:
        print("What are you doing? o.o")


def squared(n):
    return n * n

if __name__ == "__main__":
    main()
"""
#newtask2
"""
def main():
    try:
        n = int(input("What's X: "))
        print("The X squared is: ", rand_n(n))
    except ValueError:
        print("Closing Program")

def rand_n(n):
    return n * n

if __name__ == "__main__":
    main()
"""
#newtask3
def main():
    name = input("What's your name? ")
    print(hello(name))

def hello(to = "world"):
    return f"Hello, {to}"

if __name__ == "__main__":
    main()