# Allows to narrate your favorite stories.

## Installation
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

Currently available parsers for readnovelfull com, fb2 top sites.
To initiate parsing process use following command. 
```bash
narator parse <mode> <book_id> <book_name> <language> <start_url>
```
EXAMPLE
```bash
narator parse readnovelfull 5 "Martial world" "en" "https://readnovelfull.com/martial-world.html"
```
This will create Book entity in database and fill it with Chapters content from selected site.

## Narrate your favourite stories 
```bash
# narrate books using command
narator narrate <book_id> <start_chapter>
```
After process completed you now can export result to mp3 file with following command.
```bash
# export narrated book 
narator export <book_id> <start_chapter> <amount_of_chapters_per_file> --cover=<path_to_cover_img>
```

### All commands supports `help` option.
```bash 
narator parse --help
```
