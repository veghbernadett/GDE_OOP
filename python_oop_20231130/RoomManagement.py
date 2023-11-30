from abc import ABC, abstractmethod

class Room(ABC):
    def __init__(self, room_number, capacity, rate):
        self.room_number = room_number
        self.capacity = capacity
        self.rate = rate
        self.is_booked = False

    @property
    def occupancy(self): # foglalhatosag
        return self._occupancy

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


def main():
    single_bed_room = EgyagyasSzoba(room_number=101)
    single_bed_room.display_info()
    single_bed_room.book_room(1) 

    two_bed_room = KetagyasSzoba(room_number=102)
    two_bed_room.display_info()
    two_bed_room.book_room(3) 

if __name__ == "__main__":
    main()
 