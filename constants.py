import drivers.mangabat as mangabat
import drivers.mangatown as mangatown


DRIVERS = {
  'MangaBat': {
    'driver': mangabat.MangaBat,
    'description': 'MangaBat: https://readmangabat.com'
  },
  'MangaTown': {
    'driver': mangatown.MangaTown,
    'description': 'MangaTown: https://m.mangatown.com'
  },

}

DEFAULT_DRIVER = mangabat.MangaBat

CHOICES = [k for k in DRIVERS.keys()]


COGS = [
  'manga.search',
  'manga.hot',
  'manga.read',
  'help'
]


