import flet as ft

def main(page: ft.Page):
    page.title = "Enter Matricule and Name"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Text fields for input
    matricule_field = ft.TextField(label="Matricule", width=300)
    name_field = ft.TextField(label="Your Name", width=300)

    # Display area for the entered data
    result_text = ft.Text(size=18, color=ft.colors.BLUE)

    # Error message for validation
    error_message = ft.Text(size=16, color=ft.colors.RED)

    def submit_clicked(e):
        # Get the values from the text fields
        matricule = matricule_field.value.strip()
        name = name_field.value.strip()

        # Validate the fields
        if not matricule or not name:
            error_message.value = "Please enter both Matricule and Name!"
            result_text.value = ""  # Clear the result text
        else:
            error_message.value = ""  # Clear the error message
            result_text.value = f"Matricule: {matricule}, Name: {name}"

        # Update the page to reflect changes
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
                error_message,  # Display error message here
                result_text,  # Display result here
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)