from main.UI.mainUI import MainUI
from main.UI.homepage_UI import homepageUI 
from main.UI.pickTimeOfTournament import PickTimeOfTournamntsUI

run_program = MainUI(homepageUI, PickTimeOfTournamntsUI)
run_program.run()