
import flet as ft

def main(page: ft.Page):
    page.title = "Ashraf App - Working"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    status = ft.Text("جاهز للتشغيل ✅", size=20, color=ft.Colors.BLUE)

    def on_click(e):
        status.value = "تم الضغط على الزر بنجاح! 🎉"
        status.color = ft.Colors.GREEN
        page.update()

    def on_exit(e):
        page.show_dialog(
            ft.AlertDialog(
                title=ft.Text("تأكيد الخروج"),
                content=ft.Text("هل تريد إغلاق التطبيق؟"),
                actions=[
                    ft.TextButton("لا", on_click=lambda _: page.pop_dialog()),
                    ft.TextButton("نعم", on_click=lambda _: page.close()),
                ],
                actions_alignment=ft.MainAxisAlignment.END,
            )
        )

    page.add(
        ft.AppBar(
            title=ft.Text("تطبيق اختباري"),
            actions=[ft.PopupMenuButton(items=[ft.PopupMenuItem(text="خروج", on_click=on_exit)])]
        ),
        status,
        ft.ElevatedButton("اختبار التفاعل", on_click=on_click)
    )

if __name__ == "__main__":
    ft.run(main)
