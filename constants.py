import modules.mangabat as mangabat
import modules.mangatown as mangatown

BONEMAN = 459250601314746375

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
  'miner.miner',
  'help'
]


