# dateconvert.py
# Converts a date in form "mm/dd/yyyy" to 'month day, year'

def main():
    #get the date
    dateStr = input("Enter a date (mm/dd/yyyy): ")

    # split into components
    monthStr, dayStr, yearStr = dateStr.split("/")

    #convert monthStr to the month name
    months = ["January", "Febrary", "March", "April", "May", "June", "July", "August", "September", "Octuber", "November", "December"]

    monthStr = months[int(monthStr) - 1]

    # output result in month day, year format
    print(f"The converted date is:  {monthStr} {dayStr} , {yearStr}")

main() 

