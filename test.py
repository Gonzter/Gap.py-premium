import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Main Menu")

# Load background image
background = pygame.image.load("background.png")
background = pygame.transform.scale(background, (screen_width, screen_height))

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Define fonts
font = pygame.font.Font(None, 36)

# Define button properties
button_width = 200
button_height = 50
button_padding = 20

# Function to draw text on button
def draw_text(text, font, color, x, y):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)

# Function to draw buttons
def draw_button(x, y, text):
    pygame.draw.rect(screen, WHITE, (x, y, button_width, button_height))
    draw_text(text, font, BLACK, x + button_width // 2, y + button_height // 2)

# Main menu loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if any button is clicked
            mouse_pos = pygame.mouse.get_pos()
            if play_button_rect.collidepoint(mouse_pos):
                print("Play button clicked")
            elif settings_button_rect.collidepoint(mouse_pos):
                print("Settings button clicked")
            elif quit_button_rect.collidepoint(mouse_pos):
                running = False
                pygame.quit()
                sys.exit()

    # Draw background
    screen.blit(background, (0, 0))

    # Draw buttons
    play_button_rect = pygame.Rect((screen_width - button_width) // 2, 200, button_width, button_height)
    draw_button(play_button_rect.x, play_button_rect.y, "Play")

    settings_button_rect = pygame.Rect((screen_width - button_width) // 2, 300, button_width, button_height)
    draw_button(settings_button_rect.x, settings_button_rect.y, "Settings")

    quit_button_rect = pygame.Rect((screen_width - button_width) // 2, 400, button_width, button_height)
    draw_button(quit_button_rect.x, quit_button_rect.y, "Quit")

    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(30)
