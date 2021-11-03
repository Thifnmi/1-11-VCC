from utils.util import house, require
import sys
sys.path.append("..")


test = require(house, ["tu van thin", "nguyen duc thien",
               "vu trong dat"], "dau tuan duong")
print(test)
