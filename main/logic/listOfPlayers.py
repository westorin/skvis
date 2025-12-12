from main.repo.playerrepo import PlayerRepository
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from main.models.playermodel import Player

class ListOfPlayersLogic():
    """Logic for preparing player data for UI display. This class does NOT modify player data."""

    def __init__(self) -> None:
        """Initialize the logic layer with access to the player repository."""
        self.player_repo: PlayerRepository = PlayerRepository()

    def get_all_players(self) -> list["Player"]:
        """Return all Player objects currently loaded in the repository."""
        return self.player_repo.players
    
    def make_list_of_player_info_for_all(self) -> list[list[str]]:
        """Create rows of players for UI. Each row contains [name, username, team]."""
        all_players_data = ListOfPlayersLogic.get_all_players(self)

        list_of_players: list[list[str]] = []

        for player in all_players_data:
            list_of_one_player: list[str] = []

            if(len(player.name) > 20):
                list_of_one_player.append(player.name[0:17] + "...")
            else:
                list_of_one_player.append(player.name)

            if(len(player.username) > 20):
                list_of_one_player.append(player.username[0:17] + "...")
            else:
                list_of_one_player.append(player.username)
            
            if(len(player.team) > 20):
                list_of_one_player.append(player.team[0:17] + "...")
            else:
                list_of_one_player.append(player.team)

            list_of_players.append(list_of_one_player)
        
        return list_of_players
    
    def sort_players_into_pers_of_ten(self) -> List[List[List[str]]]:
        """Group player rows into pages of ten for UI. The final page is padded with empty rows so each page always contains exactly 10 rows."""
        # Get formatted player rows
        list_of_players = ListOfPlayersLogic.make_list_of_player_info_for_all(self)

        list_of_players_in_pers_of_ten: List[List[List[str]]] = []

        # Calculate how many pages of 10 players are needed
        if(len(list_of_players) % 10 == 0):
            ten_players_counter = len(list_of_players) // 10
        else:
            ten_players_counter = (len(list_of_players) // 10) + 1


        for p in range(0, ten_players_counter):
            list_of_ten_players: List[List[str]] = []

            # Check if there is still a set of ten players
            if((len(list_of_players) // 10) > 0):

                # Take the first 10 players and remove them from the list
                for i in range(0, 10):
                    list_of_ten_players.append(list_of_players[0])
                    list_of_players = list_of_players[1:]

                list_of_players_in_pers_of_ten.append(list_of_ten_players)
            
            # Check if there are less than ten players left and if there are more than 0 players left
            elif((len(list_of_players) // 10) == 0 and (len(list_of_players) % 10) != 0):
                
                # Add all remaining players
                for player in list_of_players:
                    list_of_ten_players.append(player)
                    list_of_players = list_of_players[1:]
                    
                # Pad the page with empty rows to reach 10 rows
                for i in range(0, (10 - len(list_of_players))):
                    list_of_ten_players.append(["","",""])
                list_of_players_in_pers_of_ten.append(list_of_ten_players)
                

        return list_of_players_in_pers_of_ten
                    