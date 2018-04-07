# class
class test():    
    def nhap(self):
        self.s = input("nhap: ")
    def xuat(self):
        print self.s

a =  test()
a.nhap()
a.xuat()
#----------------------
# class InputOutString(object):
#     def __init__(self):
#         self.s = ""
#     def getString(self):
#         self.s = input("nhap:")
#         self.s = " " + self.s
# # Code by Quantrimang.com
#     def printString(self):
#         print (self.s.upper())
# strObj = InputOutString()
# strObj.getString()
# strObj.printString()	