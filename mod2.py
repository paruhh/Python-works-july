import mod1    ## importing some attributes according to user need
mod1.add(2,6)

from mod1 import *    ##   * used for importing all attributes
add(10,20)
sub(2,9)

import mod1 as m    ## aliasing - changing module name for call as small words
m.add(2,8)

from mod1 import sub as s  ### changing function name for calling with simple or easy
s(10,5)

