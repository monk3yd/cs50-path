import sys
import csv


def main():
    # Expect 2 command-line argumnets
    is_valid = check_arguments(sys.argv)
    if isinstance(is_valid, str):
        sys.exit(is_valid)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    response = convert(input_path, output_path)
    if response is False:
        sys.exit(f"Could not read {output_path}")
    sys.exit(0)


def check_arguments(args):
    if len(args) < 3:
        return "Too few command-line arguments"

    if len(args) > 3:
        return "Too many command-line arguments"
    return True


def convert(input, output):
    students = []
    try:
        with open(input) as file:
            reader = csv.DictReader(file)
            for line in reader:  # each line is a student
                last, first = line["name"].split(",")
                student = {"first": first.strip(), "last": last, "house": line["house"]}
                students.append(student)

    except FileNotFoundError:
        return False
    else:
        with open(output, "w") as file:
            writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow(student)

        return True


if __name__ == "__main__":
    main()
