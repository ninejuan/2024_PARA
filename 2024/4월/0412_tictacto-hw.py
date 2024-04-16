import tkinter.messagebox
import pygame, sys, datetime, time, tkinter

colors = {
    "RED": (255, 0, 0),
    "BLUE": (0, 0, 255),
    "GREEN": (0, 255, 0),
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255)
}
HEIGHT = 600
WIDTH = 600

EMPTY = 0
RED = 1
BLUE = 2

block = [[EMPTY]*3 for i in range(3)]

def winCheck():
    for i in range(3):
        if block[i][0] == block[i][1] == block[i][2]: return block[i][0]

    for i in range(3):
        if block[0][i] == block[1][i] == block[2][i]: return block[i][0]

    if block[0][0] == block[1][1] == block[2][2] or block[2][0] == block[1][1] == block[0][2]:
        return block[1][1]
    
    return EMPTY

def drawBoard(dp):
    ddugge = 6

    pygame.draw.line(dp, colors["WHITE"], (0, 200), (600, 200), ddugge)
    pygame.draw.line(dp, colors["WHITE"], (0, 400), (600, 400), ddugge)
    pygame.draw.line(dp, colors["WHITE"], (200, 0), (200, 600), ddugge)
    pygame.draw.line(dp, colors["WHITE"], (400, 0), (400, 600), ddugge)

    xPos = WIDTH // 3 // 2 - 25
    yPos = HEIGHT // 3 // 2 - 25

    for i in range(3):
        for j in range(3):
            if block[i][j] == 1:
                circle_radius = (WIDTH // 3 // 2 + HEIGHT // 3 // 2) / 2 - 10
                pygame.draw.circle(dp, colors["BLUE"],
                                   (WIDTH // 3 * j + WIDTH // 3 // 2, HEIGHT // 3 * i + HEIGHT // 3 // 2),
                                   circle_radius, 25)
            elif block[i][j] == 2:
                pygame.draw.line(dp, colors["RED"],
                                 (WIDTH // 3 * j + WIDTH // 3 // 2 - xPos, HEIGHT // 3 * i + HEIGHT // 3 // 2 - yPos),
                                 (WIDTH // 3 * j + WIDTH // 3 // 2 + xPos, HEIGHT // 3 * i + HEIGHT // 3 // 2 + yPos),
                                 25)
                pygame.draw.line(dp, colors["RED"],
                                 (WIDTH // 3 * j + WIDTH // 3 // 2 + xPos, HEIGHT // 3 * i + HEIGHT // 3 // 2 - yPos),
                                 (WIDTH // 3 * j + WIDTH // 3 // 2 - xPos, HEIGHT // 3 * i + HEIGHT // 3 // 2 + yPos),
                                 25)

def winMsg(team):
    tkinter.messagebox.showinfo("GAME ENDS!", f"{"RED" if team == 2 else "BLUE"} TEAM WINS!")
    sys.exit()


def main():
    pygame.init()
    display = pygame.display.set_mode([WIDTH, HEIGHT], False)
    pygame.display.set_caption("내년에 소프트웨어과 전공 동아리가 될 파라의 내년 부장 이주안의 틱택토")
    run = True
    turn = 1
    checked = False
    while run:
        checked = False
        WINNER = winCheck() 
        if WINNER != 0:
            winMsg(WINNER)
            run = False

        # winMsg(WINNER) if WINNER != 0 else 0
        for event in pygame.event.get():         
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if checked: continue
                # winCheck Code
                pos = pygame.mouse.get_pos()
                # pos받아서 각 좌표별로 저장
                _xpos = pos[0] // 200
                _ypos = pos[1] // 200
                if block[_ypos][_xpos] != 0: continue
                block[_ypos][_xpos] = turn
                turn = (1 if turn == 2 else 2)
                checked = True

        pygame.display.update()
        drawBoard(display)
        
    return

main()