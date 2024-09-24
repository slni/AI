# --------  方式一 ------------
import math

print(math.pi)

# 导入并且进行重命名
import math as cutsomMath

print(cutsomMath.pi)


# --------  方式二 - 1 ------------
from mockPackage import mockMath
from mockPackage import mockPrint
print(mockMath.addValue(10, 5))
mockPrint.myPrint("hello world!")


from mockPackage import mockPrint as customPrint
customPrint.myPrint("hello world!")


# --------  方式二 - 2 ------------
from mockPackage.mockMath import addValue
from mockPackage.mockPrint import myPrint

print(addValue(20, 30))
myPrint("hello slni!")

from mockPackage.mockPrint import myPrint as myNewPrint
myNewPrint("hello slni!")