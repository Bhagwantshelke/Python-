# a = int(input("Enter number: "))
# b = int(input("Enter Number: "))
#
# def calculator(a):
#     print(a)
# calculator((lambda a,b : a + b)(a,b))
# calculator((lambda a,b : a - b)(a,b))
# calculator((lambda a,b : a / b)(a,b))
# calculator((lambda a,b : a * b)(a,b))
#

import qrcode

# Data to be encoded
data = 'QR Code using make() function'

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('MyQRCode1.png')


