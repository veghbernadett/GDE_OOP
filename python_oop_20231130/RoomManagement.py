from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, room_number, capacity, rate):
        self._room_number = room_number
        self._capacity = capacity
        self._rate = rate
        self.is_booked = False

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

class EgyagyasSzoba(Room):
    def __init__(self, room_number):
        super().__init__(room_number, capacity=1, rate=100)
    
    def display_info(self):
        print(f"Single Bed Room {self.room_number} - Capacity: {self.capacity}, Rate: EUR {self.rate} per night")

    def book_room(self, num_guests):
        if not self.is_booked and num_guests == 1:
            self.is_booked = True
            print(f"Single Bed Room {self.room_number} booked for 1 guest.")
            return True
        elif self.is_booked:
            print(f"Single Bed Room {self.room_number} is already booked.")
        else:
            print(f"Booking failed. Single Bed Room {self.room_number} is for 1 guest only.")
        return False
    
class KetagyasSzoba(Room):
    def __init__(self, room_number):
        super().__init__(room_number, capacity=2, rate=200)

    def display_info(self):
        print(f"Two Bed Room {self.room_number} - Capacity: {self.capacity}, Rate: EUR {self.rate} per night")

    def book_room(self, num_guests):
        if not self.is_booked and num_guests <= self.capacity:
            self.is_booked = True
            print(f"Two Bed Room {self.room_number} booked for {num_guests} guests.")
            return True
        elif self.is_booked:
            print(f"Two Bed Room {self.room_number} is already booked.")
        else:
            print(f"Booking failed. Insufficient capacity in Two Bed Room {self.room_number}.")
        return False
    
class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)

    def display_available_rooms(self):
        print(f"Available rooms at {self.name}:")
        for room in self.rooms:
            if not room.is_booked:
                room.display_info()

    def book_room(self, room_number, num_guests):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.book_room(num_guests)
        print(f"Room {room_number} not found in {self.name}.")
        return False


def main():
    hotel = Hotel(name="Gabor Denes Hotel")

    single_bed = int(input("Single bed booking. Please give a room no: ")) #100
    single_bed_room0 = EgyagyasSzoba(room_number=single_bed) 
    single_bed_room = EgyagyasSzoba(room_number=101)
    #single_bed_room.display_info()
    #single_bed_room.book_room(1) 

    two_bed_room = KetagyasSzoba(room_number=102)
    #two_bed_room.display_info()
    #two_bed_room.book_room(3) 

    hotel.add_room(single_bed_room0)
    hotel.add_room(single_bed_room)
    hotel.add_room(two_bed_room)

    hotel.display_available_rooms()

    hotel.book_room(101, 1)  # Successful booking
    hotel.book_room(single_bed_room0.room_number, 1)  # Successful booking
    hotel.book_room(102, 3)  # Booking fails due to insufficient capacity

if __name__ == "__main__":
    main()
 