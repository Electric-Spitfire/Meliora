# Meliora

<p align="center">
  <img src="images\Asset 1-100.jpg"/>
</p>
Yo. What's up?

This is Meliora, Pat Flan's personal assistant.

### Changelog
----
1. run_meliora.py `Changed input parsing to use regex`

2. speeches.json `migrated speeches from speeches.py to speaches.json`

3. spotify_access.py `added default device if sp.current_playback() is None`

4. vocabParse.py `restructured parsing using classes; added commands for the following 1)time 2)date 3)speeches`
[see below for all commands and their syntax](#Usage)

5. README.md `added Changelog; added Installation; added Running; added Usage;`

## Installation
----
  Clone the repository

    git clone https://github.com/dabombpat/Meliora.git

  Move into the repository directory

    cd Meliora

  Install dependencies 

    pip3 install -r requirements.txt

## Running
----
  Once installed simply run main.py

    python3 main.py

## Usage
----
### Current commands
| Commands | Syntax                                                     |
|----------|------------------------------------------------------------|
| Spotify  | play {song} OR play {song} by {artist}                     |
| Queue    | queue {song} OR queue {song} by {artist}                   |
| Time     | what is the time                                           |
| Date     | what is the date                                           |
| Inspire  | inspire me                                                 |
| TODO     | add {task} to TODO OR delete {task} from TODO OR read TODO |
