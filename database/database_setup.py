import sqlite3
import json

# Database file
DB_FILE = "track_fittings.db"

# Connect to SQLite
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS track_fittings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    vendor_lot_number TEXT,
    supply_date TEXT,
    warranty_period INTEGER,
    inspection_dates TEXT,
    fitting_type TEXT,
    unique_item_id TEXT UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

# Insert data into the database
def insert_qr_data(qr_data):
    try:
        data = json.loads(qr_data)
        cursor.execute("""
        INSERT INTO track_fittings (vendor_lot_number, supply_date, warranty_period, inspection_dates, fitting_type, unique_item_id)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data["vendor_lot_number"],
            data["supply_date"],
            data["warranty_period"],
            json.dumps(data["inspection_dates"]),
            data["fitting_type"],
            data["unique_item_id"]
        ))
        conn.commit()
        print(f"Data for {data['unique_item_id']} inserted successfully.")
    except sqlite3.IntegrityError:
        print(f"Item with unique_item_id {data['unique_item_id']} already exists.")

# Example: Insert sample QR code data
sample_qr_data = """
{
    "vendor_lot_number": "ABC123",
    "supply_date": "2025-09-01",
    "warranty_period": 36,
    "inspection_dates": ["2025-12-01", "2026-06-01"],
    "fitting_type": "Elastic Rail Clip",
    "unique_item_id": "ERC001"
}
"""
insert_qr_data(sample_qr_data)

# Close the connection
conn.close()