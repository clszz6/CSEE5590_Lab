# Creates a person object
class Person:
    # INIT
    def __init__(self, name):
        self.__name = name # name of the person PRIVATE DATA MEMBER

    def get_name(self):
        return self.__name


# Creates an employee for the airline company, CLASS 1
class Employee(Person):
    # INIT
    def __init__(self, name, employee_id):
        super(Employee, self).__init__(name)
        self.employee_id = employee_id # id of the employee


# Creates a license for the pilot, CLASS 2
class License:
    # INIT
    def __init__(self, pilot_license_number, expiration):
        self.pilot_license_number = pilot_license_number # legal representation representing the pilot
        self.expiration = expiration # expiration date of the pilot license

    def get_license(self):
        return self.pilot_license_number


# Creates a pilot to fly the airplane, INHERITANCE AND MULTIPLE INHERITANCE, CLASS 3
class Pilot(Employee, License):
    # INIT
    def __init__(self, name, employee_id, pilot_license_number, expiration):
        Employee.__init__(self, name, employee_id)
        License.__init__(self, pilot_license_number, expiration)
        self.plane_piloting = None

    def set_plane_piloting(self, plane_piloting):
        self.plane_piloting = plane_piloting

    def display_pilot_info(self):
        print(self.get_name(), self.get_license())


# Creates a passenger for the flights, CLASS 4
class Passenger(Person):
    # INIT
    def __init__(self, name, confirmation_number):
        # SUPER CALL
        super(Passenger, self).__init__(name)
        # SELF
        self.confirmation_number = confirmation_number

    def display_passenger_info(self):
        print(self.get_name(), self.confirmation_number)


# Creates flights that the passengers will sign up for, CLASS 5
class Flight:
    # INIT
    def __init__(self, airline, gate, destination):
        self.airline = airline
        self.gate = gate
        self.destination = destination
        self.pilot = None
        self.passengers = []
        self.passengers_allowed = 5

    def add_passengers(self, passenger):
        self.passengers.append(passenger)

    def add_pilot(self, pilot):
        self.pilot = pilot

    def display_flight_information(self):
        print(self.airline, "\t\t", self.gate, "\t\t", self.destination, "\n")

    def display_final_information(self):
        print(self.pilot.display_pilot_info())


# Engine for the Airline Booking Reservation System. Controls booking the flights.
def airline_booking_reservation_system():
    # Initialize the pilots and the flights for booking
    pilots = initialize_pilots()
    flights = initialize_flights()

    # Present flight information for the potential passengers
    print("Welcome to the Airline Booking Reservation System\n\n",
          "We have", len(flights), "flights available\n")

    for flight in flights:
        flight.display_flight_information()

    print("\n--------------------------------\n\n")

    # Determine if passenger wants to book any flights
    user_input = input("Would you like to add any passengers to our flights (y/n): ")
    if user_input == "y":
        is_user_exiting = False
    else:
        is_user_exiting = True

    # keep count of how many iterations for the loop
    count = 1

    # Obtain passenger information to book flights
    while is_user_exiting == False:
        name = input("Enter the passengers name: ")
        destination = input("Enter the destination (1) for New York City, (2) for Las Vegas: ")

        if destination == "1":
            flights[0].add_passengers(Passenger(name, count))
        else:
            flights[1].add_passengers(Passenger(name, count))

        user_input = input("Would you like to add more passengers to our flights (y/n): ")
        if user_input == "y":
            is_user_exiting = False
        else:
            is_user_exiting = True

        count += 1

    # Book pilot to the flight
    flights[0].add_pilot(pilots[0])
    flights[1].add_pilot(pilots[1])

    # Print final flight information
    print("\nFinal flight information\n\n--------------------------------\n\n")
    for flight in flights:
        flight.display_flight_information()
        print("Pilot/CoPilot")
        flight.display_final_information()
        print("\nPassenger Information")

        for passenger in flight.passengers:
            passenger.display_passenger_info()

        print("\n")


# Initialize the pilots available for the flights
def initialize_pilots():
    pilots = []
    pilot1 = Pilot("John", 88242, "sw9988", "Jan-2-2020")
    pilot2 = Pilot("Jim", 88243, "sw9989", "Jan-2-2020")
    pilots.append(pilot1)
    pilots.append(pilot2)

    return pilots


# Initialize the flights available
def initialize_flights():
    flights = []
    flight1 = Flight("SouthWest", "Gate1", "New York City, NY")
    flight2 = Flight("American", "Gate2", "Las Vegas, NV")
    flights.append(flight1)
    flights.append(flight2)

    return flights


def main():
    airline_booking_reservation_system()


main()
