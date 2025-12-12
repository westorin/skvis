from main.repo.teamrepo import TeamRepository
from typing import List, TYPE_CHECKING

if TYPE_CHECKING:
    from main.models.teammodel import Team

class ListOfTeamsLogic():
    """Logic layer responsible for preparing team data for UI. This class does NOT modify team data"""

    def __init__(self) -> None:
        """Initialize the logic layer with access to the team repository."""
        self.team_rep: TeamRepository = TeamRepository()

    def get_all_teams(self) -> List["Team"]:
        """Return all Team objects currently loaded in the repository."""
        return self.team_repo.teams

    def make_list_of_all_teams(self) -> List[List[str]]:
        """Create rows for all teams for UI. Each row contains [team_name, captain, website_url]."""
        all_teams_data = ListOfTeamsLogic().get_all_teams()
        list_of_teams: List[List[str]] = []
        
        # Build one row per team for UI display
        for team in all_teams_data:
            list_of_one_team: List[str] = []
            
            # Shorten team name if needed
            if(len(team.name) > 20):
                list_of_one_team.append(team.name[0:16] + "...")
            else:
                list_of_one_team.append(team.name)

            # Shorten captain if needed
            if(len(team.captain) > 20):
                list_of_one_team.append(team.captain[0:16] + "...")
            else:
                list_of_one_team.append(team.captain)

            # Shorten website URL if needed
            if(len(team.website_url) > 20):
                list_of_one_team.append(team.website_url[0:16] + "...")
            else:
                list_of_one_team.append(team.website_url)

            list_of_teams.append(list_of_one_team)
        
        return list_of_teams
            

    def sort_teams_into_a_list_of_tens(self) -> List[List[List[str]]]:
        """Group team rows into pages of ten for UI display. The last page is padded with empty rows so each page contains exactly 10 rows."""
        list_of_teams = self.make_list_of_all_teams()
        list_of_teams_in_pers_of_tens: List[List[List[str]]] = []
        
        # Calculate how many pages of 10 teams are needed
        if(len(list_of_teams) % 10 == 0):
            ten_teams_counter = (len(list_of_teams) // 10)
        else:
            ten_teams_counter = (len(list_of_teams) // 10)+ 1

        for t in range(0, ten_teams_counter):
            lists_of_ten_teams: List[List[str]] = []

            # At least 10 teams reamining
            if((len(list_of_teams) // 10 ) > 0):
                # Take the first 10 teams and remove them from the list
                for i in range(0,10):
                    lists_of_ten_teams.append(list_of_teams[0])
                    list_of_teams = list_of_teams[1:]                
                    
                list_of_teams_in_pers_of_tens.append(lists_of_ten_teams)
    
            # Fewer than 10 teams remaining (last page)
            elif((len(list_of_teams) // 10 ) == 0 and (len(list_of_teams) % 10) != 0):
                # Add all remaining teams
                for team in list_of_teams:
                    lists_of_ten_teams.append(team)
                    list_of_teams = list_of_teams[1:]

                # Pad the page with empty rows to reach 10 rows
                for i in range(0, (10 - (len(list_of_teams) % 10))):
                    lists_of_ten_teams.append(["", "", ""])
                list_of_teams_in_pers_of_tens.append(lists_of_ten_teams)
                list_of_teams = []

        return list_of_teams_in_pers_of_tens