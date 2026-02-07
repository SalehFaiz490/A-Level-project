import pygame


class Player(pygame.sprite.Sprite):
    """
    Represents the player character.
    Handles movement, collision, scoring, and player state.
    """
    def __init__(self, x, y):
        super().__init__()

        # Load player sprite and set up collision rectangle
        self.image = pygame.image.load(
            "Map tiles/player_image.png"
        ).convert_alpha()
        self.rect = self.image.get_rect()

        # Position and movement vectors
        self.pos = pygame.Vector2(x, y)
        self.dir = pygame.Vector2(0, 0)  # Direction persists between frames
        self.speed = 500

        # Player state
        self.moving = False
        self.score = 0
        self.living = True

        # Player account data (used for leaderboard / login)
        self.username = ""
        self.user_id = None
        self.recent_score = 0
        self.high_score = 0

        # Current difficulty mode
        self.diffuclity_mode = "Medium"

    def update_score(self, coin_rects, group):
        """
        Checks for collisions with coins and updates the player's score.
        """
        for coin in coin_rects[:]:
            if self.rect.colliderect(coin.rect):
                coin_rects.remove(coin)
                group.remove(coin)
                self.score += 1

    def set_direction(self, keys):
        """
        Sets the movement direction based on keyboard input.
        Direction is only updated when the player is not already moving.
        """
        if keys[pygame.K_w]:
            # Move up (y decreases in pygame)
            self.dir = pygame.Vector2(0, -1)

        elif keys[pygame.K_s]:
            # Move down
            self.dir = pygame.Vector2(0, 1)

        elif keys[pygame.K_a]:
            # Move left
            self.dir = pygame.Vector2(-1, 0)

        elif keys[pygame.K_d]:
            # Move right
            self.dir = pygame.Vector2(1, 0)

    def move_and_collide(self, dt, walls):
        """
        Moves the player and resolves collisions with walls.
        Movement is split into X and Y axes to prevent clipping.
        """

        # --- Horizontal movement ---
        self.pos.x += self.dir.x * self.speed * dt
        self.rect.x = self.pos.x

        for wall in walls:
            if self.rect.colliderect(wall):
                # Snap player to the wall and stop horizontal movement
                if self.dir.x > 0:
                    self.rect.right = wall.left
                elif self.dir.x < 0:
                    self.rect.left = wall.right

                self.moving = False
                self.pos.x = self.rect.x
                self.dir.x = 0

        # --- Vertical movement ---
        self.pos.y += self.dir.y * self.speed * dt
        self.rect.y = self.pos.y

        for wall in walls:
            if self.rect.colliderect(wall):
                # Snap player to the wall and stop vertical movement
                if self.dir.y > 0:
                    self.rect.bottom = wall.top
                elif self.dir.y < 0:
                    self.rect.top = wall.bottom

                self.moving = False
                self.pos.y = self.rect.y
                self.dir.y = 0

        # Update movement state
        if self.dir != (0, 0):
            self.moving = True

    def check_player_living(self, lava_rect, spikes):
        """
        Checks whether the player has collided with a hazard.
        Updates player state and recent score if the player dies.
        """
        if self.rect.colliderect(lava_rect):
            self.living = False
            self.recent_score = self.score

        for spike in spikes:
            if self.rect.colliderect(spike):
                self.living = False
                self.recent_score = self.score
