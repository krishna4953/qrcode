import qrcode
from PIL import Image

# Create a QRCode instance
qr = qrcode.QRCode(
    version=15,  # The size of the QR code (larger version for more data)
    box_size=10,  # Size of each box in the QR code
    border=5      # Width of the border
)

# Data that you want to embed into the QR code
data = "https://www.example.com"  # URL of the HTML page

# Add the data to the QR code
qr.add_data(data)
qr.make(fit=True)

# Create the QR code image with black fill and white background
img = qr.make_image(fill="black", back_color="white")

# Save the image as a PNG file
img.save("test.png")
