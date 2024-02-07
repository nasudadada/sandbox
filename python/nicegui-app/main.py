from nicegui import ui

todos = ['TODO1', 'TODO2']

with ui.header().classes(replace="row items-center") as header:
    ui.button(on_click=None, icon="menu").props("flat color=white")
    ui.label("TODOアプリ").classes('text-4xl font-bold my-4')

with ui.footer(value=False) as footer:
    ui.label("Footer")

with ui.row():
    with ui.page_sticky(position="bottom-right", x_offset=20, y_offset=20):
        ui.button(on_click=footer.toggle, icon="contact_support").props("fab")

with ui.row():
    todo_input = ui.input("TODOを入力してください").classes('w-64')
    ui.button("追加", on_click=lambda: add_todo(todo_input.value))

with ui.row():
    ui.label("Todo List").classes('text-2xl font-semibold my-2')

todo_list = ui.column()

for todo in todos:
    ui.markdown(todo)

def add_todo(todo_text):
    if todo_text:
        # 新しいTODOをUIのtodo_listに直接追加
        ui.markdown(todo_text)
        # TODOリスト配列にも追加
        todos.append(todo_text)
        # 入力フィールドをクリア
        todo_input.value = ''

# サーバを起動
ui.run()
