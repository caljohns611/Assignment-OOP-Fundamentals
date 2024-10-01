#question 1 task 1

class Vehcile: 
    def __init__(self, reg_num, type, owner):
        self.reg_num = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner - new_owner
        print(f"Updated owner of {self.reg_num} to {new_owner}")

vehicle1 = Vehcile("123456", "Truck", "Bob")
vehicle2 = Vehcile("qwerty", "Car", "Tom")

print(f"{vehicle1.owner} is the owner of {vehicle1.reg_num}")
print(f"{vehicle2.owner} is the owner of {vehicle2.reg_num}")

vehicle1.update_owner("Mason")
vehicle2.update_owner("Olivia")

#question 1 task 2

class Event:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participant_count = 0

    def add_participant(self):
        self.participant_count += 1
        print(f"Participant added. Current count: {self.participant_count}")

    def get_participant_count(self):
        return self.participant_count

event_name = "Coding Workshop"
event_date = "2024-10-15"

event = Event(event_name, event_date)

print(f"Initial participant count for '{event.name}': {event.get_participant_count()}")

event.add_participant()
event.add_participant()
event.add_participant()

print(f"Final participant count for '{event.name}': {event.get_participant_count()}")
