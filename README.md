# Manga Bot

A simple bot written in python.

# Commands


1. /hot: Get hot mangas from available sources.

![Hot Mangas](./assets/hot.png)

2. /read: Read a manga from source.
![Read Mangas](./assets/read.png)

3. /search: Search manga from the sources
![Search Mangas](./assets/search.png)


# Sources

Currently supports the following sources:

    1. MangaBat: https://readmangabat.com
    2. MangaTown: https://m.mangatown.com  

# How to contribute

First you must create a scrapper driver in `modules` directory. You can look at the existing drivers (i.e. `modules/mangabat.py`).

Next. register the driver in `constants.py` in `sources` variable.

Thanks ✌️!!