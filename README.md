# Allow to narrate your favorite stories and make audio-books from text stories.

```bash
# you need to have poetry package manager installed
poetry install  # to install dependancies

narator --help # to check is application installed correctly
# if everything installed corectly command will show list of available commands
```

```bash
narator init # initialize database for application
```

## Fill database with your stories. 

fill database using any familiar tool, by default database file is `narator.db`
database structure is easy and intuitive

- add book to `books` table
- add chapters to `chapters` table

## Narrate your favourite stories 
```bash
# narrate books using command
narator narrate <book_id> <start_chapter>
```
after process completed you now can export result to mp3 file with following command
```bash
# export narrated book 
narator export <book_id> <start_chapter> <amount_of_chapters_per_file> --cover=<path_to_cover_img>
```