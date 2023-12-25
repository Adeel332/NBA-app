import streamlit as st
from nba_api.stats.endpoints import playercareerstats
from nba_api.live.nba.endpoints import scoreboard

st.title("Scoring Leaders 🏆")

st.subheader('Best Point Guard')
# Create two columns
col1, col2, col3 = st.columns(3)
with col1:
    st.image('curryst01.jpg', caption='Stephen Curry')
# Add player information to the right column
with col2:
    st.subheader("Player Info:")
    st.write("Name: Stephen Curry")
    st.write("Team: Golden State Warriors")
    # Add more player information as needed
with col3:
    st.subheader('Titles')
    st.write('9x All Star,  2x Scoring Champ')
    st.write('4x NBA Champ,  9x All NBA')
    st.write('2x AS MVP,  2021-22 Finals MVP')
# Stephen Curry
career = playercareerstats.PlayerCareerStats(player_id='201939')
# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]
# json
career.get_json()
# dictionary
career.get_dict()



st.subheader("Best Shooting Guard")

# Create two columns
col1, col2, col3 = st.columns(3)
with col1:
    st.image('booker01.jpg', caption='Devin Booker')
# Add player information to the right column
with col2:
    st.subheader("Player Info:")
    st.write("Name: Devin Booker")
    st.write("Team: Phoenix Suns")
    # Add more player information as needed
with col3:
    st.subheader('Titles')
    st.write('3x All Star')
    st.write('2021-22 All NBA')
    st.write('2015-16 All Rookie')
# Devin Booker
career = playercareerstats.PlayerCareerStats(player_id='1626164')
# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]
# json
career.get_json()
# dictionary
career.get_dict()



st.subheader('Best Forward')

# Create two columns
col1, col2, col3 = st.columns(3)
with col1:
    st.image('james01.jpg', caption='Lebron James')
# Add player information to the right column
with col2:
    st.subheader("Player Info:")
    st.write("Name: Lebron James")
    st.write("Team: Los-Angeles Lakers")
    # Add more player information as needed
with col3:
    st.subheader('Titles')
    st.write('19x All Star,  2x Scoring Champ')
    st.write('4x NBA Champ,  19x All NBA')
    st.write('3x AS MVP,  4 Finals MVP')
# Lebron James
career = playercareerstats.PlayerCareerStats(player_id='2544')
# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]
# json
career.get_json()
# dictionary
career.get_dict()



st.subheader("Best Small Forward")

# Create two columns
col1, col2, col3 = st.columns(3)
with col1:
    st.image('tatum01.jpg', caption='Jayson Tatum')
# Add player information to the right column
with col2:
    st.subheader("Player Info:")
    st.write("Name: Jayson Tatum")
    st.write("Team: Boston Celtics")
    # Add more player information as needed
with col3:
    st.subheader('Titles')
    st.write('4x All Star, 3x All NBA')
    st.write('2022-23 AS MVP')
    st.write('2017-18 All Rookie')
# Jayson Tatum
career = playercareerstats.PlayerCareerStats(player_id='1628369')
# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]
# json
career.get_json()
# dictionary
career.get_dict()



st.subheader("Best Center")

# Create two columns
col1, col2, col3 = st.columns(3)
with col1:
    st.image('jokic01.jpg', caption='Nikola Jokic')
# Add player information to the right column
with col2:
    st.subheader("Player Info:")
    st.write("Name: Nikola Jokic")
    st.write("Team: Denver Nuggets")
    # Add more player information as needed
with col3:
    st.subheader('Titles')
    st.write('3x All Star')
    st.write('2021-22 All NBA')
    st.write('2015-16 All Rookie')
# Nikola Jokic
career = playercareerstats.PlayerCareerStats(player_id='203999')
# pandas data frames (optional: pip install pandas)
career.get_data_frames()[0]
# json
career.get_json()
# dictionary
career.get_dict()