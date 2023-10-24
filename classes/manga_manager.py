from modules.mangabat import MangaBat
from modules.mangatown import MangaTown

class MangaManger:

  def default_driver(self):
    return self.mangabat_driver()

  def mangabat_driver(self) -> MangaBat:
    return MangaBat()

  def mangatown_driver(self) -> MangaTown:
    return MangaTown()

  def driver(self, driver: str = None):
    if not driver:
      return self.default_driver()
    
    try:
      return getattr(self, f"{driver.lower()}_driver")()
    except:
      return self.default_driver()
    