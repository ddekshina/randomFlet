import flet as ft

def main(page: ft.page):

    def addTask(p):
        checkBox= ft.Checkbox(value=False,check_color="white", fill_color="#F875AA")
        checkBoxText = ft.Text(value= textField.value,width=350,color="black", size="18")
        taskRow=ft.Row(controls=[checkBox,checkBoxText],alignment=ft.MainAxisAlignment.START)
        page.add(taskRow)

    
    
    page.window_width = 500
    page.window_height = 600
    page.bgcolor= "#FFF6F6"
    textField = ft.TextField(width=350,color="black")
    addBtn = ft.FloatingActionButton(icon=ft.icons.ADD,bgcolor="#F875AA",on_click=addTask)
      
    entriesRow=ft.Row(controls=[textField,addBtn] , alignment=ft.MainAxisAlignment.SPACE_AROUND)
    
    page.add(entriesRow)

ft.app(target=main)