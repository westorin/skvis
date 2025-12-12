from main.wrappers.datawrapper import DataWrapper
from typing import List, TYPE_CHECKING, Any

if TYPE_CHECKING:
    from main.models.teammodel import Team
    from main.models.playermodel import Player

class TeamLogic():
    """Initialize TeamLogic with access to the shared DataWrapper."""
    def __init__(self, data_wrapper: DataWrapper) -> None:
        self.data_wrapper = DataWrapper()

    def create_list_of_team_info_for_all(self, team_name: str) -> List[List[str]]:
        """Create a list of information for a single team for UI."""
        team = self.data_wrapper.teams.get_team(team_name)
        
        list_of_all_team_info: List[List[str]] = []

        # Team header row
        team_list = [team.name, team.captain, team.website_url]
        list_of_all_team_info.append(team_list)

        # Player rows (public info only)
        for player in team.players:
            list_of_player_info: List[str] = []
            player_info = self.data_wrapper.players.get_by_handle(player)

            # Shorten player name if needed
            if(len(player_info.name) > 20):
                list_of_player_info.append(player_info.name[0:17] + "...")
            else:
                list_of_player_info.append(player_info.name)

            # Shorten username if needed
            if(len(player_info.username) > 20):
                list_of_player_info.append(player_info.username[0:17] + "...")
            else:
                list_of_player_info.append(player_info.username)

            list_of_all_team_info.append(list_of_player_info)

        # Pad missing player rows so UI always shows 5 players
        for i in range(0, (5 - len(team.players))):
            list_of_player_info = ["", ""]

            list_of_all_team_info.append(list_of_player_info)

        return list_of_all_team_info
    
    def create_list_of_teams_all_info(self, team_name: str) -> List[List[Any]]:
        """Create a full (private) information list for a single team."""
        team = self.data_wrapper.teams.get_team(team_name)
        
        list_of_all_team_info: List[List[Any]] = []

        # Team header row (includes player list)
        team_list = [team.name, team.captain, team.website_url, team.players]
        list_of_all_team_info.append(team_list)

        # Detailed player rows
        for player in team.players:
            list_of_player_info: List[Any] = []
            
            player_info = self.data_wrapper.players.get_by_handle(player)
            
            # Player name
            if(len(player_info.name) > 20):
                list_of_player_info.append(player_info.name[0:17] + "...")
            else:
                list_of_player_info.append(player_info.name)

            # Username
            if(len(player_info.username) > 20):
                list_of_player_info.append(player_info.username[0:17] + "...")
            else:
                list_of_player_info.append(player_info.username)

            # Date of birth
            list_of_player_info.append(player_info.dob)

            # Address
            if(len(player_info.address) > 20):
                list_of_player_info.append(player_info.address[0:17] + "...")
            else:
                list_of_player_info.append(player_info.address)

            # Phone number (formatted)
            list_of_player_info.append(player_info.phone[0:3] + "-" + player_info.phone[3:])

            # Email
            if(len(player_info.email) > 20):
                list_of_player_info.append(player_info.email[0:17] + "...")
            else:
                list_of_player_info.append(player_info.email)

            # Website URL
            if(len(player_info.url) > 20):
                list_of_player_info.append(player_info.url[0:17] + "...")
            else:
                list_of_player_info.append(player_info.url)

            list_of_all_team_info.append(list_of_player_info)

        # Pad missing player rows so UI always shows 5 players
        for i in range(0, (5 - len(team.players))):
            list_of_player_info = ["", "", "", "", "", "", ""]

            list_of_all_team_info.append(list_of_player_info)

        return list_of_all_team_info