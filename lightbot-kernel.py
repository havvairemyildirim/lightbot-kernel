
class LightBot:
    def __init__(self, size=10):
        # Initialize the terrain and bot properties
        self.size = size
        self.terrain = [[[{'height': 0, 'light': False, 'bot': False} for _ in range(size)] for _ in range(size)]]
        self.position = [0, 0, 0]  # Starting at (x, y, z)
        self.direction = 1  # 0: Up, 1: Right, 2: Down, 3: Left

        # Mark the bot's initial position
        self.terrain[self.position[2]][self.position[0]][self.position[1]]['bot'] = True

    def move_forward(self):
        current_block = self.terrain[self.position[2]][self.position[0]][self.position[1]]
        current_block['bot'] = False  # Remove bot from current block

        # Update position based on direction
        if self.direction == 0 and self.position[0] > 0:  # Up
            self.position[0] -= 1
        elif self.direction == 1 and self.position[1] < self.size - 1:  # Right
            self.position[1] += 1
        elif self.direction == 2 and self.position[0] < self.size - 1:  # Down
            self.position[0] += 1
        elif self.direction == 3 and self.position[1] > 0:  # Left
            self.position[1] -= 1

        next_block = self.terrain[self.position[2]][self.position[0]][self.position[1]]
        next_block['bot'] = True  # Mark bot on the new block

    def jump(self):
        current_block = self.terrain[self.position[2]][self.position[0]][self.position[1]]
        current_block['bot'] = False  # Remove bot from current block

        # Calculate the next position
        next_x, next_y = self.position[0], self.position[1]
        if self.direction == 0:  # Up
            next_x -= 1
        elif self.direction == 1:  # Right
            next_y += 1
        elif self.direction == 2:  # Down
            next_x += 1
        elif self.direction == 3:  # Left
            next_y -= 1

        # Check bounds and adjust z-level
        if 0 <= next_x < self.size and 0 <= next_y < self.size:
            next_height = self.terrain[0][next_x][next_y]['height']  # Assuming only one level for now
            self.position = [next_x, next_y, next_height]

        # Update bot's new position
        self.terrain[self.position[2]][self.position[0]][self.position[1]]['bot'] = True

    def toggle_light(self):
        block = self.terrain[self.position[2]][self.position[0]][self.position[1]]
        block['light'] = not block['light']

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def turn_left(self):
        self.direction = (self.direction - 1) % 4

    def interpret_instruction(self, instruction):
        if instruction == '^':
            self.move_forward()
        elif instruction == '>':
            self.turn_right()
        elif instruction == '<':
            self.turn_left()
        elif instruction == '@':
            self.toggle_light()
        elif instruction == '*':
            self.jump()

    def print_initial_condition(self):
        print("Initial Bot Position and Terrain Light Conditions:")
        for row in self.terrain[self.position[2]]:
            print(' '.join([f"{'X' if block['bot'] else ' '}{' on' if block['light'] else ' off'}" for block in row]))
        print()  # Newline for better readability

    def print_status(self):
        # Map direction to string
        direction_map = {0: "Up", 1: "Right", 2: "Down", 3: "Left"}
        # Get the current light state
        light_state = "On" if self.terrain[self.position[2]][self.position[0]][self.position[1]]['light'] else "Off"

        print(f"Bot Position: {self.position}")
        print(f"Direction: {direction_map[self.direction]}")
        print(f"Light State: {light_state}")

    def print_terrain_light_condition(self):
        # Print the state of the terrain lights and bot presence
        print("Terrain Light Conditions and Bot Presence:")
        for row in self.terrain[self.position[2]]:
            print(' '.join([f"{'X' if block['bot'] else ' '}{' on' if block['light'] else ' off'}" for block in row]))
        print()  # Newline for better readability

    def execute_instructions(self, instructions):
        for instruction in instructions:
            self.interpret_instruction(instruction)
            self.print_status()
            self.print_terrain_light_condition()


# Initialize the game
print("Let's play the game!")
instructions = input("Enter instructions for the bot (^, >, <, @, *): ")
light_bot = LightBot()
light_bot.print_initial_condition()  # Print initial conditions
light_bot.execute_instructions(instructions)
