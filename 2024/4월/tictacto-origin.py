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

block = [[EMPTY] * 3 for i in range(3)]


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


def main():
    pygame.init()
    display = pygame.display.set_mode([WIDTH, HEIGHT], False)
    pygame.display.set_caption("미래의 파라 부장 이주안의 틱택토")
    run = True
    turn: int = 1

    while run:
        for event in pygame.event.get():
            WINNER = 0
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                # winCheck Code
                pos = pygame.mouse.get_pos()
                # pos받아서 각 좌표별로 저장
                _xpos = pos[0] // 200
                _ypos = pos[1] // 200
                block[_ypos][_xpos] = turn
                if turn == 1:
                    turn = 2
                else:
                    turn = 1
                wc = winCheck()
                if wc:
                    WINNER = wc
            if WINNER != 0: break
        pygame.display.update()
        drawBoard(display)
    return


main()
pygame.quit()

# # pip install pygame
# import pygame, sys, datetime, time

# # RGB
# colors = {"RED": (255, 0, 0), "BLUE": (0, 0, 255), "GREEN": (0, 255, 0),
#           "BLACK": (0, 0, 0), "WHITE": (255, 255, 255)}

# HEIGHT = 600
# WIDTH = 600

# EMPTY = 0
# RED = 1
# BLUE = 2

# block = [[EMPTY] * 3 for i in range(3)]


# def win_check():
#     # 직선 3칸 - 가로, 세로
#     # 대각선 3칸

#     # 가로 체크
#     # 자 여러분들이 짜보세요!
#     for i in range(3):
#         if block[i][0] == block[i][1] == block[i][2]: return block[i][0]
#     # 세로 체크
#     for i in range(3):
#         if block[0][i] == block[1][i] == block[2][i]: return block[0][i]

#     if block[0][0] == block[1][1] == block[2][2] or \
#             block[2][0] == block[1][1] == block[0][2]:
#         return block[1][1]

#     return EMPTY


# def draw(display):
#     pygame.draw.rect(display, colors["WHITE"],
#                      [0, 0, WIDTH, HEIGHT])
#     # pygame.draw.line(그릴 보드, 색, 시작점, 도착점)
#     # 가로 2줄 그은거
#     pygame.draw.line(display,
#                      colors["BLACK"],
#                      (0, HEIGHT // 3),
#                      (WIDTH, HEIGHT // 3), 5)
#     pygame.draw.line(display, colors["BLACK"],
#                      (0, HEIGHT // 3 * 2), (WIDTH, HEIGHT // 3 * 2), 5)

#     pygame.draw.line(display,
#                      colors["BLACK"], (WIDTH // 3, 0), (WIDTH // 3, HEIGHT), 5)
#     pygame.draw.line(display, colors["BLACK"],
#                      (WIDTH // 3 * 2, 0), (WIDTH // 3 * 2, HEIGHT), 5)

#     xPos = WIDTH // 3 // 2 - 25
#     yPos = HEIGHT // 3 // 2 - 25

#     for i in range(3):
#         for j in range(3):
#             if block[i][j] == 1:
#                 circle_radius = (WIDTH // 3 // 2 + HEIGHT // 3 // 2) / 2 - 10
#                 pygame.draw.circle(display, colors["BLUE"],
#                                    (WIDTH // 3 * j + WIDTH // 3 // 2, HEIGHT // 3 * i + HEIGHT // 3 // 2),
#                                    circle_radius, 25)
#             elif block[i][j] == 2:
#                 pygame.draw.line(display, colors["RED"],
#                                  (WIDTH // 3 * j + WIDTH // 3 // 2 - xPos, HEIGHT // 3 * i + HEIGHT // 3 // 2 - yPos),
#                                  (WIDTH // 3 * j + WIDTH // 3 // 2 + xPos, HEIGHT // 3 * i + HEIGHT // 3 // 2 + yPos),
#                                  25)
#                 pygame.draw.line(display, colors["RED"],
#                                  (WIDTH // 3 * j + WIDTH // 3 // 2 + xPos, HEIGHT // 3 * i + HEIGHT // 3 // 2 - yPos),
#                                  (WIDTH // 3 * j + WIDTH // 3 // 2 - xPos, HEIGHT // 3 * i + HEIGHT // 3 // 2 + yPos),
#                                  25)
#     return


# def main():
#     pygame.init()
#     display = pygame.display.set_mode([WIDTH, HEIGHT], False)
#     pygame.display.set_caption("틱텍토")

#     run = True

#     turn = 1  # 나중에 사용될 턴...
#     checked = False
#     while run:
#         checked = False
#         current_winner = win_check()

#         if current_winner:
#             if current_winner != RED:
#                 print("RED Win")
#             else:
#                 print("BLUE Win")
#             run = False

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 run = False
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 if checked : continue
#                 pos = pygame.mouse.get_pos()
#                 x = pos[0] // (WIDTH // 3)
#                 y = pos[1] // (HEIGHT // 3)
#                 if block[y][x] != 0: continue
#                 block[y][x] = turn + 1
#                 turn = not turn
#                 checked = True

#         pygame.display.update()
#         draw(display)

#     time.sleep(3)
#     pygame.quit()

#     return


# main()
# sys.exit()