from constants import DRIVERS, DEFAULT_DRIVER

class MangaManger:

  def driver(self, driver: str = None):
    if not driver:
      return DEFAULT_DRIVER()
    
    try:
      return DRIVERS.get(driver).get('module')()
    except:
      return DEFAULT_DRIVER()
    