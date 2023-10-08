print("Name : ->",__name__)
#ImportFunc.py
import ImportFunc #เป็นการนำเข้า Function ทั้งหมดที่เขียนไว้ใน ImportFunc.py
readings = [0.1, 0.4, 0.2]
print("signal threshold is ->",ImportFunc.threshold(readings))
print("Sum Number is ->",ImportFunc.sumNumber([1,2,3,4,5]))

from ImportFunc import threshold #เป็นการนำเข้า Function เฉพาะ threshold ที่เขียนไว้ใน ImportFunc.py
print("signal threshold is ->",threshold(readings))

#stats.py
from stats import avarage
print("test 4 should be None:", avarage(set()))
print("test 5 should be -1:", avarage({0, -1, -2}))

#ClassBankAccount.py <- เขียนแบบ Object
import ClassBankAccount as CBA
mrP = CBA.BankAccount("mrP", 5000)
mrP.withdraw(400)
print("mrP ->",mrP.balance)

import ClassPlayer as CP
objcPlayer = CP.Player()
objcPlayer.fName = "Sky"
objcPlayer.lName = "Blue"
objcPlayer.age = 24
print(f"Fullname is {objcPlayer.fName} {objcPlayer.lName}, {objcPlayer.age} years old")

objcPlayer2 = CP.Player2("Sea", "GrayMan", "28")
print(f"Fullname is {objcPlayer2.fName} {objcPlayer2.lName}, {objcPlayer2.age} years old")