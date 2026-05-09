import flet as ft

def main(page: ft.Page):
    page.title = "Test App"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 20

    status = ft.Text("جاهز للتشغيل", size=20, color=ft.Colors.BLUE)

    def on_click(e):
        status.value = "تم الضغط بنجاح! 🎉"
        status.color = ft.Colors.GREEN
        page.update()

    page.add(
        ft.AppBar(title=ft.Text("اختبار"), bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
        ft.Column([
            status,
            ft.ElevatedButton("اضغط هنا", on_click=on_click, width=200, height=50)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
    )
    page.update()  # ⚠️ إلزامي لظهور الواجهة على الأندرويد

if __name__ == "__main__":
    ft.app(target=main)
