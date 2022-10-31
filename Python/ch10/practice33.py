import imp
import theater_module
theater_module.price(3)
theater_module.price_morning(4)
theater_module.price_army(5)

import theater_module as mv
mv.price(3)
mv.price_morning(4)
mv.price_army(5)

# from theater_module import *
# price(3)
# price_morning(4)
# price_army(5)

# from theater_module import price, price_army, price_morning
# price(32)
# price_morning(14)
# price_army(56)

from theater_module import price_army as price
price(1)