import flet as ft

def main(page: ft.Page):
    page.title = "Student Grades Table"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Définition des colonnes
    columns = [
        "Matricule", "Trimestre", "Maths", "Sciences", "Histoire", "Geo", "ECM", "Francais", "Anglais"
    ]

    table = ft.DataTable(
        columns=[ft.DataColumn(ft.Text(col)) for col in columns],
        rows=[]
    )

    input_fields = []  # Liste des lignes contenant les champs

    # Ajouter une ligne
    def add_row(e):
        row_fields = {}
        cells = []
        
        for index, col_name in enumerate(columns):
            if index == 1:  # Trimestre
                field = ft.TextField(width=100, height=40, input_filter=ft.InputFilter(r'^\d*$'), hint_text="1-3")
            elif index >= 2:  # Notes
                field = ft.TextField(width=100, height=40, input_filter=ft.InputFilter(r'^\d*$'), hint_text="0-20")
            else:  # Matricule
                field = ft.TextField(width=100, height=40)

            row_fields[col_name] = field
            cells.append(ft.DataCell(field))

        input_fields.append(row_fields)  # Ajouter la ligne complète
        table.rows.append(ft.DataRow(cells=cells))
        page.update()

    # Validation des entrées
    def validate_input(value, min_value, max_value, field_name):
        try:
            num = int(value)
            if num < min_value or num > max_value:
                return f"{field_name} must be between {min_value} and {max_value}!"
            return None
        except ValueError:
            return f"{field_name} must be a valid number!"

    # Soumettre les données
    def submit_data(e):
        errors = []
        collected_data = []

        for row in input_fields:
            row_data = {}
            for col_name, field in row.items():
                value = field.value.strip()
                error = None

                if col_name == "Trimestre":
                    error = validate_input(value, 1, 3, col_name)
                elif col_name in columns[2:]:  # Notes
                    error = validate_input(value, 0, 20, col_name)

                if error:
                    errors.append(error)
                    field.border_color = ft.colors.RED  # Indiquer l'erreur sur le champ
                else:
                    field.border_color = None  # Réinitialiser la bordure
                    row_data[col_name] = value

            collected_data.append(row_data)

        # Afficher erreurs ou résultats
        if errors:
            result_text.value = "\n".join(errors)
            result_text.color = ft.colors.RED
        else:
            result_text.value = "\n".join([str(data) for data in collected_data])
            result_text.color = ft.colors.BLUE

        page.update()

    # Boutons
    add_row_button = ft.ElevatedButton(text="Add Row", on_click=add_row)
    submit_button = ft.ElevatedButton(text="Submit", on_click=submit_data)

    # Zone d'affichage des erreurs ou des résultats
    result_text = ft.Text(size=16)

    # Ajout des widgets à la page
    page.add(
        ft.Column(
            [
                table,
                add_row_button,
                submit_button,
                result_text,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)
