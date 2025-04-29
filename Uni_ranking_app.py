# -*- coding: utf-8 -*-
"""
Created on Mon Apr 28 16:25:35 2025

@author: bibek
"""

import streamlit as st
import pandas as pd
# import os

df = pd.read_csv('Uni_rankings_all.csv')  # Or df = your_dataframe

# Streamlit app
st.title("University Rankings Dashboard")
st.subheader("USA, UK, Aus, NZ, Canada and Ireland")

# Dropdown for view option
view_option = st.selectbox(
    "Select Russell/Ivy League or All",
    ["All", "Russell Group & Ivy League"],
    key="view_option"
)

# Define the mapping of sort options to column names
rank_mapping = {
    "Climate Rank": ("Climate_Rank", "Russell_Ivy_Climate_Rank"),
    "Social Justice Rank": ("Social_Justice_Rank", "Russell_Ivy_Social_Justice_Rank"),
    "Gender Rank": ("Gender_Rank", "Russell_Ivy_Gender_Rank"),
    "Overall Rank": ("Overall_Rank", "Russell_Ivy_Overall_Rank")
}

# Dropdown for sorting option
st.write("Sort ranking by Climate, Social Justice, Gender or OVERALL")
sort_by = st.selectbox(
    "",
    list(rank_mapping.keys()),
    key="sort_by"
)

# Display name for the selected sort option
sort_by_display = sort_by.replace(" Rank", "")

# Filter for Russell Ivy group if selected
if view_option == "Russell Group & Ivy League":
    df_filtered = df[df["Group"].isin(["Ivy", "Russell"])]
else:
    df_filtered = df

# Prepare the display DataFrame based on the sort option
if sort_by == "Overall Rank":
    rank_columns = ["university", rank_mapping[sort_by][1] if view_option == "Russell Group & Ivy League" else rank_mapping[sort_by][0]]
    df_display = df_filtered[rank_columns]
    df_display.columns = ["University", "Overall"]
else:
    rank_column = rank_mapping[sort_by][1] if view_option == "Russell Group & Ivy League" else rank_mapping[sort_by][0]
    df_display = df_filtered[["university", rank_column]]
    df_display.columns = ["University", sort_by_display]

# Sort by the selected rank
df_display = df_display.sort_values(by=sort_by_display)

# Truncate long University names to reduce column width
df_display['University'] = df_display['University'].apply(lambda x: x[:50] + '...' if len(x) > 50 else x)

# Apply Styler to format the table
styled_df = df_display.style.set_properties(**{
    'text-align': 'left',
    'width': '150px'
}).set_table_styles([
    {'selector': 'th', 'props': [('width', '150px')]}  # Column width for headers
])

# Inject custom CSS for styling
st.markdown(
    """
    <style>
    /* Background gradient for the app */
    body {
        background: linear-gradient(45deg, #f8a5c2, #c2e9fb, #a1c4fd, #fdcbf1);
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
    }
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    .stDataFrame table th:nth-child(1),
    .stDataFrame table td:nth-child(1) {
        width: 80px !important;
        white-space: nowrap;
        text-overflow: ellipsis;
        overflow: hidden;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the styled table without the index column
st.dataframe(df_display, hide_index=True)

# Add a download button
st.download_button(
    label="Download Data as CSV",
    data=df_display.to_csv(index=False),
    file_name="university_rankings.csv",
    mime="text/csv"
)