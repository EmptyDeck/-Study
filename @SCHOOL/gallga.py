import pygame
import random

# Pygame 초기화
pygame.init()

# 화면 설정
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Galaga Style Game with Highscore")

# 색상
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


try:  # 이미지 불러오기 성공
    # 탱크와 몬스터 이미지 로드
    tank_image = pygame.image.load('data/wing.png')
    monster_image = pygame.image.load('data/monster.png')

    # 이미지를 원하는 크기로 조정
    tank_image = pygame.transform.scale(tank_image, (50, 50))  # 예시 크기
    monster_image = pygame.transform.scale(monster_image, (30, 30))  # 예시 크기
except:  # 이미지 못불러왔을때
    pass


background_image_path = 'data/space.jpg'
background_image = pygame.image.load(background_image_path)
background_image = pygame.transform.scale(background_image, (width, height))


# 탱크 설정
tank_pos = [width // 2, height - 60]
tank_speed = 5
tank_rect = tank_image.get_rect(center=tank_pos)

# 총알 설정
bullets = []
monster_bullets = []
bullet_speed = 7
bullets_fired = 0
monster_count = 10

# 몬스터 설정
monsters = []
monster_speed = 0  # 몬스터의 속도
for i in range(monster_count):
    x = random.randint(0, width - monster_image.get_width())
    random_number = random.randint(0, 1)  # 0 or 100
    y = random_number * 100
    monster_rect = monster_image.get_rect(topleft=(x, y))
    monsters.append(monster_rect)

print(monsters)

# 점수 설정
score = 0
high_score = 999

# 게임 재시작 함수


def restart_game():
    global monsters, bullets, monster_bullets, score, tank_rect
    tank_rect.center = (width // 2, height - 60)
    bullets = []
    monster_bullets = []
    monsters = []
    score = 0
    for i in range(monster_count):
        x = random.randint(0, width - 30)
        random_number = random.randint(0, 1)  # 1 or 100
        y = random_number * 100
        monster_rect = monster_image.get_rect(topleft=(x, y))
        monsters.append(monster_rect)


# 게임 루프
running = True
game_over = False


cnt = 0
while running:

    # time function
    cnt = cnt + 1
    if cnt % 200 == 0:
        print(cnt)
        print("faster")
        monster_speed = monster_speed + 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if game_over and event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            restart_game()
    screen.blit(background_image, (0, 0))

    if not game_over:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            tank_rect.move_ip(-tank_speed, 0)
        if keys[pygame.K_d]:
            tank_rect.move_ip(tank_speed, 0)
        if keys[pygame.K_k] and len(bullets) < 10:  # 쏘는것
            bullet_rect = pygame.Rect(tank_rect.centerx, tank_rect.top, 5, 10)
            bullets.append(bullet_rect)
            bullets_fired += 1  # 총알 발사 수 증가

        # 총알 업데이트
        for bullet in bullets[:]:
            bullet.move_ip(0, -bullet_speed)
            if bullet.bottom < 0:
                bullets.remove(bullet)

        # 몬스터 총알 업데이트
        for bullet in monster_bullets[:]:
            bullet.move_ip(0, bullet_speed)
            if bullet.top > height:
                monster_bullets.remove(bullet)
            if bullet.colliderect(tank_rect):
                game_over = True  # 주인공이 맞으면 게임 오버

        # 몬스터 충돌 검사
        for monster in monsters[:]:
            for bullet in bullets[:]:
                if bullet.colliderect(monster):
                    try:
                        bullets.remove(bullet)
                        monsters.remove(monster)
                    except:
                        pass
                    print(monsters)

                    if not monsters:
                        game_over = True  # 게임 오버 상태로 변경
                        win = True  # 승리 상태 설정

            if random.randint(0, 1000) < 5:  # 몬스터가 총을 쏘는 확률
                monster_bullet = pygame.Rect(
                    monster.centerx, monster.bottom, 5, 10)
                monster_bullets.append(monster_bullet)
            # 몬스터 랜덤 움직임
            monster.move_ip(random.choice([-monster_speed, monster_speed]),
                            random.choice([0, 0]))
            monster.clamp_ip(screen.get_rect())  # 화면 밖으로 나가지 않도록

        # 화면 업데이트
        screen.blit(tank_image, tank_rect)
        for bullet in bullets:
            pygame.draw.rect(screen, WHITE, bullet)
        for bullet in monster_bullets:
            pygame.draw.rect(screen, RED, bullet)
        for monster in monsters:
            screen.blit(monster_image, monster)

        # 점수 표시
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f'Score: {score}', True, WHITE)
        high_score_text = font.render(f'Highscore: {high_score}', True, WHITE)
        screen.blit(score_text, (10, 10))
        screen.blit(high_score_text, (10, 50))
    else:
        font = pygame.font.SysFont(None, 74)
        if 'win' in locals() and win:
            game_over_text = font.render('YOU WIN!', True, RED)
            bullets_text = font.render(
                f'Bullets Used: {bullets_fired}', True, WHITE)
            if bullets_fired < high_score:
                high_score = bullets_fired  # 하이스코어 갱신
            bullets_rect = bullets_text.get_rect(
                center=(width // 2, height // 2 + 100))
            screen.blit(bullets_text, bullets_rect)
            restart_text = font.render('Press Space to Restart', True, WHITE)
            restart_rect = restart_text.get_rect(
                center=(width // 2, height // 4 + 150))
            screen.blit(restart_text, restart_rect)
            cnt = 0
            monster_speed = 0
        else:
            game_over_text = font.render('GAME OVER', True, RED)
            game_over_rect = game_over_text.get_rect(
                center=(width // 2, height // 2))
            screen.blit(game_over_text, game_over_rect)
            restart_text = font.render('Press Space to Restart', True, WHITE)
            restart_rect = restart_text.get_rect(
                center=(width // 2, height // 2 + 150))
            screen.blit(restart_text, restart_rect)
            cnt = 0
            monster_speed = 0

    pygame.display.flip()
    pygame.time.delay(30)

pygame.quit()
