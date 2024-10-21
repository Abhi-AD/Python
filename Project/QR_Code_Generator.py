from wifi_qrcode_generator import wifi_qrcode

ssid = input("Enter the SSID (network name): ")
password = input("Enter the password: ")

# Generate the Wi-Fi QR code
qr_code = wifi_qrcode(
    ssid=ssid, hidden=False, authentication_type="WPA", password=password
)
qr_code_img = qr_code.make_image()

# Save the QR code as an image file
qr_code_img.save("wifi_qr_code.png")

print("Wi-Fi QR code has been generated and saved as wifi_qr_code.png.")
