from abc import ABC, abstractmethod
from datetime import datetime, timedelta

class Foglalas:
    @staticmethod
    def is_available(room_bookings, check_in_date, check_out_date):
        for booking in room_bookings:
            if check_in_date < booking['check_out'] and check_out_date > booking['check_in']:
                return False
        return True

    @staticmethod
    def book_room(room_bookings, check_in_date, check_out_date, num_guests):
        if Foglalas.is_available(room_bookings, check_in_date, check_out_date):
            room_bookings.append({
                'check_in': check_in_date,
                'check_out': check_out_date,
                'num_guests': num_guests
            })
            print(f"Room booked from {check_in_date} to {check_out_date} for {num_guests} guests.")
            return True
        else:
            print("Booking failed. Room is not available for the specified dates.")
            return False
        
    @staticmethod
    def delete_booking(room_bookings, check_in_date, check_out_date):
        for booking in room_bookings:
            if booking['check_in'] == check_in_date and booking['check_out'] == check_out_date:
                room_bookings.remove(booking)
                print(f"Booking from {check_in_date} to {check_out_date} deleted.")
                return True
        print("Booking not found for the specified dates.")
        return False
    
    @staticmethod
    def list_bookings(room_bookings):
        print("All bookings for this room:")
        for booking in room_bookings:
            print(f"Check-in: {booking['check_in']}, Check-out: {booking['check_out']}, Guests: {booking['num_guests']}")

class Room(ABC):
    def __init__(self, room_number, capacity, rate):
        self._room_number = room_number
        self._capacity = capacity
        self._rate = rate
        self.bookings = []

    @property
    def occupancy(self): # foglalhatosag
        return self._occupancy
    
    @property
    def room_number(self):
        return self._room_number
    
    @property
    def rate(self):
        return self._rate
    
    @property
    def capacity(self):
        return self._capacity

    @abstractmethod
    def display_info(self):
        pass
    
    @abstractmethod
    def book_room(self, num_guests):
        pass

    @abstractmethod
    def is_available(self, check_in_date, check_out_date):
        pass

class EgyagyasSzoba(Room):
    def __init__(self, room_number):
        super().__init__(room_number, capacity=1, rate=100)
    
    def display_info(self):
        print(f"Single Bed Room {self.room_number} - Capacity: {self.capacity}, Rate: EUR {self.rate} per night")

    def book_room(self, check_in_date, check_out_date, num_guests):
        if num_guests > 1:
            raise "Booking Error. Single Bed Room"
        return Foglalas.book_room(self.bookings, check_in_date, check_out_date, num_guests)

    def is_available(self, check_in_date, check_out_date):
        return Foglalas.is_available(self.bookings, check_in_date, check_out_date)
    
    def delete_booking(self, check_in_date, check_out_date):
        return Foglalas.delete_booking(self.bookings, check_in_date, check_out_date)
    
    def list_bookings(self):
        Foglalas.list_bookings(self.bookings)

class KetagyasSzoba(Room):
    def __init__(self, room_number):
        super().__init__(room_number, capacity=2, rate=200)

    def display_info(self):
        print(f"Two Bed Room {self.room_number} - Capacity: {self.capacity}, Rate: EUR {self.rate} per night")

    def book_room(self, check_in_date, check_out_date, num_guests):
        if num_guests > 2:
            raise "Booking Error. Double Bed Room"
        return Foglalas.book_room(self.bookings, check_in_date, check_out_date, num_guests)

    def is_available(self, check_in_date, check_out_date):
        return Foglalas.is_available(self.bookings, check_in_date, check_out_date)
    
    def delete_booking(self, check_in_date, check_out_date):
        return Foglalas.delete_booking(self.bookings, check_in_date, check_out_date)
    
    def list_bookings(self):
        Foglalas.list_bookings(self.bookings)
    
class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def hotel_info(self):
        print(self.name)
        for room in self.rooms:
            print(f"{room.display_info()}")

    def get_room_by_number(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

def display_menu(hotel_name):
    print(f"\nWelcome to {hotel_name}")
    print("1. Foglalas")
    print("2. Lemondas")
    print("3. Listazas - hotel info")
    print("4. Exit")



def main():
    hotel = Hotel(name="Gabor Denes Hotel")
 
    check_in = datetime.now()
    check_out = check_in + timedelta(days=3)

    single_bed = int(input("Single bed booking. Please give a room no: ")) #100
    single_bed_room0 = EgyagyasSzoba(room_number=single_bed) 
    single_bed_room = EgyagyasSzoba(room_number=101)
    two_bed_room = KetagyasSzoba(room_number=102)

    hotel.add_room(single_bed_room0)
    hotel.add_room(single_bed_room)
    hotel.add_room(two_bed_room)

    single_bed_room0.book_room(check_in, check_out, 1) 
   # single_bed_room.book_room(check_in, check_out, 3)  # It should fail.   
    two_bed_room.book_room(check_in, check_out, 2)  

    hotel.hotel_info()
    print(f"Room no {single_bed_room0.room_number}, Type: Single")
    single_bed_room0.list_bookings()
    print(f"Room no {two_bed_room.room_number}, Type: Double")
    two_bed_room.list_bookings()
    print("Delte bookings")
    single_bed_room0.delete_booking(check_in, check_out)

    # user interface
    while True:
        display_menu(hotel.name)
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            room_number = input("Enter room number: ")
            check_in = datetime.strptime(input("Enter check-in date (YYYY-MM-DD): "), "%Y-%m-%d")
            check_out = datetime.strptime(input("Enter check-out date (YYYY-MM-DD): "), "%Y-%m-%d")
            num_guests = int(input("Enter the number of guests: "))
            room_type = input("Please give the room tpye (single/double):")

            try:
                if check_out > check_in:
                    if room_type == 'single':
                        single_bed_room_booking = EgyagyasSzoba(room_number=room_number) 
                        hotel.add_room(single_bed_room_booking)
                        single_bed_room_booking.book_room(check_in, check_out, num_guests) 
                        print("Booking successful!")
                    elif room_type == 'double':
                        double_bed_room_booking = KetagyasSzoba(room_number=room_number) 
                        hotel.add_room(double_bed_room_booking)
                        double_bed_room_booking.book_room(check_in, check_out, num_guests) 
                        print("Booking successful!")
                else:
                    print("Date error")
            except ValueError as e:
                print(e)
        elif choice == '2':
            room_number = input("Enter room number: ")
            check_in = datetime.strptime(input("Enter check-in date (YYYY-MM-DD): "), "%Y-%m-%d")
            check_out = datetime.strptime(input("Enter check-out date (YYYY-MM-DD): "), "%Y-%m-%d")

            room = hotel.get_room_by_number(room_number)
            if room:
                room.delete_booking(check_in, check_out)
                print("Booking is deleted")
            else:
                print("Room is not found")

        elif choice == '3':
            hotel.hotel_info()
        
        elif choice == '4':
            print("Exiting the Booking System. Thank you!")
            break



if __name__ == "__main__":
    main()
 