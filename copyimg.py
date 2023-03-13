import sqlite3
import shutil
from pathlib import Path

serieslist = [8, 9, 25, 45, 86, 241, 321]

imagesource = Path ("D:/trusti")
destroot = "D:/series1"
cnn = sqlite3.connect("Series230209.db")
cr = cnn.cursor()

for series in serieslist:
    series_dir, dummy= cr.execute ("select series_name, series_alias from series where series_id = ?", (str(series),) ).fetchone()
    print (series_dir)
    directory_path = Path (destroot + "/" + series_dir)
    directory_path.mkdir(parents=True, exist_ok=True)
    print (directory_path)
    films = cr.execute ("select film_name from films where series_id = ?", (str(series),)).fetchall()
    for i in films:
        film = i[0]
        for source_file in imagesource.glob(film + ".jpg"):
            shutil.copy2(source_file, directory_path)
