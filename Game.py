import pygame
import random
from Tetromino import *

# Initialize pygame and do the pregame processing
pygame.init()
pygame.display.set_caption('Tetris')
WIDTH, HEIGHT = 1000, 700
window = pygame.display.set_mode((WIDTH, HEIGHT))

def main():
    """
        This is the main function that the game will run in.
    """
    run = menu = True
    FPS = 60
    clock = pygame.time.Clock()
    fonts = make_fonts()
    menu_buttons, game_buttons = create_buttons(fonts)
    tetrominos = [make_tetromino([])]
    while run:
        clock.tick(FPS)
        window.fill((100, 150, 205))
        pos = pygame.mouse.get_pos()
        if menu:
            display_menu(pos, fonts, menu_buttons)
        else:
            display_game(pos, fonts, tetrominos, game_buttons)
        run, menu = check_events(pos, menu, tetrominos)
        pygame.display.update()

def make_fonts():
    """
        This function makes the fonts for the game.
    """
    fonts = []
    fonts.append(pygame.font.Font('freesansbold.ttf', 150))
    fonts.append(pygame.font.Font('freesansbold.ttf', 50))
    return fonts

def create_buttons(fonts):
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
        button_words = []
        button_words.append(fonts[1].render('New Game', False, (255, 255, 255)))
        button_words.append(fonts[1].render('AI', False, (255, 255, 255)))
        for i in range(len(menu_buttons)):
            menu_buttons[i].blit(button_words[i], (0, 0))
        menu_buttons.append(highlight)
        return menu_buttons
    def create_ingame_buttons():
        pass
    return create_menu_buttons(), []

def make_tetromino(tetrominos):
    """
        This functions creates a tetromino.
    """
    def make_block_surface(color):
        """
            This function makes the surface for one block.
        """
        surface = pygame.Surface((25, 25))
        surface.fill(color)
        pygame.draw.rect(surface, (255, 255, 255), (0, 0, 25, 25), 1)
        return surface
    def make_L():
        """
            This function creates an L tetromino.
        """
        blocks = []
        color = (255, 140, 0)
        for i in range(3):
            surface = make_block_surface(color)
            blocks.append(Block(surface, (i*25 + 75, -25)))
        blocks.append(Block(make_block_surface(color), (125, -50)))
        return L(blocks, tetrominos)
    def make_J():
        """
            This function creates a J tetromino.
        """
        blocks = []
        color = (0, 96, 255)
        for i in range(3):
            surface = make_block_surface(color)
            blocks.append(Block(surface, (i*25 + 75, -25)))
        blocks.append(Block(make_block_surface(color), (75, -50)))
        return J(blocks, tetrominos)
    def make_S():
        """
            This function creates an S tetromino.
        """
        blocks = []
        color = (50, 255, 100)
        for i in range(2):
            surface = make_block_surface(color)
            blocks.append(Block(surface, (i*25 + 75, -25)))
        for i in range(2):
            surface = make_block_surface(color)
            blocks.append(Block(surface, (i*25 + 100, -50)))
        return S(blocks, tetrominos)
    def make_Z():
        """
            This function creates a Z tetromino.
        """
        blocks = []
        color = (204, 33, 41)
        for i in range(2):
            surface = make_block_surface(color)
            blocks.append(Block(surface, (i*25 + 75, -50)))
        for i in range(2):
            surface = make_block_surface(color)
            blocks.append(Block(surface, (i*25 + 100, -25)))
        return Z(blocks, tetrominos)
    def make_I():
        """
            This function creates an I tetromino.
        """
        blocks = []
        color = (0, 200, 255)
        for i in range(4):
            surface = make_block_surface(color)
            blocks.append(Block(surface, (i*25 + 75, -25)))
        return I(blocks, tetrominos)
    def make_T():
        """
            This function creates a T tetromino.
        """
        blocks = []
        color = (177, 156, 255)
        for i in range(3):
            surface = make_block_surface(color)
            blocks.append(Block(surface, (i*25 + 75, -25)))
        blocks.append(Block(make_block_surface(color), (100, -50)))
        return T(blocks, tetrominos)
    def make_O():
        """
            This functin creates a O tetromino.
        """
        blocks = []
        color = (255, 200, 50)
        blocks.append(Block(make_block_surface(color), (100, -50)))
        blocks.append(Block(make_block_surface(color), (100, -25)))
        blocks.append(Block(make_block_surface(color), (125, -50)))
        blocks.append(Block(make_block_surface(color), (125, -25)))
        return O(blocks, tetrominos)
    choice = random.randint(1, 7)
    tetromino = None
    if choice == 1:
        tetromino = make_L()
    elif choice == 2:
        tetromino = make_J()
    elif choice == 3:
        tetromino = make_S()
    elif choice == 4:
        tetromino = make_Z()
    elif choice == 5:
        tetromino = make_I()
    elif choice == 6:
        tetromino = make_T()
    elif choice == 7:
        tetromino = make_O()
    return tetromino

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
                    tetrominos[-1].start_horizontal(-1)
                if event.key == pygame.K_RIGHT:
                    tetrominos[-1].start_horizontal(1)
                if event.key == pygame.K_DOWN:
                    tetrominos[-1].start_down()
                if event.key == pygame.K_UP:
                    tetrominos[-1].shift()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tetrominos[-1].stop_horizontal()
                if event.key == pygame.K_DOWN:
                    tetrominos[-1].stop_down()
    return True, menu

def remove_tetrominos(tetrominos):
    """
        This function removes all of the blocks of the tetrominos that
        have made a full line. If all of the blocks of a specific tetromino
        have been removed. The tetromino is removed from the list of
        tetrominos.
    """
    filled_lines = set()
    block_locations = set()
    for tetro in tetrominos:
        for block in tetro.blocks:
            block_locations.add((block.pos_x, block.pos_y))
    lowest_y = -float('inf')
    for block in tetrominos[-1].blocks:
        y = block.pos_y
        if all([(x, y) in block_locations for x in range(0, 250, 25)]):
            lowest_y = max(lowest_y, y)
            filled_lines.add(y)
    if len(filled_lines) > 0:
        for tetro in tetrominos:
            for block in tetro.blocks:
                if block.pos_y in filled_lines:
                    block.remove_block()
        i = 0
        while i < len(tetrominos):
            if all([b.active == False for b in tetrominos[i].blocks]):
                tetrominos.pop(i)
            else:
                i += 1
        for i in range(len(tetrominos)):
            tetrominos[i].fall(tetrominos, i, lowest_y)
    return len(filled_lines) * 10

def display_menu(pos, fonts, buttons):
    """
        This function displays the menu when the player is at the menu.
    """
    for i in range(len(buttons)-1):
        window.blit(buttons[i], (WIDTH // 2 - 270 // 2, (i + 3) * HEIGHT // 7))
    if WIDTH // 2 - 270 // 2 <= pos[0] <= WIDTH // 2 + 270 // 2 and \
            3 * HEIGHT // 7 <= pos[1] <= 3 * HEIGHT // 7 + 50:
        window.blit(buttons[-1], (WIDTH // 2 - 270 // 2, 3 * HEIGHT // 7))
    title = fonts[0].render('Tetris', False, (255, 255, 255))
    window.blit(title, (WIDTH // 2 - title.get_rect().width // 2, HEIGHT // 7))

def display_game(pos, fonts, tetrominos, game_buttons):
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
    if tetrominos[-1].active:
        tetrominos[-1].update_pos(pygame.time.get_ticks(), tetrominos[:-1])
    else:
        remove_tetrominos(tetrominos)
        tetrominos.append(make_tetromino(tetrominos))
    for tetro in tetrominos:
        for block in tetro.blocks:
            background.blit(block.surface, (block.pos_x, block.pos_y))
    window.blit(background, (WIDTH // 2 - 125, HEIGHT // 2 - 250))

main()
pygame.quit()
