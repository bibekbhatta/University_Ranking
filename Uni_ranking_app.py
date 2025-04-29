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

# Add subtitle
st.subheader("USA, UK, Aus, NZ, Canada and Ireland")

# Move the "Select Ranking View" dropdown below the subtitle in the main area
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

# Sorting option
st.write("Sort ranking by Climate, Social Justice, Gender or OVERALL")
sort_by = st.selectbox(
    "",
    list(rank_mapping.keys()),
    key="sort_by"
)

# Remove "Rank" from the display name for the selected sort option
sort_by_display = sort_by.replace(" Rank", "")

# Filter for Russell Ivy group if selected
if view_option == "Russell Group & Ivy League":
    df_filtered = df[df["Group"].isin(["Ivy", "Russell"])]
else:
    df_filtered = df

# Prepare the display DataFrame based on the sort option
if sort_by == "Overall Rank":
    if view_option == "Russell Group & Ivy League":
        rank_columns = [
            "university",  # Exclude "Group" column
            "Russell_Ivy_Climate_Rank", "Russell_Ivy_Social_Justice_Rank", 
            "Russell_Ivy_Gender_Rank", "Russell_Ivy_Overall_Rank"
        ]
        df_display = df_filtered[rank_columns]
        df_display.columns = ["University", "Climate", "Social Justice", "Gender", "Overall"]
    else:
        rank_columns = [
            "university",  # Exclude "Group" column
            "Climate_Rank", "Social_Justice_Rank", 
            "Gender_Rank", "Overall_Rank"
        ]
        df_display = df_filtered[rank_columns]
        df_display.columns = ["University", "Climate", "Social Justice", "Gender", "Overall"]
else:
    if view_option == "Russell Group & Ivy League":
        rank_column = rank_mapping[sort_by][1]  # Use Russell Ivy rank column
    else:
        rank_column = rank_mapping[sort_by][0]  # Use overall rank column
    df_display = df_filtered[["university", "Group", rank_column]]
    df_display.columns = ["University", "Group", sort_by_display]

# Sort by the selected rank
df_display = df_display.sort_values(by=sort_by_display)

# Inject custom CSS to style the University column, reduce gap, make subtitle colorful, set background gradient, and add mobile responsiveness
st.markdown(
    """
    <style>
    /* Set the background gradient for the entire app */
    body {
        background: linear-gradient(45deg, #f8a5c2, #c2e9fb, #a1c4fd, #fdcbf1); /* Pink, light blue, blue, light pink */
        background-size: 400% 400%;
        animation: gradient 15s ease infinite;
        min-height: 100vh;
    }

    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Default styling for the University column (first column) - reduced width by 30% */
    .stDataFrame table th:nth-child(1),
    .stDataFrame table td:nth-child(1) {
        width: 84px !important;  /* 120px reduced by 30% = 84px */
        white-space: nowrap;      /* Prevent text wrapping */
        overflow-x: auto;         /* Enable horizontal scrolling */
        text-overflow: ellipsis;  /* Show ellipsis for overflowed text */
    }

    /* Styling for other columns (Group, Climate, Social Justice, Gender, Overall) */
    .stDataFrame table th:not(:nth-child(1)),
    .stDataFrame table td:not(:nth-child(1)) {
        width: 90px !important;   /* Fixed width for other columns */
        text-align: center;       /* Center-align text for better readability */
    }

    /* Override University column width when there are 5 columns (Overall Rank case, Group hidden) */
    .stDataFrame table[aria-colcount="5"] th:nth-child(1),
    .stDataFrame table[aria-colcount="5"] td:nth-child(1) {
        width: 56px !important;   /* 80px reduced by 30% = 56px */
    }

    /* Ensure the table itself can scroll vertically if needed */
    .stDataFrame {
        overflow-y: auto;         /* Enable vertical scrolling for the table */
        max-height: 400px;        /* Optional: Limit the table height */
    }

    /* Reduce the gap between the st.write heading and the st.selectbox dropdown */
    div.stMarkdown:has(p:contains("Sort ranking by Climate")) {
        margin-bottom: -10px !important;  /* Further reduce bottom margin */
        padding-bottom: 0px !important;   /* Remove bottom padding */
    }

    div.stSelectbox:has(select option[value="Social Justice Rank"]) {
        margin-top: -20px !important;     /* Further pull the dropdown closer */
        padding-top: 0px !important;      /* Remove top padding */
    }

    /* Make the subtitle colorful with a gradient */
    div.stMarkdown h2 {
        background: linear-gradient(90deg, #ff0000, #ff8c00, #ffff00, #00ff00, #0000ff, #4b0082, #8b00ff); /* Rainbow gradient */
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        color: transparent; /* Fallback for browsers that don't support background-clip */
    }
    
    /* Add more color to the app components */
    .stApp {
        background: rgba(255, 255, 255, 0.7); /* Semi-transparent white background */
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
    }
    
    .stSelectbox, .stButton {
        background: rgba(255, 255, 272, 0.8);
        border-radius: 5px;
    }
    
    /* Make the main title more vibrant */
    .stMarkdown h1 {
        color: #6200ee;
        text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.1);
    }

    /* Mobile responsiveness */
    @media (max-width: 600px) {
        /* Reduce padding and margins for the app container */
        .stApp {
            padding: 10px !important;
            margin: 0 !important;
        }

        /* Reduce font sizes for title and subtitle */
        .stMarkdown h1 {
            font-size: 24px !important;  /* Smaller title font */
        }

        .stMarkdown h2 {
            font-size: 16px !important;  /* Smaller subtitle font */
        }

        /* Reduce font size for dropdown labels and text */
        .stMarkdown p {
            font-size: 14px !important;
        }

        .stSelectbox label, .stSelectbox div {
            font-size: 14px !important;
        }

        /* Make the table more compact */
        .stDataFrame {
            width: 100% !important;      /* Ensure table takes full width */
            overflow-x: auto;            /* Enable horizontal scrolling if needed */
        }

        /* Reduce column widths for mobile */
        .stDataFrame table th:nth-child(1),
        .stDataFrame table td:nth-child(1) {
            width: 60px !important;      /* Smaller University column width */
            font-size: 12px !important;  /* Smaller font for better fit */
        }

        .stDataFrame table th:not(:nth-child(1)),
        .stDataFrame table td:not(:nth-child(1)) {
            width: 60px !important;      /* Smaller width for other columns */
            font-size: 12px !important;  /* Smaller font for better fit */
        }

        /* Further reduce University column width when there are 5 columns (Overall Rank case) */
        .stDataFrame table[aria-colcount="5"] th:nth-child(1),
        .stDataFrame table[aria-colcount="5"] td:nth-child(1) {
            width: 40px !important;      /* Even smaller for Overall Rank case */
        }

        /* Hide Group column on mobile for non-Overall Rank cases to save space */
        .stDataFrame table[aria-colcount="3"] th:nth-child(2),
        .stDataFrame table[aria-colcount="3"] td:nth-child(2) {
            display: none !important;    /* Hide Group column on mobile */
        }

        /* Adjust widths for remaining columns after hiding Group */
        .stDataFrame table[aria-colcount="3"] th:nth-child(1),
        .stDataFrame table[aria-colcount="3"] td:nth-child(1) {
            width: 80px !important;      /* Slightly wider University column */
        }

        .stDataFrame table[aria-colcount="3"] th:nth-child(3),
        .stDataFrame table[aria-colcount="3"] td:nth-child(3) {
            width: 60px !important;      /* Rank column width */
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Display the table without the index column
st.dataframe(df_display, hide_index=True)

# Optional: Add a download button for the filtered data
st.download_button(
    label="Download Data as CSV",
    data=df_display.to_csv(index=False),
    file_name="university_rankings.csv",
    mime="text/csv"
)