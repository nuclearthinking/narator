import typer
from typer import Typer
from typing_extensions import Annotated

app = Typer()


@app.command(
    name='voiceover',
    help='Start voice over over chapters',
)
def voiceover(
    book_id: Annotated[int, typer.Argument(help='Id of book to voiceover')],
    start: Annotated[int, typer.Argument(help='From what number of chapter start process of voiceover')],
):
    from narator.core.dubbing import start_voiceover

    start_voiceover(book_id=book_id, start=start)


@app.command(
    name='export',
    help='Export chapters to mp3',
)
def export(
    book_id: Annotated[int, typer.Argument(help='Id of book to export.')],
    start: Annotated[int, typer.Argument(help='Chapter number to start exporting dubbed chapters.')],
    step: Annotated[int, typer.Argument(help='How many chapters to export.')],
):
    from narator.core.exporter import export_chapters

    export_chapters(book_id=book_id, start=start, step=step)
