from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

# Finnur það í logic layer undir "tournamentmanager.py" í TournamentManager classanum
# Getur kallað á það með:
# logic.tournament_manager.list_tournaments_basic_info()
# logic.tournament_manager.list_tournaments_basic_info_by_timeframe("Past")
# logic.tournament_manager.list_tournaments_basic_info_by_timeframe("Ongoing")
# logic.tournament_manager.list_tournaments_basic_info_by_timeframe("Future")

# og það returnar lista [name, start_date, end_date]

# Kannski hægt að skrifa það einhvernveginn svona fyrir UI:

# tm = logic.tournament_manager

# if choice == "1":
    # rows = tm.list_tournaments_basic_info_by_timeframe("Past")
# elif choice == "2":
    # rows = tm.list_tournaments_basic_info_by_timeframe("Ongoing")
# elif choice == "3":
    # rows = tm.list_tournaments_basic_info_by_timeframe("Future")

# for name, start, end in rows:
    # print(name, start, end)
    

def main() -> None:
    data = DataWrapper()
    logic = LogicWrapper(data)
    tm = logic.tournament_manager

    print("\n=== ALL TOURNAMENTS ===")
    all_rows = tm.list_tournaments_basic_info()
    for row in all_rows:
        print(row)

    # Past
    print("\n=== PAST TOURNAMENTS ===")
    past = tm.list_tournaments_basic_info_by_timeframe("Past")
    for row in past:
        print(row)

    # Ongoing
    print("\n=== ONGOING TOURNAMENTS ===")
    ongoing = tm.list_tournaments_basic_info_by_timeframe("Ongoing")
    for row in ongoing:
        print(row)

    # Future
    print("\n=== FUTURE TOURNAMENTS ===")
    future = tm.list_tournaments_basic_info_by_timeframe("Future")
    for row in future:
        print(row)


if __name__ == "__main__":
    main()
