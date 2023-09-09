import tkinter as tk
import math

class Canvas:
    def __init__(self, width, height):
        self.root = tk.Tk()
        self.canvas = tk.Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        self.CP = (width / 2, height / 2)  # Initial position at the center
        self.CD = 0  # Initial direction (degrees)

    def turnTo(self, angle):
        self.CD = angle % 360  # Ensure angle is within [0, 360]

    def turn(self, angle):
        self.CD = (self.CD + angle) % 360  # Ensure angle is within [0, 360]

    def forward(self, dist, isVisible=True):
        rad_per_deg = 0.017453393  # radians per degree
        x = self.CP[0] + dist * math.cos(rad_per_deg * self.CD)
        y = self.CP[1] + dist * math.sin(rad_per_deg * self.CD)

        if isVisible:
            self.canvas.create_line(self.CP[0], self.CP[1], x, y)
            self.canvas.update()

        self.CP = (x, y)

    def run(self):
        self.root.mainloop()

# Example usage:
if __name__ == "__main__":
    canvas = Canvas(400, 400)

    # Draw a 90-degree triangle
    canvas.forward(100)
    canvas.turn(90)  # Turn 90 degrees
    canvas.forward(100)
    canvas.turn(135)  # Turn 135 degrees
    canvas.forward(141.42)  # Length of the hypotenuse

    canvas.run()
