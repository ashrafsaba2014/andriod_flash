import flet as ft

def main(page: ft.Page):
    try:
        # إعدادات آمنة لأندرويد
        page.title = "Test App"
        page.padding = 0
        page.bgcolor = ft.Colors.WHITE

        def on_tap(e):
            page.add(ft.Text("✅ التفاعل يعمل!", size=18, color=ft.Colors.GREEN))
            page.update()

        # حاوية تضمن ظهور المحتوى في أي حجم شاشة
        page.add(
            ft.Container(
                content=ft.Column([
                    ft.Text("إذا ظهرت هذه الكلمات، فالواجهة تعمل 100%", size=16, color=ft.Colors.BLACK, weight=ft.FontWeight.BOLD),
                    ft.Container(height=20),
                    ft.ElevatedButton("اضغط هنا", on_click=on_tap, width=180, height=45)
                ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                bgcolor=ft.Colors.WHITE,
                expand=True,
                alignment=ft.alignment.center
            )
        )
        page.update()  # إجباري على الأندرويد
    except Exception as e:
        # يعرض الخطأ على الشاشة مباشرة إذا فشل البدء
        page.add(ft.Text(f"❌ خطأ أثناء التشغيل:\n{str(e)}", color=ft.Colors.RED, size=14))
        page.update()

if __name__ == "__main__":
    ft.app(target=main)
