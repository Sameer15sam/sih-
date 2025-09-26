import cv2
from pyzbar.pyzbar import decode
import json

# Path to QR code image to scan
qr_code_image_path = "qr_codes/ERC001.png"

# Load the image
image = cv2.imread(qr_code_image_path)

# Decode the QR code
decoded_objects = decode(image)
if decoded_objects:
    for obj in decoded_objects:
        qr_data = obj.data.decode("utf-8")
        print("Decoded QR Code Data:")
        print(json.dumps(json.loads(qr_data), indent=4))
else:
    print("No QR code found in the image.")

# Display the image (optional)
cv2.imshow("QR Code", image)
cv2.waitKey(0)
cv2.destroyAllWindows()