import qrcode
msg = input("Enter your message Here: ")

img = qrcode.make(msg)
type(img) 
img.save("students.png")

print("Qr Code Gen...")