from dino_runner.components.game import Game
game=Game()
death_count=0
while  not game.playing:
    game.show_menu(death_count)
    if not game.running:
        death_count+=1
        print(death_count)
# if __name__ == "__main__":
#      game=Game()
#      game.run()
#      print("hello there...")
