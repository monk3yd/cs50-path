import sys

from fpdf import FPDF


def main():
    generate_shirtificate(input("Name: "))


def generate_shirtificate(name):
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Font
    pdf.set_font("helvetica", "B", 28)

    # Print image
    pdf.image("shirtificate.png", x=0, y=70)

    # Move cursor
    pdf.cell(80)

    # Write title
    title = "CS50 Shirtificate"
    pdf.cell(30, 10, title, border=0, align="C", )

    pdf.ln(130)
    pdf.cell(75)

    # Write name
    pdf.set_font("helvetica", "", 24)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(70, 10, f"{name} took CS50", align="C")

    # newline
    # pdf.ln(20)
    ...
    # Save to file
    pdf.output("shirtificate.pdf")
    sys.exit(0)


if __name__ == "__main__":
    main()
