from dino_runner.components.game import Game
game=Game()
# death_count=0
while  game.running:
    if not game.playing:
        game.show_menu()
        # death_count+=1
        # print(death_count)
