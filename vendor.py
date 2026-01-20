vendor_name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

annual_purchase = 0

print("\nEnter monthly purchases:")
for month in range(1, 13):
    purchase = float(input(f"Month {month} purchase amount: "))
    annual_purchase += purchase

print("\n--- Vendor Annual Billing Report ---")
print("Vendor Name:", vendor_name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("Total Annual Purchase:", annual_purchase)