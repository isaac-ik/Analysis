import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import requests
from PIL import Image
from io import BytesIO

# ---------------------------------------- FUNCTIONS ---------------------------------------------------#
# Function to add images to bars
def add_images_to_bars(bars, image_urls, ax):
    for bar, img_url in zip(bars, image_urls):
        try:
            response = requests.get(img_url)
            response.raise_for_status()  # Check if the request was successful
            img = Image.open(BytesIO(response.content))
            # Create OffsetImage
            oi = OffsetImage(img, zoom=0.1)
            # Create AnnotationBbox
            ab = AnnotationBbox(oi, (bar.get_x() + bar.get_width() / 2, bar.get_height()), frameon=False, box_alignment=(0.5, 0))
            # Add to the plot
            ax.add_artist(ab)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching image from {img_url}: {e}")

def plot_team_performance(team1, team2=None):
    team1_data = df[df['team_name'] == team1]
    wins1 = team1_data['fixtures_wins_total'].sum()
    draws1 = team1_data['fixtures_draws_total'].sum()
    losses1 = team1_data['fixtures_loses_total'].sum()
    team1logo = team1_data['team_logo'].iloc[0]

    categories = ['Wins', 'Draws', 'Losses']
    team1_values = [wins1, draws1, losses1]
    
    # Number of categories
    n = len(categories)
    x = np.arange(n)
    width = 0.3
    fig, ax = plt.subplots()
    
    if team2:
        team2_data = df[df['team_name'] == team2]
        wins2 = team2_data['fixtures_wins_total'].sum()
        draws2 = team2_data['fixtures_draws_total'].sum()
        losses2 = team2_data['fixtures_loses_total'].sum()
        team2logo = team2_data['team_logo'].iloc[0]
        team2_values = [wins2, draws2, losses2]
        
        # Plot bars for both teams
        bar1 = ax.bar(x - width/2, team1_values, width, label=team1, color=['green', 'blue', 'red'])
        bar2 = ax.bar(x + width/2, team2_values, width, label=team2, color=['lightgreen', 'lightblue', 'lightcoral'])
        
        # Get both Teams logo image URLs
        image_urls_team1 = [team1logo, team1logo, team1logo]
        add_images_to_bars(bar1, image_urls_team1, ax)
        image_urls_team2 = [team2logo, team2logo, team2logo]
        add_images_to_bars(bar2, image_urls_team2, ax)
    else:
        bar1 = ax.bar(x, team1_values, width, label=team1, color=['green', 'blue', 'red'])
        # Get Team 1 logo image URLs
        image_urls_team1 = [team1logo, team1logo, team1logo]
        add_images_to_bars(bar1, image_urls_team1, ax)
    
    ax.set_xlabel('Result Type')
    ax.set_ylabel('Count')
    ax.set_title(f'Team Performance for {team1}' + (f' vs {team2}' if team2 else ''))
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    st.pyplot(fig)

def plot_goals_analysis(team1, team2=None):
    team1_data = df[df['team_name'] == team1]
    goals_for1 = team1_data['goals_for_total_total'].sum()
    goals_against1 = team1_data['goals_against_total_total'].sum()
    
    fig, ax = plt.subplots()
    ax.bar(['Goals For', 'Goals Against'], [goals_for1, goals_against1], color=['blue', 'red'], alpha=0.7, label=team1)
    
    if team2:
        team2_data = df[df['team_name'] == team2]
        goals_for2 = team2_data['goals_for_total_total'].sum()
        goals_against2 = team2_data['goals_against_total_total'].sum()
        ax.bar(['Goals For', 'Goals Against'], [goals_for2, goals_against2], color=['lightblue', 'lightcoral'], alpha=0.5, label=team2)
    
    ax.set_xlabel('Goal Type')
    ax.set_ylabel('Count')
    ax.set_title(f'Goals Analysis for {team1}' + (f' vs {team2}' if team2 else ''))
    ax.legend()
    st.pyplot(fig)

def plot_streak_analysis(team1, team2=None):
    team1_data = df[df['team_name'] == team1]
    winning_streak1 = team1_data['biggest_streak_wins'].max()
    drawing_streak1 = team1_data['biggest_streak_draws'].max()
    losing_streak1 = team1_data['biggest_streak_loses'].max()
    
    fig, ax = plt.subplots()
    ax.bar(['Winning Streak', 'Drawing Streak', 'Losing Streak'], [winning_streak1, drawing_streak1, losing_streak1], color=['green', 'blue', 'red'], alpha=0.7, label=team1)
    
    if team2:
        team2_data = df[df['team_name'] == team2]
        winning_streak2 = team2_data['biggest_streak_wins'].max()
        drawing_streak2 = team2_data['biggest_streak_draws'].max()
        losing_streak2 = team2_data['biggest_streak_loses'].max()
        ax.bar(['Winning Streak', 'Drawing Streak', 'Losing Streak'], [winning_streak2, drawing_streak2, losing_streak2], color=['lightgreen', 'lightblue', 'lightcoral'], alpha=0.5, label=team2)
    
    ax.set_xlabel('Streak Type')
    ax.set_ylabel('Count')
    ax.set_title(f'Streak Analysis for {team1}' + (f' vs {team2}' if team2 else ''))
    ax.legend()
    st.pyplot(fig)

# ----------------------------- MAIN -----------------------------------------------------------------#
# Loading data
df = pd.read_csv("TeamsStat.csv")

# Sidebar for selecting analysis type
analysis_type = st.sidebar.selectbox("Select Analysis Type", ["Team Performance", "Goal Analysis", "Streak Analysis"])

# Add a checkbox for comparison
compare_teams = st.sidebar.checkbox("Compare Teams")

# Dropdown menu for team selection
teams = df['team_name'].unique()
team1 = st.sidebar.selectbox("Select Team", teams)

team2 = None
if compare_teams:
    team2 = st.sidebar.selectbox("Select Team to Compare", [t for t in teams if t != team1])

# Plot the selected analysis
if analysis_type == "Team Performance":
    st.header(f'Team Performance for {team1}' + (f' vs {team2}' if team2 else ''))
    plot_team_performance(team1, team2)

elif analysis_type == "Goal Analysis":
    st.header(f'Goals Analysis for {team1}' + (f' vs {team2}' if team2 else ''))
    plot_goals_analysis(team1, team2)

elif analysis_type == "Streak Analysis":
    st.header(f'Streak Analysis for {team1}' + (f' vs {team2}' if team2 else ''))
    plot_streak_analysis(team1, team2)
