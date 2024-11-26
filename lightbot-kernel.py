
class LightBot:
    def __init__(self, size=10):
        # Initialize the terrain and bot properties
        self.size = size
        self.terrain = [[(False, False) for _ in range(size)] for _ in range(size)]  # (light, bot_present)
        self.position = [0, 0]  # Starting position at (0, 0)
        self.direction = 1  # 0: Up, 1: Right, 2: Down, 3: Left

        # Mark the bot's initial position
        self.terrain[self.position[0]][self.position[1]] = (False, True)

    def move_forward(self):
        # Remove bot from the current position
        current_light, _ = self.terrain[self.position[0]][self.position[1]]
        self.terrain[self.position[0]][self.position[1]] = (current_light, False)

        # Move the bot forward in the current direction
        if self.direction == 0 and self.position[0] > 0:  # Up
            self.position[0] -= 1
        elif self.direction == 1 and self.position[1] < self.size - 1:  # Right
            self.position[1] += 1
        elif self.direction == 2 and self.position[0] < self.size - 1:  # Down
            self.position[0] += 1
        elif self.direction == 3 and self.position[1] > 0:  # Left
            self.position[1] -= 1

        # Mark the bot's new position
        self.terrain[self.position[0]][self.position[1]] = (current_light, True)

    def turn_right(self):
        self.direction = (self.direction + 1) % 4

    def turn_left(self):
        self.direction = (self.direction - 1) % 4

    def toggle_light(self):
        current_light, bot_present = self.terrain[self.position[0]][self.position[1]]
        self.terrain[self.position[0]][self.position[1]] = (not current_light, bot_present)

    def interpret_instruction(self, instruction):
        if instruction == '^':
            self.move_forward()
        elif instruction == '>':
            self.turn_right()
        elif instruction == '<':
            self.turn_left()
        elif instruction == '@':
            self.toggle_light()


    def print_initial_condition(self):
        print("Initial Bot Position and Terrain Light Conditions:")
        for row in self.terrain:
            print(' '.join([f"{'X' if bot else ' '}{' on' if light else ' off'}" for light, bot in row]))
        print()  # Newline for better readability

    def print_status(self):
        # Map direction to string
        direction_map = {0: "Up", 1: "Right", 2: "Down", 3: "Left"}
        # Get the current light state
        light_state = "On" if self.terrain[self.position[0]][self.position[1]][0] else "Off"

        print(f"Bot Position: {self.position}")
        print(f"Direction: {direction_map[self.direction]}")
        print(f"Light State: {light_state}")

    def print_terrain_light_condition(self):
        # Print the state of the terrain lights and bot presence
        print("Terrain Light Conditions and Bot Presence:")
        for row in self.terrain:
            print(' '.join([f"{'X' if bot else ' '}{' on' if light else ' off'}" for light, bot in row]))
        print()  # Newline for better readability

    def execute_instructions(self, instructions):
        for instruction in instructions:
            self.interpret_instruction(instruction)
            self.print_status()
            self.print_terrain_light_condition()

print("Let's play the game!")
instructions = input("Enter instructions for the bot: ")
# ^^>^<^@
light_bot = LightBot()
light_bot.print_initial_condition()  # Print initial conditions
light_bot.execute_instructions(instructions)
