from game_characters import Coin


def circles_collide(x1, y1, r1, x2, y2, r2):
    """
    Returns True if two circles collide.

    Args:
        x1, y1: Center of circle 1
        r1: Radius of circle 1
        x2, y2: Center of circle 2
        r2: Radius of circle 2
    """
    dx = x2 - x1
    dy = y2 - y1
    distance_squared = dx * dx + dy * dy
    sum_radii_squared = (r1 + r2) ** 2
    return distance_squared <= sum_radii_squared


def enemy_collides(enemies_list, player):
    for enemy in enemies_list:
        if circles_collide(
            enemy.x_pos,
            enemy.y_pos,
            enemy.radius,
            player.x_pos,
            player.y_pos,
            player.radius,
        ):
            return True


def check_coin_collisions(coin_list, player):
    for coin in coin_list:
        if circles_collide(
            coin.x_pos,
            coin.y_pos,
            coin.radius,
            player.x_pos,
            player.y_pos,
            player.radius,
        ):
            coin.destroy()
            player.collected_coins += 1
