import sys

def main(name="World"):
    print(f"Hello, {name}!")

if __name__ == "__main__":
    # Check for --name argument
    if "--name" in sys.argv:
        index = sys.argv.index("--name") + 1
        if index < len(sys.argv):
            main(sys.argv[index])
        else:
            main()
    else:
        main()
