import pygame
from Tetromino import *

# Initialize pygame and do the pregame processing
pygame.init()
pygame.display.set_caption('Tetris')
WIDTH, HEIGHT = 1000, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))

title_font = pygame.font.Font('freesansbold.ttf', 150)

def main():
    """
        This is the main function that the game will run in.
    """
    run = menu = True
    FPS = 60
    clock = pygame.time.Clock()
    menu_buttons, game_buttons = create_buttons()
    tetrominos = create_game_surfaces()
    while run:
        clock.tick(FPS)
        window.fill((100, 150, 205))
        pos = pygame.mouse.get_pos()
        if menu:
            display_menu(pos, menu_buttons)
        else:
            display_game(pos, tetrominos, game_buttons)
        run, menu = check_events(pos, menu, tetrominos)
        pygame.display.update()

def create_buttons():
    """
        This function creates the buttons for the game.
    """
    def create_menu_buttons():
        """
            This functions creates the buttons for the menu of the game.
        """
        menu_buttons = []
        highlight = pygame.Surface((265, 50), pygame.SRCALPHA)
        highlight.fill((255,215,0,128))
        for i in range(2):
            new_game_button = pygame.Surface((265, 50))
            pygame.draw.rect(new_game_button, (192, 192, 192), pygame.Rect(0, 0, 265, 50))
            menu_buttons.append(new_game_button)
        font = pygame.font.Font('freesansbold.ttf', 50)
        button_words = []
        button_words.append(font.render('New Game', False, (255, 255, 255)))
        button_words.append(font.render('AI', False, (255, 255, 255)))
        for i in range(len(menu_buttons)):
            menu_buttons[i].blit(button_words[i], (0, 0))
        menu_buttons.append(highlight)
        return menu_buttons
    def create_ingame_buttons():
        pass
    return create_menu_buttons(), []

def create_game_surfaces():
    """
        This function creates the surfaces with which the game
        will be played.
    """
    def make_tetrominos():
        """
            This functions creates the tetrominos (the shapes).
        """
        tetrominos = []
        line = pygame.Surface((100, 25))
        line.fill((0, 255, 255))
        for i in range(4):
            pygame.draw.line(line, (255, 255, 255), (i*25, 0), (i*25, 25))
        line = Line(line)
        tetrominos.append(line)
        return tetrominos
    return make_tetrominos()

def check_events(pos, menu, tetrominos):
    """
        This function checks all of the user's inputs. It takes in
        the mouse's position and a boolean representing whether or
        not the player is at the menu returns whether or not the
        game should continue running.
    """
    def check_menu_clicks(pos):
        """
            This function handles mouse clicks that occur while
            the player is at the menu.
        """
        if WIDTH // 2 - 270 // 2 <= pos[0] <= WIDTH // 2 + 270 // 2 and \
                3 * HEIGHT // 7 <= pos[1] <= 3 * HEIGHT // 7 + 50:
            return False
        return True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, menu
        if menu:
            if event.type == pygame.MOUSEBUTTONDOWN:
                    menu = check_menu_clicks(pos)
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tetrominos[0].start_horizontal(-1)
                if event.key == pygame.K_RIGHT:
                    tetrominos[0].start_horizontal(1)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tetrominos[0].stop_horizontal()
    return True, menu

def display_menu(pos, buttons):
    """
        This function displays the menu when the player is at the menu.
    """
    for i in range(len(buttons)-1):
        window.blit(buttons[i], (WIDTH // 2 - 270 // 2, (i + 3) * HEIGHT // 7))
    if WIDTH // 2 - 270 // 2 <= pos[0] <= WIDTH // 2 + 270 // 2 and \
            3 * HEIGHT // 7 <= pos[1] <= 3 * HEIGHT // 7 + 50:
        window.blit(buttons[-1], (WIDTH // 2 - 270 // 2, 3 * HEIGHT // 7))
    title = title_font.render('Tetris', False, (255, 255, 255))
    window.blit(title, (WIDTH // 2 - title.get_rect().width // 2, HEIGHT // 7))

def display_game(pos, tetrominos, game_buttons):
    """
        This function displays the game when the player enters it
        from the menu.
    """
    def make_background():
        """
            This function creates the background where the player
            actually plays.
        """
        playground = pygame.Surface((251, 501))
        playground.fill((0, 0, 0))
        for i in range(10):
            pygame.draw.line(playground, (255, 255, 255), (i*25, 0), (i*25, 500))
        for i in range(20):
            pygame.draw.line(playground, (255, 255, 255), (0, i*25), (300, i*25))
        pygame.draw.line(playground, (255, 255, 255), (0, 500), (250, 500))
        pygame.draw.line(playground, (255, 255, 255), (250, 0), (250, 500))
        return playground
    background = make_background()
    for tetromino in tetrominos:
        tetromino.update_pos(pygame.time.get_ticks())
        background.blit(tetromino.surface, (tetromino.pos_x, tetromino.pos_y))
    window.blit(background, (WIDTH // 2 - 125, HEIGHT // 2 - 250))

main()
pygame.quit()
