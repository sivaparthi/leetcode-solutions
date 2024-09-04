class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        # Direction vectors for north, east, south, and west
        direction_vectors = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        direction_index = 0  # Start facing north (0th index)

        # Convert obstacles to a set of tuples for O(1) lookup
        obstacle_set = set(map(tuple, obstacles))
        print(obstacle_set)

        # Initialize robot's starting position
        x, y = 0, 0
        max_distance = 0

        # Process each command
        for command in commands:
            if command == -1:  # Turn right 90 degrees
                direction_index = (direction_index + 1) % 4
            elif command == -2:  # Turn left 90 degrees
                direction_index = (direction_index - 1) % 4
            else:  # Move forward 'command' steps
                dx, dy = direction_vectors[direction_index]
                for j in range(command):
                    # Move one step in the current direction
                    if (x + dx, y + dy) not in obstacle_set:
                        x += dx
                        y += dy
                        # Update the maximum squared distance from the origin
                        max_distance = max(max_distance, x**2 + y**2)
        return max_distance