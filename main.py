import flet

piece = "img/circle.jpg"

def main(page: flet.Page):
    page.title = "Tic Tac Toe with Flet"
    page.theme_mode = flet.ThemeMode.DARK
    page.padding = 50
    page.update()

    grade = flet.GridView(
        expand=1,
        runs_count=5,
        max_extent=150,
        child_aspect_ratio=1.0,
        spacing=12,
        run_spacing=12,
    )      

    page.add(grade)
    page.window_width = 600
    page.window_height = 625

    def switch(piece: str):
        piece
        if piece == "img/circle.jpg":
            piece = "img/mark.jpg"
        else:
            piece = "img/circle.jpg"
        return piece

    def clicou(e):
        print("clicou", e.control.data)
        if grade.controls[e.control.data].content.src != f"img/none.jpg":
            print("(Recusado) clicou", e.control.data)
            return
        global piece
        grade.controls[e.control.data].content.src = piece
        piece = switch(piece)
        grade.controls[e.control.data].content.update()

    for i in range(0, 9):
        grade.controls.append(
            flet.Container(
                alignment=flet.alignment.center,
                width=150,
                height=150,
                border_radius=10,
                ink=True,
                data=i,
                on_click=lambda e: clicou(e),
                content=flet.Image(
                    src=f"img/none.jpg",
                    # src=f"img/circle.jpg",
                    # src=f"img/mark.jpg",
                    fit=flet.ImageFit.NONE,
                    repeat=flet.ImageRepeat.NO_REPEAT,
                    border_radius=flet.border_radius.all(11),
                ),
        ))
    page.update()

flet.app(target=main, view=flet.WEB_BROWSER)