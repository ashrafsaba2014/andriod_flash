import flet as ft

def main(page: ft.Page):
    # إعدادات أساسية آمنة
    page.title = "Test App"
    page.bgcolor = ft.Colors.WHITE
    page.padding = 20

    status = ft.Text("جاري التحميل...", size=18, color=ft.Colors.GREY)

    def on_click(e):
        status.value = "تم الضغط بنجاح! 🎉"
        status.color = ft.Colors.GREEN
        page.update()

    # إضافة العناصر للصفحة
    page.add(
        ft.AppBar(title=ft.Text("اختبار"), bgcolor=ft.Colors.RED, color=ft.Colors.WHITE),
        ft.Column([
            status,
            ft.ElevatedButton("اضغط هنا", on_click=on_click, width=200, height=50)
        ], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER, expand=True)
    )
    # ⚠️ إلزامي على الأندرويد لإجبار الرسم فورًا
    page.update()

# ❌ حذف if __name__ == "__main__": تمامًا
# ✅ استدعاء مباشر في مستوى الموديول (مطلوب لمُفسّر الأندرويد)
ft.app(target=main)
