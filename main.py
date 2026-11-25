import os

ENTRY = "The client already approved the draft as-is this morning, so this meeting is just nine people congratulating themselves for a decision none of them made."

assert ENTRY.strip(), "entry must not be empty"
assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
