from main.logic.clearScreenInTerminal import clear_screen
from main.wrappers.datawrapper import DataWrapper
from main.models.playermodel import Player
from main.models.teammodel import Team
import math

class AddTeamUI():
    def __init__(self, logic):
        self.logic = logic

    def save_new_team_and_players(
        self,
        data: DataWrapper,
        name_of_team: str,
        team_url: str,
        tag: str,
        capt_username: str,
        capt_name: str,
        capt_dob: str,
        capt_address: str,
        capt_phone: str,
        capt_email: str,
        capt_url: str,
        player_1_username: str,
        player_1_name: str,
        player_1_dob: str,
        player_1_address: str,
        player_1_phone: str,
        player_1_email: str,
        player_1_url: str,
        player_2_username: str,
        player_2_name: str,
        player_2_dob: str,
        player_2_address: str,
        player_2_phone: str,
        player_2_email: str,
        player_2_url: str,
    ) -> None:
        """Create a new team + 3 players and save tem to CSV."""

        # Create Team
        team_id = data.teams.get_next_id()
        player_usernames = [capt_username, player_1_username, player_2_username]

        team = Team(
            str(team_id),
            name_of_team,
            capt_username,
            player_usernames,
            team_url,
            tag,
            wins=0,
            losses=0,
        )
        data.teams.add_team(team)

        # Helper to add a single player
        def add_player(username, name, dob, address, phone, email, url):
            player_id = data.players.get_next_id()
            player = Player(
                str(player_id),
                name,
                dob,
                address,
                phone,
                email,
                url,
                username,
                name_of_team,
            )
            data.players.add_player(player) # This also calls save_players()

        add_player(capt_username, capt_name, capt_dob, capt_address, capt_phone, capt_email, capt_url)
        add_player(player_1_username, player_1_name, player_1_dob, player_1_address, player_1_phone, player_1_email, player_1_url)
        add_player(player_2_username, player_2_name, player_2_dob, player_2_address, player_2_phone, player_2_email, player_2_url)

    def print_add_team(self):
        
        data = DataWrapper()

        name_of_team = ""
        capt_username = ""
        team_url = ""
        tag = "****"

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

        enter_what = "Enter the name of the team..."
        isError = False
        all_team_info_in = False
        error_text = "Error erro err er e"

        header_text = """+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t+-------------------------+\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t| ╔═╗ ┬┐ ┬┐  ╔╦╗┌─┐┌─┐┌┬┐ |\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t| ╠═╣ ││ ││   ║ ├┤ ├─┤│││ |\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t| ╩ ╩─┴┘─┴┘   ╩ └─┘┴ ┴┴ ┴ |\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t+-------------------------+\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""

        center_text = """|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""


        while True:

            team_info =f"""|\t\t\t\t\t\t+----------------------+----------------------+----------------------+-----------------+\t\t\t\t\t|
|\t\t\t\t\t\t| Name of team         | Username of capt.    | Url.                 | Team TAG        |\t\t\t\t\t|
|\t\t\t\t\t\t+======================+======================+======================+=================+\t\t\t\t\t|
|\t\t\t\t\t\t| {name_of_team + " "*(20 -len(name_of_team))
                } | {capt_username + " "*(20 - len(capt_username))
                     } | {team_url + " "*(20 -len(team_url))
                          } |     [{tag}]      |\t\t\t\t\t|
|\t\t\t\t\t\t+----------------------+----------------------+----------------------+-----------------+\t\t\t\t\t|"""
            players_info = f"""|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t+----------------------+----------------------+---------------+----------------------+----------+----------------------+----------------------+\t\t\t|
|\t\t| Username             | Name                 | Date of birth | Address              | Phone    | E-mail               | URL.                 |\t\t\t|
|\t\t+======================+======================+===============+======================+==========+======================+======================+\t\t\t|
|\t\t| {capt_username + " "*(20 - len(capt_username))
        } | {capt_name + " "*(20 - len(capt_name))
             } | {capt_dob + " "*(13 - len(capt_dob))
                  } | {capt_address + " "*(20 - len(capt_address))
                       } | {capt_phone + " "*(8 - len(capt_phone))
                            } | {capt_email + " "*(20 - len(capt_email))
                                 } | {capt_url + " "*(20 - len(capt_url))} |\t\t\t|
|\t\t+----------------------+----------------------+---------------+----------------------+----------+----------------------+----------------------+\t\t\t|
|\t\t| {player_1_username + " "*(20 - len(player_1_username))
        } | {player_1_name + " "*(20 - len(player_1_name))
             } | {player_1_dob + " "*(13 - len(player_1_dob))
                  } | {player_1_address + " "*(20 - len(player_1_address))
                       } | {player_1_phone + " "*(8 - len(player_1_phone))
                            } | {player_1_email + " "*(20 - len(player_1_email))
                                 } | {player_1_url + " "*(20 - len(player_1_url))} |\t\t\t|
|\t\t+----------------------+----------------------+---------------+----------------------+----------+----------------------+----------------------+\t\t\t|
|\t\t| {player_2_username + " "*(20 - len(player_2_username))
        } | {player_2_name + " "*(20 - len(player_2_name))
             } | {player_2_dob + " "*(13 - len(player_2_dob))
                  } | {player_2_address + " "*(20 - len(player_2_address))
                       } | {player_2_phone + " "*(8 - len(player_2_phone))
                            } | {player_2_email + " "*(20 - len(player_2_email))
                                 } | {player_2_url + " "*(20 - len(player_2_url))} |\t\t\t|
|\t\t+----------------------+----------------------+---------------+----------------------+----------+----------------------+----------------------+\t\t\t|"""

            

            if(all_team_info_in == False):
                commands = f"""|\t\t\t\t\t\t| {" "*(math.floor((76 -len(enter_what)) / 2)) + enter_what + " "*(math.ceil((76 -len(enter_what)) / 2))} |\t\t\t\t\t\t|
|\t\t\t\t\t\t+=========================+==============================+=====================+\t\t\t\t\t\t|"""
                pad_text = """\n|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|
|\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t|"""

            else:
                commands = f"""|\t\t\t\t\t\t| {" "*(math.floor((76 -len(enter_what)) / 2)) + enter_what + " "*(math.ceil((76 -len(enter_what)) / 2))} |\t\t\t\t\t\t|
|\t\t\t\t\t\t+==============================================================================+\t\t\t\t\t\t|
|\t\t\t\t\t\t|                             s. Save teams info                               |\t\t\t\t\t\t|
|\t\t\t\t\t\t+-------------------------+------------------------------+---------------------+\t\t\t\t\t\t|"""
                pad_text = ""

            footer_text = f"""|\t\t\t\t\t\t+------------------------------------------------------------------------------+\t\t\t\t\t\t|
{commands}
|\t\t\t\t\t\t| b. Go back to last page | r. Restart entering the team | q. Quit the program |\t\t\t\t\t\t|
|\t\t\t\t\t\t+-------------------------+------------------------------+---------------------+\t\t\t\t\t\t|{pad_text}
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+"""

            clear_screen()

            print(header_text)
            print(team_info)
            print(players_info)
            print(center_text)
            print(footer_text)

            choice = str(input(">>>> "))
            if(choice.lower() == "q"):
                return "QUIT"
            elif(choice.lower() == "b"):
                return "BACK"
            elif(choice.lower() == "r"):
                return
            elif(name_of_team == ""): 
                if(len(choice) < 21 and data.teams.get_team(choice) == None):
                    name_of_team = choice
                    enter_what = "Enter the username of the captain of this team"
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20 and is unique."

            elif(name_of_team != "" and capt_username == ""):
                if(len(choice) < 21 and data.players.get_by_handle(choice) == None):
                    capt_username = choice
                    enter_what = "Enter the URL of the team"

                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20 and is unique."

            elif(capt_username != "" and team_url == ""):
                if(len(choice) < 21):
                    team_url = choice
                    enter_what = "Enter the tag of the team [????]"
                else:
                    isError = True
                    error_text = "Please make sure the url isn't longer then 20"

            elif(team_url != "" and tag == "****"):
                if(len(choice) == 4):
                    tag = choice
                    enter_what = "Enter the name of the team captain"

                else:
                    isError = True
                    error_text = "Please make sure the tag isn't longer or shorter then 4"                    

            elif(tag != "****" and capt_name == ""):
                if(len(choice) < 21):
                    capt_name = choice
                    enter_what = "Enter the date of birth of the team captain (dd-mm-yyyy)"
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20"

            elif(capt_name != "" and capt_dob == ""):
                if(len(choice) == 10):
                    capt_dob = choice
                    enter_what = "Enter the address of the team captain "
                
                else:
                    isError = True
                    error_text = "Please make sure the date of birth is in this format (dd-mm-yyyy)"

            elif(capt_dob != "" and capt_address == ""):
                if(len(choice) < 21):
                    capt_address = choice
                    enter_what = "Enter the phone number of the team captain "
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20"

            elif(capt_address != "" and capt_phone == ""):
                if(len(choice) == 7):
                    capt_phone = choice
                    enter_what = "Enter the email of the team captain "

                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 7"

            elif(capt_phone != "" and capt_email == ""):
                if(len(choice) < 21):
                    capt_email = choice
                    enter_what = "Enter the url of the team captain "
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20"

            elif(capt_email != "" and capt_url == ""):
                if(len(choice) < 21):
                    capt_url = choice
                    enter_what = "Enter the username of the player"
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20"

                # Player 1 info 

            elif(capt_url != "" and player_1_username == ""):
                if(len(choice) < 21 and data.players.get_by_handle(choice) == None and choice != capt_username):
                    player_1_username = choice
                    enter_what = "Enter the name of the play"
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20 and is unique."

            elif(player_1_username != "" and player_1_name == ""):
                if(len(choice) < 21):
                    player_1_name = choice
                    enter_what = "Enter the date of birth of the player (dd-mm-yyyy)"
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20"

            elif(player_1_name != "" and player_1_dob == ""):
                if(len(choice) == 10):
                    player_1_dob = choice
                    enter_what = "Enter the address of the player"
                
                else:
                    isError = True
                    error_text = "Please make sure the date of birth is in this format (dd-mm-yyyy)"

            elif(player_1_dob != "" and player_1_address == ""):
                if(len(choice) < 21):
                    player_1_address = choice
                    enter_what = "Enter the phone number of the player"
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20"

            elif(player_1_address != "" and player_1_phone == ""):
                if(len(choice) == 7):
                    player_1_phone = choice
                    enter_what = "Enter the email of the player "
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 7"

            elif(player_1_phone != "" and player_1_email == ""):
                if(len(choice) < 21):
                    player_1_email = choice
                    enter_what = "Enter the url of the team captain "
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20"

            elif(player_1_email != "" and player_1_url == ""):
                if(len(choice) < 21):
                    player_1_url = choice
                    enter_what = "Enter the username of the player"
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20"

                # Player 2 info

            elif(player_1_url != "" and player_2_username == ""):
                if(len(choice) < 21 and data.players.get_by_handle(choice) == None and choice != player_1_username and choice != capt_username):
                    player_2_username = choice
                    enter_what = "Enter the name of the play"
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20 and is unique."

            elif(player_2_username != "" and player_2_name == ""):
                if(len(choice) < 21):
                    player_2_name = choice
                    enter_what = "Enter the date of birth of the player (dd-mm-yyyy)"
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20"

            elif(player_2_name != "" and player_2_dob == ""):
                if(len(choice) == 10):
                    player_2_dob = choice
                    enter_what = "Enter the address of the player"
                
                else:
                    isError = True
                    error_text = "Please make sure the date of birth is in this format (dd-mm-yyyy)"

            elif(player_2_dob != "" and player_2_address == ""):
                if(len(choice) < 21):
                    player_2_address = choice
                    enter_what = "Enter the phone number of the player"
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20"

            elif(player_2_address != "" and player_2_phone == ""):
                if(len(choice) == 7):
                    player_2_phone = choice
                    enter_what = "Enter the email of the player "
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 7"

            elif(player_2_phone != "" and player_2_email == ""):
                if(len(choice) < 21):
                    player_2_email = choice
                    enter_what = "Enter the command you want"
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20"

            elif(player_2_email != "" and player_2_url == ""):
                if(len(choice) < 21):
                    player_2_url = choice
                    enter_what = "Enter the username of the player"
                    all_team_info_in = True
                
                else:
                    isError = True
                    error_text = "Please make sure the name isn't longer then 20"
            
            elif(player_2_url != "" and choice.lower() == "s"):
                self.save_new_team_and_players(
                    data,
                    name_of_team,
                    team_url,
                    tag,
                    capt_username,
                    capt_name,
                    capt_dob,
                    capt_address,
                    capt_phone,
                    capt_email,
                    capt_url,
                    player_1_username,
                    player_1_name,
                    player_1_dob,
                    player_1_address,
                    player_1_phone,
                    player_1_email,
                    player_1_url,
                    player_2_username,
                    player_2_name,
                    player_2_dob,
                    player_2_address,
                    player_2_phone,
                    player_2_email,
                    player_2_url,
                )
                return "BACK"

            error_message_text =f"""|\t\t\t\t\t\t+------------------------------------------------------------------------------+\t\t\t\t\t\t|
|\t\t\t\t\t\t|                                                                              |\t\t\t\t\t\t|
|\t\t\t\t\t\t|     \x1b[33m^\x1b[0m                                                                        |\t\t\t\t\t\t|
|\t\t\t\t\t\t|    \x1b[33m/ \ \x1b[0m   {error_text + " "*(66 - len(error_text))} |\t\t\t\t\t\t|
|\t\t\t\t\t\t|   \x1b[33m/\x1b[0m \033[31m\033[1m|\033[0m \x1b[33m\ \x1b[0m                                                                     |\t\t\t\t\t\t|
|\t\t\t\t\t\t|  \x1b[33m/\x1b[0m  \033[31m\033[1m.\033[0m  \x1b[33m\  \x1b[0m           Enter Y. if you want to try again                       |\t\t\t\t\t\t|
|\t\t\t\t\t\t| \x1b[33m/_______\ \x1b[0m              or q. if you want to quit.                           |\t\t\t\t\t\t|
|\t\t\t\t\t\t|                                                                              |\t\t\t\t\t\t|
|\t\t\t\t\t\t+------------------------------------------------------------------------------+\t\t\t\t\t\t|"""

            if(isError == True):
                clear_screen()
                print(header_text)
                print(team_info)
                print(players_info)
                print(error_message_text)
                print(footer_text)
                
                isError = False

                choice = str(input(">>>> "))
                if(choice.lower() == "q"):
                    return "BACK"
                    
        


        