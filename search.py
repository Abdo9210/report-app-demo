reports = ["sales report", "inventory report", "employee report"]
action = "search"
match action:
case "search":
keyword = "sales"
found = False
for report in reports:
if keyword.lower() in report.lower():
print(f"Report found: {report}")
found = True
if not found:
print("No report matched the keyword.")

case "export":
print("Exporting report as PDF...")

case _:
print("Invalid action selected.")
