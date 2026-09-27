
# ============================================================
# MOVIES LIST
# ============================================================

movies = ["Avengers", "Harry potter", "Don no. 1", "Bahubali"]

user_ID = "kartik"
password = "26bai10193"

# Store booked seats
Booked_seats = []


# ============================================================
# MANAGE MOVIES
# ============================================================

def Manage_Movies():

    # Log In System
    print("=====Log In=====")

    ID = input("Enter User ID: ")
    passcode = input("Enter password: ")

    if ID == user_ID and passcode == password:

        print("Welcome sir!")

        while True:

            print("== Main Menu ==")
            print("1. Add Movie")
            print("2. Remove Movie")
            print("3. View Movie")
            print("4. Log Out")

            change = input("Enter the command: ")

            # ADD MOVIE
            if change == "1":

                movie_name = input("Enter movie Name: ")

                movies.append(movie_name)

                print(movies)
                print("Movie Added Successfully!")

            # REMOVE MOVIE
            elif change == "2":

                movie_name_remove = input("Enter movie name: ")

                if movie_name_remove in movies:

                    movies.remove(movie_name_remove)

                    print(movies)
                    print("Movie Removed Successfully!")

                else:

                    print("Movie Not Found!")

            # VIEW MOVIE
            elif change == "3":

                if len(movies) == 0:

                    print("No movie is available")
                    print("Add movies")

                else:

                    print(movies)

            # LOG OUT
            elif change == "4":

                print("LOGGED OUT")
                print("THANK YOU SIR!")

                break

            else:

                print("Invalid Choice!")
                print("Try Again!")

    else:

        print("Incorrect ID or Password")
        print("Try Again!")


# ============================================================
# BOOKING FUNCTION
# ============================================================

def Booking():

    if len(movies) == 0:

        print("No movies are available!")
        print("Please add movies first.")

        return

    while True:

        print("========================================")
        print("   WELCOME TO PYCINEMA BOOKING SYSTEM")
        print("========================================")

        print(movies)

        # ====================================================
        # STEP 2 — STORE TICKET PRICES (DICTIONARY)
        # ====================================================

        ticket_prices = {
            "Adult": 800,
            "Student": 600,
            "Child": 500
        }

        # ====================================================
        # STEP 3 — STORE TICKET TYPES (TUPLE)
        # ====================================================

        ticket_types = ("Adult", "Student", "Child")

        # ====================================================
        # STEP 4 — DISPLAY AVAILABLE MOVIES
        # ====================================================

        print("\nAvailable Movies:")

        for i in range(len(movies)):

            print(str(i + 1) + ". " + movies[i])

        # ====================================================
        # STEP 5 & 6 — SELECT MOVIE + VALIDATE
        # ====================================================

        while True:

            try:

                movie_choice = int(input("\nChoose a movie: "))

                if movie_choice >= 1 and movie_choice <= len(movies):

                    break

                else:

                    print(
                        "Invalid movie choice! "
                        "Please select a valid movie."
                    )

            except ValueError:

                print("Please enter a valid number!")

        selected_movie = movies[movie_choice - 1]

        print("You selected:", selected_movie)

        # ====================================================
        # STEP 7 — DISPLAY TICKET PRICES
        # ====================================================

        print("\nTicket Prices:")

        for ticket_type in ticket_types:

            print(
                ticket_type,
                ": Rs.",
                ticket_prices[ticket_type]
            )

        # ====================================================
        # STEP 8-12 — TICKET COUNTS + VALIDATE
        # ====================================================

        valid_order = False

        while not valid_order:

            # ADULT TICKETS
            while True:

                try:

                    adult_tickets = int(
                        input("\nEnter number of Adult tickets: ")
                    )

                    if adult_tickets >= 0:

                        break

                    else:

                        print(
                            "Number of tickets cannot be negative."
                        )

                except ValueError:

                    print("Please enter a valid number!")

            # STUDENT TICKETS
            while True:

                try:

                    student_tickets = int(
                        input("Enter number of Student tickets: ")
                    )

                    if student_tickets >= 0:

                        break

                    else:

                        print(
                            "Number of tickets cannot be negative."
                        )

                except ValueError:

                    print("Please enter a valid number!")

            # CHILD TICKETS
            while True:

                try:

                    child_tickets = int(
                        input("Enter number of Child tickets: ")
                    )

                    if child_tickets >= 0:

                        break

                    else:

                        print(
                            "Number of tickets cannot be negative."
                        )

                except ValueError:

                    print("Please enter a valid number!")

            total_tickets = (
                adult_tickets
                + student_tickets
                + child_tickets
            )

            if total_tickets == 0:

                print(
                    "You must purchase at least one ticket."
                )

            else:

                valid_order = True

        # ====================================================
        # STEP 13-16 — CALCULATE COSTS AND SUBTOTAL
        # ====================================================

        adult_cost = (
            adult_tickets * ticket_prices["Adult"]
        )

        student_cost = (
            student_tickets * ticket_prices["Student"]
        )

        child_cost = (
            child_tickets * ticket_prices["Child"]
        )

        subtotal = (
            adult_cost
            + student_cost
            + child_cost
        )

        # ====================================================
        # STEP 17-18 — STUDENT DISCOUNT
        # ====================================================

        if student_tickets >= 2:

            student_discount = student_cost * 0.10

        else:

            student_discount = 0

        after_student_discount = (
            subtotal - student_discount
        )

        # ====================================================
        # STEP 19-20 — GROUP DISCOUNT + FINAL TOTAL
        # ====================================================

        if total_tickets >= 5:

            group_discount = (
                after_student_discount * 0.05
            )

        else:

            group_discount = 0

        final_total = (
            after_student_discount - group_discount
        )

        # ====================================================
        # STEP 21 — SEAT BOOKING
        # ====================================================

        Total_seats = [

            "A1", "A2", "A3", "A4", "A5",
            "A6", "A7", "A8", "A9", "A10",

            "B1", "B2", "B3", "B4", "B5",
            "B6", "B7", "B8", "B9", "B10",

            "C1", "C2", "C3", "C4", "C5",
            "C6", "C7", "C8", "C9", "C10",

            "D1", "D2", "D3", "D4", "D5",
            "D6", "D7", "D8", "D9", "D10",

            "E1", "E2", "E3", "E4", "E5",
            "E6", "E7", "E8", "E9", "E10",

            "F1", "F2", "F3", "F4", "F5",
            "F6", "F7", "F8", "F9", "F10",

            "G1", "G2", "G3", "G4", "G5",
            "G6", "G7", "G8", "G9", "G10",

            "H1", "H2", "H3", "H4", "H5",
            "H6", "H7", "H8", "H9", "H10",

            "I1", "I2", "I3", "I4", "I5",
            "I6", "I7", "I8", "I9", "I10",

            "J1", "J2", "J3", "J4", "J5",
            "J6", "J7", "J8", "J9", "J10"

        ]

        # DISPLAY AVAILABLE SEATS

        available_seats = [
            seat for seat in Total_seats
            if seat not in Booked_seats
        ]

        print("\n========================================")
        print("          AVAILABLE SEATS")
        print("========================================")

        for i in range(0, len(Total_seats), 10):

            for seat in Total_seats[i:i + 10]:

                if seat in Booked_seats:

                    print("[X]", end=" ")

                else:

                    print("[" + seat + "]", end=" ")

            print()

        print("========================================")
        print("[X] = BOOKED SEAT")
        print("========================================")

        # CHECK WHETHER ENOUGH SEATS ARE AVAILABLE

        if len(available_seats) < total_tickets:

            print("Not enough seats are available!")
            print("Please select fewer tickets.")

            return

        # SELECT SEATS ACCORDING TO TICKET QUANTITY

        Seats = []

        for i in range(total_tickets):

            while True:

                seat_choice = input(
                    "Enter seat number for ticket "
                    + str(i + 1) + ": "
                ).upper().strip()

                if seat_choice not in Total_seats:

                    print("Invalid seat number!")
                    print("Please select a valid seat.")

                elif seat_choice in Booked_seats:

                    print("Seat is already occupied!")
                    print("Enter a different seat number.")

                elif seat_choice in Seats:

                    print("You already selected this seat!")
                    print("Choose a different seat.")

                else:

                    Seats.append(seat_choice)

                    break

        # ADD SELECTED SEATS TO BOOKED SEATS

        Booked_seats.extend(Seats)

        print("\nSelected Seats:", Seats)
        print("Seats booked successfully!")

        # ====================================================
        # STEP 22 — PRINT BOOKING RECEIPT
        # ====================================================

        print("\n========================================")
        print("           BOOKING SUMMARY")
        print("========================================")

        print("Movie:", selected_movie)

        print(
            "Adult Tickets:",
            adult_tickets,
            "x Rs.",
            ticket_prices["Adult"],
            "= Rs.",
            adult_cost
        )

        print(
            "Student Tickets:",
            student_tickets,
            "x Rs.",
            ticket_prices["Student"],
            "= Rs.",
            student_cost
        )

        print(
            "Child Tickets:",
            child_tickets,
            "x Rs.",
            ticket_prices["Child"],
            "= Rs.",
            child_cost
        )

        print("----------------------------------------")

        print("Total Tickets:", total_tickets)

        print("Selected Seats:", ", ".join(Seats))

        print("Subtotal: Rs.", subtotal)

        print(
            "Student Discount: Rs.",
            student_discount
        )

        print(
            "After Student Discount: Rs.",
            after_student_discount
        )

        print("Group Discount: Rs.", group_discount)

        print("----------------------------------------")

        print(
            "FINAL TOTAL: Rs.",
            round(final_total, 2)
        )

        print("========================================")
        print("BOOKING SUCCESSFUL")
        print("Enjoy your movie!")
        print("========================================")

        # ====================================================
        # STEP 23 — BOOKING MENU
        # ====================================================

        print("\n1. Book Another Ticket")
        print("2. Return to Main Menu")

        booking_choice = input("Enter your choice: ")

        if booking_choice == "2":

            print("Returning to Main Menu...")

            break

        elif booking_choice == "1":

            continue

        else:

            print("Invalid Choice!")
            print("Returning to Main Menu...")

            break


# ============================================================
# MAIN MENU
# ============================================================

while True:

    print("=====================")
    print("      Main Menu      ")
    print("=====================")

    print("1. Manage Movies")
    print("2. Booking Ticket")
    print("3. Log Out")

    choice = input("Enter your choice: ")

    if choice == "1":

        Manage_Movies()

    elif choice == "2":

        Booking()

    elif choice == "3":

        print("Logged Out!")
        print("Thank you!")

        break

    else:

        print("Invalid Choice!")
        print("Try Again!")



        