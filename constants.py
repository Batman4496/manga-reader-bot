import modules.mangabat as mangabat
import modules.mangatown as mangatown


sources = {
  'MangaBat': {
    'm': mangabat.MangaBat,
    'description': 'MangaBat WTF'
  },
  'MangaTown': {
    'm': mangatown.MangaTown,
    'description': 'MangaTown WTF'
  },

}

CHOICES = [k for k in sources.keys()]


COGS = [
  'manga.search',
  'manga.hot',
  'manga.read',
  'help'
]


