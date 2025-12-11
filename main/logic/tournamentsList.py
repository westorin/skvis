from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper


class TournamentsListLogic():
    
    def sort_past_tournaments_list(self):
        data = DataWrapper()
        logic = LogicWrapper(data)
        tm = logic.tournament_manager

        list_of_tournaments = tm.list_tournaments_basic_info_by_timeframe("Past")

        list_of_tournaments_in_pers_of_tens = []
        
        if(len(list_of_tournaments) % 10 == 0):
            ten_tournaments_counter = (len(list_of_tournaments) // 10)
        else:
            ten_tournaments_counter = (len(list_of_tournaments) // 10)+ 1

        for t in range(0, ten_tournaments_counter):
            lists_of_ten_tournaments = []
            # Here we check if the list of the all teams has 10 teams to add
            if((len(list_of_tournaments) // 10 ) > 0):
                # Here we have a for loop that counts ten so we can add the ten teams to a list and remove the on you add
                for i in range(0,10):
                    lists_of_ten_tournaments.append(list_of_tournaments[0])
                    list_of_tournaments = list_of_tournaments[1:]                
                    
                list_of_tournaments_in_pers_of_tens.append(lists_of_ten_tournaments)
    
            # Here we check if the list of all teams has less then 10 teams
            elif((len(list_of_tournaments) // 10 ) == 0 and (len(list_of_tournaments) % 10) != 0):
                for team in list_of_tournaments:
                    lists_of_ten_tournaments.append(team)
                    list_of_tournaments = list_of_tournaments[1:]

                for i in range(0, (10 - (len(list_of_tournaments) % 10))):
                    lists_of_ten_tournaments.append(["", "", ""])
                list_of_tournaments_in_pers_of_tens.append(lists_of_ten_tournaments)
                list_of_tournaments = []

        return list_of_tournaments_in_pers_of_tens
    
    def sort_on_going_tournaments_list(self):
        data = DataWrapper()
        logic = LogicWrapper(data)
        tm = logic.tournament_manager

        list_of_tournaments = tm.list_tournaments_basic_info_by_timeframe("Ongoing")

        list_of_tournaments_in_pers_of_tens = []
        
        if(len(list_of_tournaments) % 10 == 0):
            ten_tournaments_counter = (len(list_of_tournaments) // 10)
        else:
            ten_tournaments_counter = (len(list_of_tournaments) // 10)+ 1

        for t in range(0, ten_tournaments_counter):
            lists_of_ten_tournaments = []
            # Here we check if the list of the all teams has 10 teams to add
            if((len(list_of_tournaments) // 10 ) > 0):
                # Here we have a for loop that counts ten so we can add the ten teams to a list and remove the on you add
                for i in range(0,10):
                    lists_of_ten_tournaments.append(list_of_tournaments[0])
                    list_of_tournaments = list_of_tournaments[1:]                
                    
                list_of_tournaments_in_pers_of_tens.append(lists_of_ten_tournaments)
    
            # Here we check if the list of all teams has less then 10 teams
            elif((len(list_of_tournaments) // 10 ) == 0 and (len(list_of_tournaments) % 10) != 0):
                for team in list_of_tournaments:
                    lists_of_ten_tournaments.append(team)
                    list_of_tournaments = list_of_tournaments[1:]

                for i in range(0, (10 - (len(list_of_tournaments) % 10))):
                    lists_of_ten_tournaments.append(["", "", ""])
                list_of_tournaments_in_pers_of_tens.append(lists_of_ten_tournaments)
                list_of_tournaments = []

        return list_of_tournaments_in_pers_of_tens
    
    def sort_future_tournaments_list(self):
        data = DataWrapper()
        logic = LogicWrapper(data)
        tm = logic.tournament_manager

        list_of_tournaments = tm.list_tournaments_basic_info_by_timeframe("Future")

        list_of_tournaments_in_pers_of_tens = []
        
        if(len(list_of_tournaments) % 10 == 0):
            ten_tournaments_counter = (len(list_of_tournaments) // 10)
        else:
            ten_tournaments_counter = (len(list_of_tournaments) // 10)+ 1

        for t in range(0, ten_tournaments_counter):
            lists_of_ten_tournaments = []
            # Here we check if the list of the all teams has 10 teams to add
            if((len(list_of_tournaments) // 10 ) > 0):
                # Here we have a for loop that counts ten so we can add the ten teams to a list and remove the on you add
                for i in range(0,10):
                    lists_of_ten_tournaments.append(list_of_tournaments[0])
                    list_of_tournaments = list_of_tournaments[1:]                
                    
                list_of_tournaments_in_pers_of_tens.append(lists_of_ten_tournaments)
    
            # Here we check if the list of all teams has less then 10 teams
            elif((len(list_of_tournaments) // 10 ) == 0 and (len(list_of_tournaments) % 10) != 0):
                for team in list_of_tournaments:
                    lists_of_ten_tournaments.append(team)
                    list_of_tournaments = list_of_tournaments[1:]

                for i in range(0, (10 - (len(list_of_tournaments) % 10))):
                    lists_of_ten_tournaments.append(["", "", ""])
                list_of_tournaments_in_pers_of_tens.append(lists_of_ten_tournaments)
                list_of_tournaments = []

        return list_of_tournaments_in_pers_of_tens