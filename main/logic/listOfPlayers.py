from main.repo.playerrepo import PlayerRepository
from typing import List
class ListOfPlayersLogic():
    def __init__(self):
        self.player_repo = PlayerRepository()

    def get_all_players(self):
        return self.player_repo.players
    
    def make_list_of_player_info_for_all(self) -> List:
        all_players_data = ListOfPlayersLogic.get_all_players(self)

        list_of_players = []

        for player in all_players_data:
            list_of_one_player = []
            list_of_one_player.append(player.name)
            list_of_one_player.append(player.username)
            list_of_one_player.append(player.team)

            list_of_players.append(list_of_one_player)
        
        return list_of_players
    
    def sort_players_into_pers_of_ten(self) -> List:
        # Here we get a list of all the players in our CSV file
        list_of_players = ListOfPlayersLogic.make_list_of_player_info_for_all(self)

        list_of_players_in_pers_of_ten =[]

        # Here we check if the player count is 
        if(len(list_of_players) % 10 == 0):
            ten_players_counter = len(list_of_players) // 10
        else:
            ten_players_counter = (len(list_of_players) // 10) + 1


        for p in range(0, ten_players_counter):
            list_of_ten_players = []
            # Here we check if there are still a set of ten players
            if((len(list_of_players) // 10) > 0):

                # Here we add a player to a our ten players list and then remove him from our all players list 
                for i in range(0, 10):
                    list_of_ten_players.append(list_of_players[0])
                    list_of_players = list_of_players[1:]
                list_of_players_in_pers_of_ten.append(list_of_ten_players)
            
            # Here we check if there are less the ten players left and if there are more then none players left
            elif((len(list_of_players) // 10) == 0 and (len(list_of_players) % 10) != 0):
                
                # Here we add all the player left
                for player in list_of_players:
                    list_of_ten_players.append(player)
                    list_of_players = list_of_players[1:]
                    
                # Here we pad the end of the list
                for i in range(0, (10 - len(list_of_players))):
                    list_of_ten_players.append(["","",""])
                list_of_players_in_pers_of_ten.append(list_of_ten_players)
                

        return list_of_players_in_pers_of_ten
                    