import random
import string


def main():
    h = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(1000000))
    with open("Output.txt", "w") as text_file:
        text_file.write(h)


if __name__ == '__main__':
    main()
