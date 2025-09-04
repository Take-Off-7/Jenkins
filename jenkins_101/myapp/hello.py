# hello.py
import argparse

def main(name):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Greet someone.")
    parser.add_argument('--name', default='World', help='Name to greet')
    args = parser.parse_args()
    main(args.name)
