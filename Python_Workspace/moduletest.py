import module1
import package1# to use package1 as namespace; modules are not imported
#import package1.mod1 #first method to import packages
#from package1 import mod2,mod1 #another method to import packages
#print(dir())
#import package1
print(module1.var_m1)
module1.func_m1()
print(package1.mod1.pkg_m2_var1)
print(package1.mod2.var1_m2)
