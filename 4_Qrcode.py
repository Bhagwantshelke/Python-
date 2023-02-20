import qrcode

# # Data to be encoded
# data = 'QR Code using make() function'
#
# # Encoding data using make() function
# img = qrcode.make(data)
#
# # Saving as an image file
# img.save('MyQRCode1.png')


# import qrcode
# user_input = input("enter a value for QR: \n")
# qr = qrcode.QRCode(    version=1,    error_correction=qrcode.constants.ERROR_CORRECT_L,    box_size=10,    border=4,)
# qr.add_data(user_input
#
# )qr.make(fit=True)
# img = qr.make_image(fill_color="black", back_color="white")
# img.save('test2.png')




import qrcode
qr = qrcode.QRCode(    version=1,
                       error_correction=qrcode.constants.ERROR_CORRECT_L,
                       box_size=10,
                       border=4,)

qr.add_data({"Name" : input("Enter your Name : "),
            "Location" : input("Enter your Location : ")
             })
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("data1.png")