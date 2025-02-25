import flet as ft
import subprocess
import sys
import os

def main(page: ft.Page):
    page.title = "Student Grades Management"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.colors.GREY_100
    
    def open_script(script_name):
        try:
            script_path = os.path.join(os.getcwd(), script_name)
            if not os.path.exists(script_path):
                raise FileNotFoundError(f"{script_name} not found!")
            
            # Use subprocess to open the script in a new console window
            subprocess.Popen([sys.executable, script_path], creationflags=subprocess.CREATE_NEW_CONSOLE)

            status_text.value = f"{script_name} launched successfully!"
            status_text.color = ft.colors.GREEN
        except FileNotFoundError as e:
            status_text.value = str(e)
            status_text.color = ft.colors.RED
        except Exception as e:
            status_text.value = f"Error launching {script_name}: {str(e)}"
            status_text.color = ft.colors.RED
        page.update()
    
    def open_register_file(e):
        open_script("Register.py")
    
    def open_display_grades_file(e):
        open_script("Display_grades.py")
    
    # Status text to show launch results
    status_text = ft.Text(size=16)
    
    # Create the UI
    page.add(
        ft.Column(
            [
                ft.Text(
                    "Student Grades Management",
                    size=28,
                    weight=ft.FontWeight.BOLD,
                    color=ft.colors.BLUE,
                    text_align=ft.TextAlign.CENTER
                ),
                ft.Divider(),
                ft.ElevatedButton(
                    "Enter Grades",
                    icon=ft.icons.EDIT_NOTE,
                    on_click=open_register_file,
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.BLUE
                    ),
                    width=200,
                    height=50
                ),
                ft.ElevatedButton(
                    "View Grades",
                    icon=ft.icons.VISIBILITY,
                    on_click=open_display_grades_file,
                    style=ft.ButtonStyle(
                        color=ft.colors.WHITE,
                        bgcolor=ft.colors.GREEN
                    ),
                    width=200,
                    height=50
                ),
                status_text
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=20
        )
    )

if __name__ == "__main__":
    ft.app(target=main)