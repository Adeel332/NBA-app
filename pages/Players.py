import re
import streamlit as st
from nba_api.stats.library.data import players
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.library.data import (
    player_index_id,
    player_index_full_name,
    player_index_first_name,
    player_index_last_name,
    player_index_is_active,
)

def _find_players(regex_pattern, row_id):
    players_found = []
    for player in players:
        if re.search(regex_pattern, str(player[row_id]), flags=re.I):
            players_found.append(_get_player_dict(player))
    return players_found

def _get_player_dict(player_row):
    return {
        "id": player_row[player_index_id],
        "full_name": player_row[player_index_full_name],
        "first_name": player_row[player_index_first_name],
        "last_name": player_row[player_index_last_name],
        "is_active": player_row[player_index_is_active],
    }

def display_players(players_list):
    for player in players_list:
        st.write(f"Player ID: {player['id']}, Full Name: {player['full_name']}, Active: {player['is_active']}")

def find_players_by_full_name(regex_pattern):
    players_list = _find_players(regex_pattern, player_index_full_name)
    display_players(players_list)

def find_players_by_first_name(regex_pattern):
    players_list = _find_players(regex_pattern, player_index_first_name)
    display_players(players_list)

def find_players_by_last_name(regex_pattern):
    players_list = _find_players(regex_pattern, player_index_last_name)
    display_players(players_list)

def find_player_by_id(player_id):
    regex_pattern = "^{}$".format(player_id)
    players_list = _find_players(regex_pattern, player_index_id)
    if len(players_list) > 1:
        st.warning("Found more than 1 id")
    elif not players_list:
        st.info("No player found")
    else:
        display_players(players_list)

def get_players():
    players_list = []
    for player in players:
        players_list.append(_get_player_dict(player))
    display_players(players_list)

def get_active_players():
    players_list = []
    for player in players:
        if player[player_index_is_active]:
            players_list.append(_get_player_dict(player))
    display_players(players_list)

def get_inactive_players():
    players_list = []
    for player in players:
        if not player[player_index_is_active]:
            players_list.append(_get_player_dict(player))
    display_players(players_list)

# Streamlit UI
st.title("NBA Player Search App")

option = st.sidebar.selectbox("Select search type", ["By Full Name", "By First Name", "By Last Name", "By ID", "All Players", "Active Players", "Inactive Players"])

if option == "By Full Name":
    regex_pattern = st.text_input("Enter full name regex pattern:")
    find_players_by_full_name(regex_pattern)
elif option == "By First Name":
    regex_pattern = st.text_input("Enter first name regex pattern:")
    find_players_by_first_name(regex_pattern)
elif option == "By Last Name":
    regex_pattern = st.text_input("Enter last name regex pattern:")
    find_players_by_last_name(regex_pattern)
elif option == "By ID":
    player_id = st.text_input("Enter player ID:")
    if player_id:
        find_player_by_id(player_id)

        career = playercareerstats.PlayerCareerStats(player_id)

        # pandas data frames (optional: pip install pandas)
        career.get_data_frames()[0]

        # json
        career.get_json()

        # dictionary
        career.get_dict()

    else:
        st.warning("Please Enter Valid Player Id")
elif option == "All Players":
    get_players()
elif option == "Active Players":
    get_active_players()
elif option == "Inactive Players":
    get_inactive_players()
