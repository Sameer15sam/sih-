import qrcode
import json
import os

# Directory to save generated QR codes
QR_CODE_DIR = "qr_codes"

# Ensure the directory exists
if not os.path.exists(QR_CODE_DIR):
    os.makedirs(QR_CODE_DIR)

# Sample Data for QR Code
items = [
    {
        "vendor_lot_number": "ABC123",
        "supply_date": "2025-09-01",
        "warranty_period": 36,
        "inspection_dates": ["2025-12-01", "2026-06-01"],
        "fitting_type": "Elastic Rail Clip",
        "unique_item_id": "ERC001"
    },
    {
        "vendor_lot_number": "DEF456",
        "supply_date": "2025-09-05",
        "warranty_period": 24,
        "inspection_dates": ["2026-01-01", "2026-07-01"],
        "fitting_type": "Rail Pad",
        "unique_item_id": "RP002"
    }
]

# Generate QR Codes
for item in items:
    unique_id = item["unique_item_id"]
    qr_data = json.dumps(item)
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    # Save QR Code as PNG
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(os.path.join(QR_CODE_DIR, f"{unique_id}.png"))

print(f"QR Codes generated and saved in `{QR_CODE_DIR}` directory.")