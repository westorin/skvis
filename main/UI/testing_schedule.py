# main/test_schedule.py

from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

def main():
    data = DataWrapper()
    logic = LogicWrapper(data)

    tm = logic.tournament_manager

    tournaments = tm.list_tournaments()
    if not tournaments:
        print("No tournaments found.")
        return

    print("=== TOURNAMENTS FOUND ===")
    for idx, t in enumerate(tournaments, start=1):
        print(f"{idx}. {t.name}  (location={t.location}, start={t.start})")

    print("\n=== SCHEDULE PER TOURNAMENT ===")
    for t in tournaments:
        print(f"\n##### {t.name} #####")
        try:
            pages = tm.get_schedule_pages(t.name)
        except Exception as e:
            print(f"Error building schedule for '{t.name}': {e}")
            continue

        if not pages:
            print("  (no matches for this tournament)")
            continue

        for page_idx, page in enumerate(pages, start=1):
            print(f"\n  -- Page {page_idx} --")
            for row in page:
                # row = [game_nr, team_a, team_b, date, time, location]
                print("  ", row)

if __name__ == "__main__":
    main()
