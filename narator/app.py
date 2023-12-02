import typer
from typer import Typer
from typing_extensions import Annotated

from narator.core.dubbing import start_voiceover

app = Typer(name='narator')


@app.command(
    name='voiceover',
    help='Start voice over over chapters',
)
def voiceover(
    book_id: Annotated[int, typer.Argument(help='Id of book to voiceover')],
    chapter_number: Annotated[int, typer.Argument(help='From what number of chapter start process of voiceover')],
):
    start_voiceover(book_id, chapter_number)
