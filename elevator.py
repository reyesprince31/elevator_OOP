class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current
        
    def up(self):
        """Makes the elevator go up one floor."""
        if self.current >= elevator.top:
            self.current -= 1
        self.current += 1
    def down(self):
        """Makes the elevator go down one floor."""
        if self.current <= elevator.bottom:
            self.current += 1
        self.current -= 1
    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        if floor >= elevator.top:
            self.current = elevator.top
        else:
            self.current = floor

    def __str__(self) -> str:
        return f"Current Floor: {self.current}"
        
    

elevator = Elevator(-1, 10, 0)

elevator.up()
print(elevator.current)

elevator.down()
print(elevator.current)

elevator.go_to(10)
print(elevator.current)

elevator.go_to(10)
elevator.up()
elevator.down()
print(elevator.current)

elevator.go_to(-1)
elevator.down()
elevator.down()
elevator.up()
elevator.up()
print(elevator.current) # should be 1


elevator.go_to(7)
print(elevator)
