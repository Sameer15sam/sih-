import sqlite3
import json
from datetime import datetime, timedelta

# Database file
DB_FILE = "track_fittings.db"

# Connect to SQLite
conn = sqlite3.connect(DB_FILE)
cursor = conn.cursor()

# Generate warranty expiration report
def generate_warranty_expiration_report():
    today = datetime.now()
    cutoff_date = today + timedelta(days=30)
    cursor.execute("""
    SELECT vendor_lot_number, unique_item_id, warranty_period, supply_date
    FROM track_fittings
    """
    )
    items = cursor.fetchall()
    print("Items Nearing Warranty Expiration:")
    for item in items:
        supply_date = datetime.strptime(item[3], "%Y-%m-%d")
        warranty_end_date = supply_date + timedelta(days=item[2] * 30)
        if today <= warranty_end_date <= cutoff_date:
            print(f"Item ID: {item[1]}, Vendor Lot: {item[0]}, Warranty Ends: {warranty_end_date.date()}")

# Generate inspection due report
def generate_inspection_due_report():
    today = datetime.now()
    cursor.execute("""
    SELECT unique_item_id, inspection_dates
    FROM track_fittings
    """
    )
    items = cursor.fetchall()
    print("\nItems Due for Inspection:")
    for item in items:
        inspection_dates = json.loads(item[1])
        for date in inspection_dates:
            inspection_date = datetime.strptime(date, "%Y-%m-%d")
            if today <= inspection_date <= today + timedelta(days=30):
                print(f"Item ID: {item[0]}, Inspection Due: {inspection_date.date()}")

# Generate Reports
generate_warranty_expiration_report()
generate_inspection_due_report()

# Close the connection
conn.close()