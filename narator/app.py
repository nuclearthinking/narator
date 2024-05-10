import typer
from typer import Typer
from typing_extensions import Annotated

app = Typer()


@app.command(
    name='narrate',
    help='Start voice over over chapters',
)
def voiceover(
    book_id: Annotated[int, typer.Argument(help='Id of book to voiceover')],
    start: Annotated[int, typer.Argument(help='From what number of chapter start process of voiceover')] = 0,
):
    from narator.core.narration import narrate

    narrate(book_id=book_id, start=start)


@app.command(
    name='narrate-y',
    help='Start narration with Yandex STT engine.'
)
def voiceover_y(
    book_id: Annotated[int, typer.Argument(help='Id of book to voiceover')],
    start: Annotated[int, typer.Argument(help='From what number of chapter start process of voiceover')] = 0,
):
    from narator.core.narration import narrate_y

    narrate_y(book_id=book_id, start=start)


@app.command(
    name='export',
    help='Export chapters to mp3.',
)
def export(
    book_id: Annotated[int, typer.Argument(help='Id of book to export.')],
    start: Annotated[int, typer.Argument(help='Chapter number to start exporting dubbed chapters.')],
    step: Annotated[int, typer.Argument(help='How many chapters to export.')],
    cover: Annotated[
        str,
        typer.Option(help='Path to cover img.'),
    ] = None,
):
    from narator.core.exporter import export_chapters
    if cover is None:
        cover = 'resources/the_mech_touch_01.jpg'

    export_chapters(book_id=book_id, start=start, step=step, cover_path=cover)


@app.command(
    name='init',
    help='Initialize narator application.',
)
def init():
    from narator.storage import base

    base.initialize_db()
