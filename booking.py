# Theatre Booking System

TOTAL_SEATS = 350
remaining_seats = TOTAL_SEATS

total_bookings = 0
tickets_sold = 0
rejected_bookings = 0

while remaining_seats > 0:
    tickets = int(input("Enter number of tickets (0 to exit): "))

    # Exit condition
    if tickets == 0:
        break

    # Validate ticket count
    if tickets < 1 or tickets > 15:
        print("BOOKING REJECTED - Invalid number of tickets (1-15 only)")
        rejected_bookings += 1
        continue

    # Check seat availability
    if tickets > remaining_seats:
        print("BOOKING REJECTED - Not enough seats available")
        rejected_bookings += 1
        continue

    ages = []
    valid_booking = True

    # Input ages
    for i in range(tickets):
        age = int(input(f"Enter age for person {i+1}: "))
        
        if age < 12:
            valid_booking = False
            # skip remaining inputs using continue logic
        ages.append(age)

    # Check age restriction
    for age in ages:
        if age < 12:
            print("BOOKING REJECTED - Age restriction")
            rejected_bookings += 1
            valid_booking = False
            break

    if not valid_booking:
        continue

    # Booking successful
    remaining_seats -= tickets
    tickets_sold += tickets
    total_bookings += 1

    print(f"BOOKING CONFIRMED - {tickets} tickets")

    # Stop if full
    if remaining_seats == 0:
        print("Theatre is now full!")
        break

# Final Report
print("\nFINAL REPORT")
print(f"Total Bookings: {total_bookings}")
print(f"Total Tickets Sold: {tickets_sold}")
print(f"Rejected Bookings: {rejected_bookings}")
print(f"Remaining Seats: {remaining_seats}")