import pygame
import game_graphics.UI.UI
import Main
import game_graphics.Sprite


class PlayerInfoBar:
    def __init__(self):
        self.font = pygame.font.SysFont(game_graphics.UI.UI.UI.user_interface_font, game_graphics.UI.UI.UI.user_interface_font_size)

        self.background = pygame.Surface((100, 64), pygame.SRCALPHA)
        self.background.fill((0, 0, 0, 170))

        self.text_color = (255, 255, 255)

        self.player_hp_count = Main.player.hp
        self.player_max_hp_count = Main.player.max_hp
        self.player_xp_count = Main.player.xp
        self.player_level_count = Main.player.lvl

        self.player_hp_text = self.font.render(str(self.player_hp_count) + " | " + str(self.player_max_hp_count), 0, (150 * (1 - Main.player.hp / Main.player.max_hp), 150 * Main.player.hp / Main.player.max_hp, 0))
        self.player_xp_text = self.font.render(str(self.player_xp_count), 0, self.text_color)
        self.player_level_text = self.font.render(str(self.player_level_count), 0, self.text_color)

    def render(self, display):
        if Main.player.hp / Main.player.max_hp > 0.6:
            display.canvas.blit(game_graphics.Sprite.player_icon.pic, (Main.window_width - 184, 20))
        elif Main.player.hp / Main.player.max_hp > 0.3:
            display.canvas.blit(game_graphics.Sprite.player_icon_injured_1.pic, (Main.window_width - 184, 20))
        elif Main.player.hp / Main.player.max_hp > 0:
            display.canvas.blit(game_graphics.Sprite.player_icon_injured_2.pic, (Main.window_width - 184, 20))
        else:
            display.canvas.blit(game_graphics.Sprite.player_icon_death.pic, (Main.window_width - 184, 20))

        display.canvas.blit(self.background, (Main.window_width - 120, 20))

        display.canvas.blit(game_graphics.Sprite.hp_icon.pic, (Main.window_width - 116, 23))
        display.canvas.blit(game_graphics.Sprite.xp_icon.pic, (Main.window_width - 116, 44))
        display.canvas.blit(game_graphics.Sprite.level_icon.pic, (Main.window_width - 116, 65))

        if self.player_hp_count != Main.player.hp or self.player_max_hp_count != Main.player.max_hp:
            self.player_hp_count = Main.player.hp
            self.player_max_hp_count = Main.player.max_hp
            self.player_hp_text = self.font.render(str(self.player_hp_count) + " | " + str(self.player_max_hp_count), 0, (150 * (1 - Main.player.hp / Main.player.max_hp), 150 * Main.player.hp / Main.player.max_hp, 0))

        if self.player_xp_count != Main.player.xp:
            self.player_xp_count = Main.player.xp
            self.player_xp_text = self.font.render(str(self.player_xp_count), 0, self.text_color)

        if self.player_level_count != Main.player.lvl:
            self.player_level_count = Main.player.lvl
            self.player_level_text = self.font.render(str(self.player_level_count), 0, self.text_color)

        display.canvas.blit(self.player_hp_text, (Main.window_width - 97, 25))
        display.canvas.blit(self.player_xp_text, (Main.window_width - 97, 46))
        display.canvas.blit(self.player_level_text, (Main.window_width - 97, 67))


    def update(self):
        pass