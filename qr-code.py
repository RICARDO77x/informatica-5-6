import qrcode

def main():
    song = "https://www.youtube.com/watch?v=h0p8yTqj8i4"
    qr = qrcode.QRCode(version = 1, box_size = 5, border = 5)
    qr.add_data(song)
    qr.make(fit=True)

    img = qr.make_image(fill_color="blue", back_color="white")
    img.save("my-qrcode.png")



if __name__== "__main__":
    main()

