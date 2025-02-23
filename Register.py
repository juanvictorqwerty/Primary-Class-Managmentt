import flet as ft
import openpyxl
import os

# Excel file path
EXCEL_FILE = "ClassePrimaire.xlsx"

def ensure_excel_file():
    """Ensure the Excel file exists with a proper structure."""
    if not os.path.exists(EXCEL_FILE):
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "Students"
        ws["A3"] = "Matricule"
        ws["B3"] = "Name"
        wb.save(EXCEL_FILE)

def is_unique_matricule(matricule):
    """Check if the given Matricule (ID) is unique in the file."""
    wb = openpyxl.load_workbook(EXCEL_FILE)
    ws = wb.active
    existing_ids = [str(cell.value) for cell in ws["A"] if cell.row >= 4 and cell.value is not None]
    return matricule not in existing_ids

def add_to_excel(matricule, name):
    """Append the Matricule and Name to the Excel file, ensuring uniqueness."""
    wb = openpyxl.load_workbook(EXCEL_FILE)
    ws = wb.active

    # Find the next empty row starting from A4
    row = 4
    while ws[f"A{row}"].value is not None:
        row += 1

    # Write values
    ws[f"A{row}"] = matricule
    ws[f"B{row}"] = name

    wb.save(EXCEL_FILE)

def main(page: ft.Page):
    page.title = "Enter Matricule and Name"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    ensure_excel_file()  # Ensure the Excel file is set up

    # Text fields for input
    matricule_field = ft.TextField(label="Matricule", width=300)
    name_field = ft.TextField(label="Your Name", width=300)

    # Display area for success message
    result_text = ft.Text(size=18, color=ft.colors.BLUE)

    # Error message for validation
    error_message = ft.Text(size=16, color=ft.colors.RED)

    def submit_clicked(e):
        matricule = matricule_field.value.strip()
        name = name_field.value.strip()

        # Validate fields
        if not matricule or not name:
            error_message.value = "Please enter both Matricule and Name!"
            result_text.value = ""
        elif not matricule.isnumeric():
            error_message.value = "Matricule must be a numeric value!"
            result_text.value = ""
        elif not is_unique_matricule(matricule):
            error_message.value = "Matricule already exists! Please enter a unique one."
            result_text.value = ""
        else:
            # Append data to Excel
            add_to_excel(matricule, name)
            error_message.value = ""
            result_text.value = f"Successfully added: Matricule: {matricule}, Name: {name}"

            # Clear input fields
            matricule_field.value = ""
            name_field.value = ""

        # Update the UI
        page.update()

    # Submit button
    submit_button = ft.ElevatedButton(text="Submit", on_click=submit_clicked)

    # Add all widgets to the page
    page.add(
        ft.Column(
            [
                matricule_field,
                name_field,
                submit_button,
                error_message,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
