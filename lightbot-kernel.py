
class LightBot:
    def __init__(self, size=10, levels=5):
        self.size = size
        self.levels = levels
        self.terrain = [[[{'height': z, 'light': False, 'bot': False, 'blue': False}
                          for _ in range(size)] for _ in range(size)] for z in range(levels)]
        self.position = [0, 0, 0]  # Starting at (x, y, z)
        self.direction = 1  # 0: Up, 1: Right, 2: Down, 3: Left

        # Mark the bot's initial position
        self.terrain[self.position[2]][self.position[0]][self.position[1]]['bot'] = True

        # Example blue blocks
        self.terrain[0][1][1]['blue'] = True
        self.terrain[1][2][2]['blue'] = True
        self.terrain[2][3][3]['blue'] = True

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

        next_x, next_y = self.position[0], self.position[1]
        if self.direction == 0:  # Up
            next_x -= 1
        elif self.direction == 1:  # Right
            next_y += 1
        elif self.direction == 2:  # Down
            next_x += 1
        elif self.direction == 3:  # Left
            next_y -= 1

        if 0 <= next_x < self.size and 0 <= next_y < self.size:
            for z in range(self.levels - 1, -1, -1):
                if self.terrain[z][next_x][next_y]['height'] == z:
                    self.position = [next_x, next_y, z]
                    break

        self.terrain[self.position[2]][self.position[0]][self.position[1]]['bot'] = True

    def toggle_light(self):
        block = self.terrain[self.position[2]][self.position[0]][self.position[1]]
        if block['blue']:  # Only toggle lights on blue blocks
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

    def print_status(self):
        direction_map = {0: "Up", 1: "Right", 2: "Down", 3: "Left"}
        block = self.terrain[self.position[2]][self.position[0]][self.position[1]]
        light_state = "On" if block['light'] else "Off"
        print(f"Bot Position: {self.position}")
        print(f"Direction: {direction_map[self.direction]}")
        print(f"Light State: {light_state}")

    def print_terrain(self):
        z = self.position[2]  # Show only the current level
        print("Terrain Light Conditions and Bot Presence:")
        for row in self.terrain[z]:
            print(' '.join([
                f"{'X' if block['bot'] else ''}"
                f"{'(off)' if not block['blue'] and not block['light'] else ''}"
                f"{' off' if block['blue'] and not block['light'] else ''}"
                f"{' on' if block['light'] else ''}"
                for block in row
            ]))
        print()  # Newline for better readability

    def execute_instructions(self, instructions):
        for instruction in instructions:
            self.interpret_instruction(instruction)
            print("--------")  # Separator between steps
            self.print_status()
            self.print_terrain()


# Initialize the game
print("Let's play the game!")
instructions = input("Enter instructions for the bot (^, >, <, @, *): ")
light_bot = LightBot()
light_bot.print_terrain()  # Print initial terrain
light_bot.execute_instructions(instructions)
