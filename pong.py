import pygame 

# constants and variables
white = (255,255,255)
black = (0,0,0)

width = 600
height = 600

pygame.init()
game_font = pygame.font.SysFont('Ubuntu',40)

delay =  30

paddle_speed = 20

paddle_width = 10
paddle_height = 100

p1_x_pos = 10
p1_y_pos = height / 2 - paddle_height / 2

p2_x_pos = width - paddle_width - 10
p2_y_pos = height / 2 - paddle_height / 2

p1_score = 0
p2_score = 0

p1_up = False
p1_down = False
p2_up = False
p2_down = False

ball_x_pos = width / 2
ball_y_pos = height / 2
ball_width = 8
ball_x_vel = -10
ball_y_vel = 0

screen = pygame.display.set_mode((width,height))

# drawing objects
def draw_objects():
    pygame.draw.rect(screen, white, (int(p1_x_pos), int(p1_y_pos), paddle_width, paddle_height))
    pygame.draw.rect(screen, white, (int(p2_x_pos), int(p2_y_pos), paddle_width, paddle_height))
    pygame.draw.circle(screen, white, (ball_x_pos, ball_y_pos), ball_width)
    score = game_font.render(f"{str(p1_score)} - {str(p2_score)}", False, white)
    screen.blit(score, (width / 2, 30))

def apply_player_movement():
    global p1_y_pos
    global p2_y_pos

    if p1_up:
        p1_y_pos = max(p1_y_pos - paddle_speed, 0)
    elif p1_down:
        p1_y_pos = min(p1_y_pos + paddle_speed, height)
    if p2_up:
        p2_y_pos = max(p2_y_pos - paddle_speed, 0)
    elif p2_down:
        p2_y_pos = min(p2_y_pos + paddle_speed, height)


def apply_ball_movement():
    global ball_x_pos
    global ball_y_pos
    global ball_x_vel
    global ball_y_vel
    global p1_score
    global p2_score

    if (ball_x_pos + ball_x_vel < p1_x_pos + paddle_width) and (p1_y_pos < ball_y_pos + ball_y_vel + ball_width < p1_y_pos + paddle_height):
        ball_x_vel = -ball_x_vel
        ball_y_vel = (p1_y_pos + paddle_height / 2 - ball_y_pos) / 15
        ball_y_vel = -ball_y_vel
    elif ball_x_pos + ball_x_vel < 0:
        p2_score += 1
        ball_x_pos = width / 2
        ball_y_pos = height / 2
        ball_x_vel = 10
        ball_y_vel = 0
    if (ball_x_pos + ball_x_vel > p2_x_pos - paddle_width) and (p2_y_pos < ball_y_pos + ball_y_vel + ball_width < p2_y_pos + paddle_height):
        ball_x_vel = -ball_x_vel
        ball_y_vel = (p2_y_pos + paddle_height / 2 - ball_y_pos) / 15
        ball_y_vel = -ball_y_vel
    elif ball_x_pos + ball_x_vel > height:
        p1_score += 1
        ball_x_pos = width / 2
        ball_y_pos = height / 2
        ball_x_vel = -10
        ball_y_vel = 0
    if ball_y_pos + ball_y_vel > height or ball_y_pos + ball_y_vel < 0:
        ball_y_vel = -ball_y_vel    
    
    ball_x_pos += ball_x_vel
    ball_y_pos += ball_y_vel

pygame.display.set_caption("Pong")
screen.fill(black)
pygame.display.flip()

running = True
p1_wins = False
p2_wins = False

while running:
    
    while p1_wins:
        
        screen.fill(black)
        p1_wins = game_font.render("P1 wins!", True, white)
        screen.blit(p1_wins, [width / 3, height / 3])
        pygame.display.update()
        
        for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_1:
                        running = False
                        p1_wins = False
                        
                    if event.key == pygame.K_2:
                        p1_score = 0
                        p2_score = 0
                        p1_x_pos = 10
                        p1_y_pos = height / 2 - paddle_height / 2
                        p2_x_pos = width - paddle_width - 10
                        p2_y_pos = height / 2 - paddle_height / 2
                        running = True
                        p1_wins = False

                if event.type == pygame.QUIT:
                    running = False
                    p1_wins = False

    while p2_wins:

        screen.fill(black)
        p2_wins = game_font.render("P2 wins!", True, white)
        screen.blit(p2_wins, [width / 3, height / 3])
        pygame.display.update()

        for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_1:
                        running = False
                        p2_wins = False
                        
                    if event.key == pygame.K_2:
                       p1_score = 0
                       p2_score = 0
                       p1_x_pos = 10
                       p1_y_pos = height / 2 - paddle_height / 2
                       p2_x_pos = width - paddle_width - 10
                       p2_y_pos = height / 2 - paddle_height / 2
                       running = True
                       p2_wins = False

                if event.type == pygame.QUIT:
                    running = False
                    p2_wins = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_w:
                p1_up = True
            if event.key == pygame.K_s:
                p1_down = True
            if event.key == pygame.K_UP:
                p2_up = True
            if event.key == pygame.K_DOWN:
                p2_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                p1_up = False
            if event.key == pygame.K_s:
                p1_down = False
            if event.key == pygame.K_UP:
                p2_up = False
            if event.key == pygame.K_DOWN:
                p2_down = False
    
    if p1_score == 5:
        p1_wins = True
    elif p2_score == 5:
        p2_wins = True
        

    screen.fill(black)
    apply_player_movement()
    apply_ball_movement()
    draw_objects()
    pygame.display.flip()
    pygame.time.wait(delay)