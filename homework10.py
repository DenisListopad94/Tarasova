#Task 1
# from datetime import datetime
#
# class Task:
#     def __init__(self, description, deadline):
#         self.description = description
#         self.status = False
#         self.deadline = deadline
#
#     def mark_as_done(self):
#         self.status = True
#
#     def __str__(self):
#         status_str = "Done" if self.status else "Not Done"
#         return f"{self.description} (Status: {status_str}, Deadline: {self.deadline})"
#
# class Project:
#     def __init__(self, name):
#         self.name = name
#         self.tasks = []
#
#     def add_task(self, task):
#         self.tasks.append(task)
#
#     def show_tasks(self):
#         print(f"Tasks for Project '{self.name}':")
#         for task in self.tasks:
#             print(task)
#
# class ProjectManager:
#     def __init__(self):
#         self.projects = []
#
#     def add_project(self, project):
#         self.projects.append(project)
#
#     def show_all_tasks(self):
#         print("All Tasks:")
#         for project in self.projects:
#             project.show_tasks()
#
# project_manager = ProjectManager()
# task1 = Task("Write report", datetime(2023, 12, 1))
# task2 = Task("Prepare presentation", datetime(2023, 12, 5))
# project1 = Project("Project A")
# project1.add_task(task1)
# project1.add_task(task2)
# project_manager.add_project(project1)
# project_manager.show_all_tasks()
# task1.mark_as_done()
# project_manager.show_all_tasks()

#Task 2
# class Passenger:
#     def __init__(self, first_name, last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"
#
# class Ticket:
#     def __init__(self, passenger, flight):
#         self.passenger = passenger
#         self.flight = flight
#
#     def __str__(self):
#         return f"Ticket: {self.passenger} - {self.flight}"
#
# class Flight:
#     def __init__(self, flight_number, destination, departure_time):
#         self.flight_number = flight_number
#         self.destination = destination
#         self.departure_time = departure_time
#         self.reserved_tickets = []
#
#     def reserve_ticket(self, passenger):
#         ticket = Ticket(passenger, self)
#         self.reserved_tickets.append(ticket)
#         print(f"Ticket reserved for {passenger} on Flight {self.flight_number} to {self.destination}")
#
#     def cancel_reservation(self, ticket):
#         if ticket in self.reserved_tickets:
#             self.reserved_tickets.remove(ticket)
#             print(f"Reservation canceled for {ticket.passenger} on Flight {self.flight_number}")
#         else:
#             print("Ticket not found in reservations.")
#
#     def show_reserved_tickets(self):
#         print(f"Reserved Tickets for Flight {self.flight_number} to {self.destination}:")
#         for ticket in self.reserved_tickets:
#             print(ticket)
#
# class Airline:
#     def __init__(self, name):
#         self.name = name
#         self.flights = []
#
#     def add_flight(self, flight):
#         self.flights.append(flight)
#
#     def show_all_flights(self):
#         print(f"All Flights for {self.name}:")
#         for flight in self.flights:
#             print(f"Flight {flight.flight_number} to {flight.destination} - Departure Time: {flight.departure_time}")
#
# airline = Airline("Sample Airlines")
# passenger1 = Passenger("John", "Doe")
# passenger2 = Passenger("Jane", "Doe")
# flight1 = Flight("FA123", "New York", "2023-12-01 10:00")
# flight2 = Flight("FA456", "Los Angeles", "2023-12-02 12:00")
# airline.add_flight(flight1)
# airline.add_flight(flight2)
# flight1.reserve_ticket(passenger1)
# flight1.reserve_ticket(passenger2)
# flight2.reserve_ticket(passenger1)
# airline.show_all_flights()
# flight1.show_reserved_tickets()
# flight1.cancel_reservation(flight1.reserved_tickets[0])
# flight1.show_reserved_tickets()

#Task 3
# from abc import ABC, abstractmethod
#
# class Alive(ABC):
#     def __init__(self, age_limit):
#         self.age = 0
#         self.age_limit = age_limit
#         self.alive = True
#
#     @abstractmethod
#     def eat(self, food_available):
#         pass
#
#     @abstractmethod
#     def check_status(self):
#         pass
#
# class Fox(Alive):
#     def __init__(self):
#         super().__init__(age_limit=5)
#
#     def eat(self, food_available):
#         if food_available > 0:
#             print("Fox is eating a rabbit.")
#             food_available -= 1
#         else:
#             print("No food available for the fox.")
#             self.alive = False
#
#     def check_status(self):
#         self.age += 1
#         if self.age >= self.age_limit:
#             print("Fox has reached its age limit and died.")
#             self.alive = False
#
# class Rabbit(Alive):
#     def __init__(self):
#         super().__init__(age_limit=3)
#
#     def eat(self, food_available):
#         if food_available > 0:
#             print("Rabbit is eating a plant.")
#             food_available -= 1
#         else:
#             print("No food available for the rabbit.")
#             self.alive = False
#
#     def check_status(self):
#         self.age += 1
#         if self.age >= self.age_limit:
#             print("Rabbit has reached its age limit and died.")
#             self.alive = False
#
# class Plant(Alive):
#     def __init__(self):
#         super().__init__(age_limit=10)
#
#     def eat(self, food_available):
#         print("Plant is absorbing sunlight.")
#
#     def check_status(self):
#         self.age += 1
#         if self.age >= self.age_limit:
#             print("Plant has reached its age limit and died.")
#             self.alive = False
#
# fox = Fox()
# rabbit = Rabbit()
# plant = Plant()
#
# for _ in range(3):
#     fox.eat(1)
#     rabbit.eat(1)
#     plant.eat(0)
#
#     fox.check_status()
#     rabbit.check_status()
#     plant.check_status()
