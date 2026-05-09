import flet as ft

def main(page: ft.Page):
    page.title = "Ashraf App - Working"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = ft.Colors.WHITE
    page.padding = 20

    # نص الحالة
    status = ft.Text("جاهز للتشغيل ✅", size=22, color=ft.Colors.BLUE, weight=ft.FontWeight.BOLD)

    # عند الضغط
    def on_click(e):
        status.value = "تم الضغط بنجاح! 🎉"
        status.color = ft.Colors.GREEN
        page.update()

    # عند طلب الخروج
    def on_exit(e):
        def close_app(e2):
            page.pop_dialog()
            page.close()  # الطريقة الآمنة لإغلاق Flet على الأندرويد
        def keep_open(e2):
            page.pop_dialog()
        page.show_dialog(
            ft.AlertDialog(
                title=ft.Text("تأكيد الخروج"),
                content=ft.Text("هل تريد إغلاق التطبيق؟"),
                actions=[
                    ft.TextButton("لا", on_click=keep_open),
                    ft.TextButton("نعم", on_click=close_app),
                ],
            )
        )

    # الهيكل الآمن للأندرويد
    page.add(
        ft.AppBar(
            title=ft.Text("تطبيق اختباري"),
            bgcolor=ft.Colors.RED,
            color=ft.Colors.WHITE,
            actions=[
                ft.PopupMenuButton(
                    items=[ft.PopupMenuItem(text="خروج", on_click=on_exit)]
                )
            ]
        ),
        ft.Container(
            content=ft.Column([
                status,
                ft.ElevatedButton("اختبار التفاعل", on_click=on_click, width=200, height=50),
            ], horizontal_alignment=ft.CrossAxisAlignment.CENTER, spacing=30),
            alignment=ft.alignment.center,
            expand=True
        )
    )
    page.update()  # ⚠️ ضروري جدًا على الأندرويد لإجبار الرسم

if __name__ == "__main__":
    ft.app(target=main)  # ✅ الدالة الرسمية للتشغيل في Flet 0.80+
