label arc2:
    show mc neutral

    "The world around you shifts, pixels dissolving into streams of data."
    "You find yourself inside a vast, glowing network—a living map of connections."

    mc "Welcome, [player_name]. This is the Neural Simulation, a construct designed to test your AI intuition."
    
    "Dr. Monroe steps forward, his gaze intense."
    
    mc "Three domains await you, each revealing a different truth about AI."
    
    menu:
        "Explore the Deterministic Zone":
            $ Location = renpy.call_screen("MapScreen")
            jump deterministic_zone

        "Explore the Probabilistic Zone":
            $ Location = renpy.call_screen("MapScreen")
            jump probabilistic_zone

        "Explore the Reinforcement Zone":
            $ Location = renpy.call_screen("MapScreen")
            jump reinforcement_zone

init python:
    import pygame
    import renpy.store as store
    import renpy.exports as renpy
    import pygame
    import os

    class OverworldGame:
        def __init__(self):
            self.width, self.height = 800, 600
            self.running = True  
            self.clock = pygame.time.Clock()

            # Correctly load image using Pygame
            self.background = pygame.image.load("images/backgrounds/probabilistic.png")

            self.player = pygame.image.load(os.path.join("game", "images", "characters", "player.png"))

            # Player position
            self.player_x = 100
            self.player_y = 100
            self.speed = 5  

        def handle_events(self):
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False  

        def update(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.player_x -= self.speed
            if keys[pygame.K_RIGHT]:
                self.player_x += self.speed
            if keys[pygame.K_UP]:
                self.player_y -= self.speed
            if keys[pygame.K_DOWN]:
                self.player_y += self.speed

        def draw(self, screen):
            screen.blit(self.background, (0, 0))  # Draw background
            screen.blit(self.player, (self.player_x, self.player_y))  # Draw player

        def run(self):
            screen = pygame.display.set_mode((self.width, self.height))
            while self.running:
                self.handle_events()
                self.update()
                self.draw(screen)
                pygame.display.flip()
                self.clock.tick(30)
            renpy.pop_screen()  # Return to Ren'Py on exit

# Function to start the game
label start_overworld:
    $ game = OverworldGame()
    $ renpy.call_screen("OverworldScreen")
    return

label deterministic_zone:
    scene bg_deterministic_zone with fade
    "You step into the Deterministic Zone, where every action has a predictable result."
    "Dr. Monroe appears, ready to test you."
    
    mc "In deterministic AI, every input leads to a single, expected outcome."
    mc "Let's see if you can solve this logic puzzle."

    # Insert puzzle mini-game here
    jump start_overworld  # Returns to overworld

label probabilistic_zone:
    scene bg_probabilistic_zone with fade
    "The Probabilistic Zone is filled with shifting patterns, unpredictable and ever-changing."
    
    mc "AI often relies on probabilities rather than certainties."
    mc "Try navigating this space without getting lost."

    # Insert probability-based challenge here
    jump start_overworld  # Returns to overworld

label reinforcement_zone:
    scene bg_reinforcement_zone with fade
    "The Reinforcement Learning Zone is an adaptive space, where trial and error is key."
    
    mc "This area simulates how AI learns through rewards and punishments."
    mc "Make the right choices to maximize your score."

    # Insert reinforcement learning challenge
    jump start_overworld  # Returns to overworld
