# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 16:25:35 2025

@author: bibek
"""

import streamlit as st
import pandas as pd


st.title("University Rankings for Progressiveness")

st.write(
    'For methodology, click here <a href="https://github.com/bibekbhatta/University_Ranking" target="_blank">https://github.com/bibekbhatta/University_Ranking </a>.',
    unsafe_allow_html=True
)

st.subheader("USA, UK, Aus, NZ, Canada and Ireland")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('Uni_rankings_all.csv')

df = load_data()

sections = ['Russell and Ivy Combined'] + sorted(df['country'].unique().tolist())
section = st.selectbox("Choose Country or Group", sections)

ranking_types = {
    'Climate': 'Climate_Rank',
    'Social Justice': 'Social_Justice_Rank',
    'Gender': 'Gender_Rank',
    'Overall': 'Overall_Rank'
}
ranking_type = st.selectbox("Choose Ranking Type", list(ranking_types.keys()))


score_columns = {
    'Climate': 'climate_score',
    'Social Justice': 'social_score',  # Correct column name
    'Gender': 'gender_score',
    'Overall': 'overall_score'
}

# Filter data based on section
if section == 'Russell and Ivy Combined':
    filtered_df = df[df['Group'].isin(['Ivy', 'Russell'])].copy()
    rank_column = f'Russell_Ivy_Combined_{ranking_types[ranking_type]}'
else:
    filtered_df = df[df['country'] == section].copy()
    rank_column = f'Country_{ranking_types[ranking_type]}'

# Select score column
score_column = score_columns[ranking_type]

# Sort by the selected ranking
filtered_df = filtered_df.sort_values(rank_column)

# Display the table
st.subheader(f"{ranking_type} Rankings for {section}")
display_df = filtered_df[['university', rank_column, score_column]].rename(
    columns={rank_column: 'Rank', score_column: 'Score'}
)
st.dataframe(display_df, use_container_width=True, hide_index=True)

csv = display_df.to_csv(index=False)
st.download_button(
    label="Download Table as CSV",
    data=csv,
    file_name=f"{section}_{ranking_type}_rankings.csv",
    mime="text/csv"
)

st.write("If you use this data, pls give credits to this author and provide this link: https://github.com/bibekbhatta/University_Ranking")


# footer = """
# <style>
# .footer {
#     position: fixed;
#     left: 0;
#     bottom: 0;
#     width: 100%;
#     background-color: #f1f1f1;
#     color: black;
#     text-align: center;
#     padding: 10px;
# }
# </style>
# <div class='footer'>
#     <p>For methodology, click here: <a href="https://github.com/bibekbhatta/University_Ranking" target="_blank">link to github</a>.</p>
# </div>
# """
# st.markdown(footer, unsafe_allow_html=True)
