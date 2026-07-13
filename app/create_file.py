import datetime
import sys
from pathlib import Path


def main() -> None:
    args = sys.argv[1:]

    directories: list[str] = []
    filename: str | None = None

    i = 0
    while i < len(args):
        if args[i] == "-d":
            i += 1
            while i < len(args) and not args[i].startswith("-"):
                directories.append(args[i])
                i += 1
        elif args[i] == "-f":
            i += 1
            if i < len(args):
                filename = args[i]
                i += 1
        else:
            i += 1

    dir_path = Path(*directories) if directories else Path(".")
    if directories:
        dir_path.mkdir(parents=True, exist_ok=True)

    lines = []
    while True:
        content = input("Enter content line: ")
        if content.strip().lower() == "stop":
            break
        lines.append(content)

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    formatted_content = timestamp + "\n"

    for index, line in enumerate(lines, 1):
        formatted_content += f"{index} {line}\n"

    if filename:
        file_path = dir_path / filename if directories else Path(filename)

        if file_path.exists():
            formatted_content = "\n" + formatted_content

        with open(file_path, "a", encoding="utf-8") as f:
            f.write(formatted_content)


if __name__ == "__main__":
    main()
