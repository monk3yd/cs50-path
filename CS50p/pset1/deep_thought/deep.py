def main():
    # Get input
    answer = input("""
    “All right,” said the computer, and settled into silence again. The two men fidgeted. The tension was unbearable.
    “You’re really not going to like it,” observed Deep Thought.
    “Tell us!”
    “All right,” said Deep Thought. “The Answer to the Great Question…”
    “Yes…!”
    “Of Life, the Universe and Everything…” said Deep Thought.
    “Yes…!”
    “Is…” said Deep Thought, and paused.
    “Yes…!”
    “Is…”
    “Yes…!!!…?”
    “Forty-two,” said Deep Thought, with infinite majesty and calm.”

    — The Hitchhiker’s Guide to the Galaxy, Douglas Adams
    """)

    answer = check_answer(answer)
    print(answer)


def check_answer(answer):
    # Filter input
    answer = answer.lower().strip()
    # Check answer
    if not (answer == "42" or answer == "forty-two" or answer == "forty two"):
        return "No"
    return "Yes"


main()
