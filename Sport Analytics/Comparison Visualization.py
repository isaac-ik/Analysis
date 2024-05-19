import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
# ---------------------------------------- FUNCTIONS ---------------------------------------------------#

def plot_team_performance(team1, team2=None):
    team1_data = df[df['team_name'] == team1]
    wins1 = team1_data['fixtures_wins_total'].sum()
    draws1 = team1_data['fixtures_draws_total'].sum()
    losses1 = team1_data['fixtures_loses_total'].sum()

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
        team2_values = [wins2, draws2, losses2]
        
        # Plot bars for both teams
        bar1 = ax.bar(x - width/2, team1_values, width, label=team1, color='green')
        bar2 = ax.bar(x + width/2, team2_values, width, label=team2, color='lightblue')
        
    else:
        bar1 = ax.bar(x, team1_values, width, label=team1, color='green')

    
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
    
    categories = ['Goals For', 'Goals Against']
    team1_values = [goals_for1, goals_against1]

    # Number of categories
    n = len(categories)
    x = np.arange(n)
    width = 0.3
    fig, ax = plt.subplots()
    
    if team2:
        team2_data = df[df['team_name'] == team2]
        goals_for2 = team2_data['goals_for_total_total'].sum()
        goals_against2 = team2_data['goals_against_total_total'].sum()
        team2_values = [goals_for2, goals_against2]
        # Pplot for both teams
        bar1 = ax.bar(x - width/2, team1_values, width, label=team1, color='green')
        bar2 = ax.bar(x + width/2, team2_values, width, label=team2, color='lightblue')
    else:
        bar1 = ax.bar(x, team1_values, width, label=team1, color='green')
    
    ax.set_xlabel('Goal Type')
    ax.set_ylabel('Count')
    ax.set_title(f'Goals Analysis for {team1}' + (f' vs {team2}' if team2 else ''))
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    ax.legend()
    st.pyplot(fig)

def plot_streak_analysis(team1, team2=None):
    team1_data = df[df['team_name'] == team1]
    winning_streak1 = team1_data['biggest_streak_wins'].max()
    drawing_streak1 = team1_data['biggest_streak_draws'].max()
    losing_streak1 = team1_data['biggest_streak_loses'].max()

    categories = ['Winning Streak', 'Drawing Streak', 'Losing Streak']
    team1_values = [winning_streak1, drawing_streak1, losing_streak1]
    
    # Number of categories
    n = len(categories)
    x = np.arange(n)
    width = 0.3
    fig, ax = plt.subplots()
    
    if team2:
        team2_data = df[df['team_name'] == team2]
        winning_streak2 = team2_data['biggest_streak_wins'].max()
        drawing_streak2 = team2_data['biggest_streak_draws'].max()
        losing_streak2 = team2_data['biggest_streak_loses'].max()

        #plot for both teams
        bar1 = ax.bar(x - width/2, team1_values, width, label=team1, color='green')
        bar2 = ax.bar(x + width/2, team2_values, width, label=team2, color='lightblue')
    else:
        bar1 = ax.bar(x, team1_values, width, label=team1, color='green')
    
    ax.set_xlabel('Streak Type')
    ax.set_ylabel('Count')
    ax.set_title(f'Streak Analysis for {team1}' + (f' vs {team2}' if team2 else ''))
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
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
