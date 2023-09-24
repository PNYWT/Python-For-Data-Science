import ClassImport
readings = [0.1, 0.4, 0.2]
print("signal threshold is ->",ClassImport.threshold(readings))

from stats import avarage
print("test 4 should be None:", avarage(set()))
print("test 5 should be -1:", avarage({0, -1, -2}))

