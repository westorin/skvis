from main.logic.clearScreenInTerminal import clear_screen

class AddTeamUI():

    def print_add_team(self):
        

        name_of_team = ""
        capt_username = ""
        team_url = ""
        team_tag = "****"

        capt_name = ""
        capt_dob = ""
        capt_address = ""
        capt_phone = ""
        capt_email = ""
        capt_url = ""

        player_1_username = ""
        player_1_name = ""
        player_1_dob = ""
        player_1_address = ""
        player_1_phone = ""
        player_1_email = ""
        player_1_url = ""

        player_2_username = ""
        player_2_name = ""
        player_2_dob = ""
        player_2_address = ""
        player_2_phone = ""
        player_2_email = ""
        player_2_url = ""

        header_text = """
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t+-------------------------+\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t| ╔═╗ ┬┐ ┬┐  ╔╦╗┌─┐┌─┐┌┬┐ |\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t| ╠═╣ ││ ││   ║ ├┤ ├─┤│││ |\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t| ╩ ╩─┴┘─┴┘   ╩ └─┘┴ ┴┴ ┴ |\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t+-------------------------+\t\t\t\t\t\t\t\t\t\t|"""

        team_info =f"""
|\t\t\t\t\t\t+----------------------+----------------------+----------------------+-----------------+\t\t\t\t\t|
|\t\t\t\t\t\t| Name of team         | Username of capt.    | Url.                 | Team TAG [****] |\t\t\t\t\t|
|\t\t\t\t\t\t+======================+======================+======================+=================+\t\t\t\t\t|
|\t\t\t\t\t\t| {name_of_team + " "*(20 -len(name_of_team))
                } | {capt_username + " "*(20 - len(capt_username))
                     } | {team_url + " "*(20 -len(team_url))
                          } | [{team_tag}]          |\t\t\t\t\t|
|\t\t\t\t\t\t+----------------------+----------------------+----------------------+-----------------+\t\t\t\t\t|
"""
        players_info = f"""
|\t\t\t+----------------------+----------------------+---------------+----------------------+----------+----------------------+----------------------+\t\t\t|
|\t\t\t| Username             | Name                 | Date of birth | Address              | Phone    | E-mail               | URL.                 |\t\t\t|
|\t\t\t+======================+======================+===============+======================+==========+======================+======================+\t\t\t|
|\t\t\t|                      |                      |               |                      |          |                      |                      |\t\t\t|
|\t\t\t+----------------------+----------------------+---------------+----------------------+----------+----------------------+----------------------+\t\t\t|
|\t\t\t|                      |                      |               |                      |          |                      |                      |\t\t\t|
|\t\t\t+----------------------+----------------------+---------------+----------------------+----------+----------------------+----------------------+\t\t\t|
|\t\t\t|                      |                      |               |                      |          |                      |                      |\t\t\t|
|\t\t\t+----------------------+----------------------+---------------+----------------------+----------+----------------------+----------------------+\t\t\t|
"""
        clear_screen()

        print(header_text)
        print(team_info)
        print(players_info)
        choice = input()
        if(choice.lower() == "q"):
            return "QUIT"
        elif(choice.lower() == "b"):
            return "BACK"