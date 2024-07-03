import numpy as np
class LineModel:
    def _init_(self, slope=1, bias=0):
        """
        Initialize a new LineModel with given slope and bias values.
        """
        self.points = []
        self.slope = slope  # Default slope
        self.bias = bias  # Default bias (intercept)
        
    def add_points(self, points):
        """
        Adds new points to the existing points list.
        """
        self.points.extend(points)
        
    def total_distance(self):
        """
        Computes the summation of all perpendicular distances between points and the line.
        Returns the sum.
        """
        total_dist = 0.0
        for point in self.points:
            x, y = point
            # Calculate perpendicular distance from point (x, y) to the line y = mx + c
            dist = np.abs(self.slope * x - y + self.bias) / np.sqrt(self.slope ** 2 + 1)
            total_dist += dist
        return total_dist
    
    def line_equation(self):
        """
        Prints the line equation in the form of y = mx + c.
        """
        print(f"Line equation: y = {self.slope}x + {self.bias}")

class OptimizeLineModel(LineModel):
    def _init_(self, learning_rate, iterations, slope=1, bias=0):
        """
        Initialize a new OptimizeLineModel with a learning rate and number of iterations for optimization.
        """
        super()._init_(slope, bias)
        self.learning_rate = learning_rate
        self.iterations = iterations
        
    def optimize_line(self):
        """
        Updates the line's slope and bias values to minimize the perpendicular distances.
        """
        num_points = len(self.points)
        for _ in range(self.iterations):
            gradient_slope = 0.0
            gradient_bias = 0.0
            for point in self.points:
                x, y = point
                # Calculate gradients for slope and bias
                predicted_y = self.slope * x + self.bias
                error = predicted_y - y
                gradient_slope += 2 * error * x / num_points
                gradient_bias += 2 * error / num_points
            # Update slope and bias using gradient descent
            self.slope -= self.learning_rate * gradient_slope
            self.bias -= self.learning_rate * gradient_bias

# Implementation
points = [(1, 2), (4, 8), (3, 6), (8, 16)]
model = OptimizeLineModel(learning_rate=0.01, iterations=100)
model.add_points(points)
model.optimize_line()
print(f"Total distance: {model.total_distance()}")
model.line_equation()