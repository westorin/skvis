from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper
from typing import List

class TournamentsListLogic():
    """Logic for preparing tournament lists for UI."""
    def sort_past_tournaments_list(self) -> List[List[List[str]]]:
        data = DataWrapper()
        logic = LogicWrapper(data)
        tm = logic.tournament_manager

        list_of_tournaments: List[List[str]] = tm.list_tournaments_basic_info_by_timeframe("Past")
        list_of_tournaments_in_pers_of_tens: List[List[List[str]]] = []
        
        # Determine how many pages of 10 we need
        if (len(list_of_tournaments) % 10 == 0):
            ten_tournaments_counter = (len(list_of_tournaments) // 10)
        else:
            ten_tournaments_counter = (len(list_of_tournaments) // 10)+ 1

        for t in range(0, ten_tournaments_counter):
            lists_of_ten_tournaments: List[List[str]] = []

            # Check if the list of the all teams has 10 teams to add
            if ((len(list_of_tournaments) // 10 ) > 0):
                for i in range(0,10):
                    lists_of_ten_tournaments.append(list_of_tournaments[0])
                    list_of_tournaments = list_of_tournaments[1:]                
                list_of_tournaments_in_pers_of_tens.append(lists_of_ten_tournaments)
    
            # Partial last page: pad with empty placeholder rows
            elif ((len(list_of_tournaments) // 10 ) == 0 and (len(list_of_tournaments) % 10) != 0):
                for team in list_of_tournaments:
                    lists_of_ten_tournaments.append(team)
                    list_of_tournaments = list_of_tournaments[1:]

                for i in range(0, (10 - (len(list_of_tournaments) % 10))):
                    lists_of_ten_tournaments.append(["", "", ""])

                list_of_tournaments_in_pers_of_tens.append(lists_of_ten_tournaments)
                list_of_tournaments = []

        return list_of_tournaments_in_pers_of_tens
    
    def sort_on_going_tournaments_list(self) -> List[List[List[str]]]:
        """Returns pages of 10 tournament rows for Ongoing tournaments."""
        data = DataWrapper()
        logic = LogicWrapper(data)
        tm = logic.tournament_manager

        list_of_tournaments = tm.list_tournaments_basic_info_by_timeframe("Ongoing")
        list_of_tournaments_in_pers_of_tens: List[List[List[str]]] = []
        
        if (len(list_of_tournaments) % 10 == 0):
            ten_tournaments_counter = (len(list_of_tournaments) // 10)
        else:
            ten_tournaments_counter = (len(list_of_tournaments) // 10)+ 1

        for t in range(0, ten_tournaments_counter):
            lists_of_ten_tournaments: List[List[str]] = []

            if ((len(list_of_tournaments) // 10 ) > 0):
                for i in range(0,10):
                    lists_of_ten_tournaments.append(list_of_tournaments[0])
                    list_of_tournaments = list_of_tournaments[1:]                
                list_of_tournaments_in_pers_of_tens.append(lists_of_ten_tournaments)
    
            elif ((len(list_of_tournaments) // 10 ) == 0 and (len(list_of_tournaments) % 10) != 0):
                for team in list_of_tournaments:
                    lists_of_ten_tournaments.append(team)
                    list_of_tournaments = list_of_tournaments[1:]

                for i in range(0, (10 - (len(list_of_tournaments) % 10))):
                    lists_of_ten_tournaments.append(["", "", ""])

                list_of_tournaments_in_pers_of_tens.append(lists_of_ten_tournaments)
                list_of_tournaments = []

        return list_of_tournaments_in_pers_of_tens
    
    def sort_future_tournaments_list(self) -> List[List[List[str]]]:
        """Returns pages of 10 tournament rows for Future tournaments."""
        data = DataWrapper()
        logic = LogicWrapper(data)
        tm = logic.tournament_manager

        list_of_tournaments: List[List[str]] = tm.list_tournaments_basic_info_by_timeframe("Future")
        list_of_tournaments_in_pers_of_tens: List[List[List[str]]] = []
        
        if (len(list_of_tournaments) % 10 == 0):
            ten_tournaments_counter = (len(list_of_tournaments) // 10)
        else:
            ten_tournaments_counter = (len(list_of_tournaments) // 10)+ 1

        for t in range(0, ten_tournaments_counter):
            lists_of_ten_tournaments: List[List[str]] = []

            if ((len(list_of_tournaments) // 10 ) > 0):
                for i in range(0,10):
                    lists_of_ten_tournaments.append(list_of_tournaments[0])
                    list_of_tournaments = list_of_tournaments[1:]                
                    
                list_of_tournaments_in_pers_of_tens.append(lists_of_ten_tournaments)
    
            elif ((len(list_of_tournaments) // 10 ) == 0 and (len(list_of_tournaments) % 10) != 0):
                for team in list_of_tournaments:
                    lists_of_ten_tournaments.append(team)
                    list_of_tournaments = list_of_tournaments[1:]

                for i in range(0, (10 - (len(list_of_tournaments) % 10))):
                    lists_of_ten_tournaments.append(["", "", ""])
                    
                list_of_tournaments_in_pers_of_tens.append(lists_of_ten_tournaments)
                list_of_tournaments = []

        return list_of_tournaments_in_pers_of_tens