import qrcode

def generate_qr_code(data, filename="my_qrcode.png", box_size=10, border=4):
    qr = qrcode.QRCode(
        version=1,  
        error_correction=qrcode.constants.ERROR_CORRECT_L,  
        box_size=box_size,  
        border=border,  
    )
    
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    img.save(filename)
    print(f"QR code saved as '{filename}'")

if __name__ == "__main__":
    user_input = input("Enter the text or URL to encode in the QR code: ")
    file_name = input("Enter the filename to save (default: my_qrcode.png): ").strip()
    if not file_name:
        file_name = "my_qrcode.png"
    generate_qr_code(user_input, filename=file_name)
