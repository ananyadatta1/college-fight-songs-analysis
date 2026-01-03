import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# --- CONFIGURATION ---
st.set_page_config(page_title="College Fight Song DNA", layout="wide")

# --- DATA LOADING ---
@st.cache_data
def load_data():
    # Replace with your local path or GitHub URL
    df = pd.read_csv('data/fight-songs.csv')
    
    # 1. Cleaning Yes/No to 1/0
    trope_cols = ['fight', 'victory', 'win_won', 'rah', 'nonsense', 'colors', 'men', 'opponents', 'spelling']
    for col in trope_cols:
        df[col] = df[col].map({'Yes': 1, 'No': 0})
    
    # 2. Feature Engineering
    df['aggression_score'] = df[['fight', 'victory', 'win_won', 'opponents']].sum(axis=1)
    df['spirit_score'] = df[['rah', 'nonsense', 'colors', 'spelling']].sum(axis=1)
    df['is_big_ten'] = df['conference'] == 'Big Ten'
    
    # 3. Year Cleaning
    df['year_clean'] = pd.to_numeric(df['year'], errors='coerce')
    df['year_clean'] = df['year_clean'].fillna(df['year_clean'].median())
    
    return df, trope_cols

df, trope_cols = load_data()

# --- SIDEBAR ---
st.sidebar.title("🎵 Settings")
st.sidebar.markdown("Explore the data behind the exuberant nonsense of college fight songs.")
show_raw_data = st.sidebar.checkbox("Show Raw Data")

# --- MAIN HEADER ---
st.title("🎶 College Fight Song DNA Explorer")
st.markdown("""
    **Is college spirit a formula?** I analyzed 65 fight songs to find out if conferences like the 
    **Big Ten** and **SEC** have unique lyrical identities or if they all follow a 'Standardized Blueprint.'
""")

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📊 Conference Analysis", "🏆 Big Ten Spotlight", "🏫 School DNA"])

# TAB 1: CONFERENCE ANALYSIS
with tab1:
    st.header("The Lyrical Monolith vs. Regional Variance")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Box Plot for Aggression
        fig_box = px.box(df, x="conference", y="aggression_score", color="conference",
                        points="all", title="Aggression Score Distribution",
                        color_discrete_sequence=px.colors.qualitative.Safe)
        st.plotly_chart(fig_box, use_container_width=True)
        
    with col2:
        st.subheader("The Findings")
        st.write("""
            **The 'Standardized' Blueprint:** Despite regional stereotypes, the Big Ten and SEC show massive overlap in aggression.
            
            **The CV Insight:**
            The SEC (CV: 0.57) and Big Ten (CV: 0.66) are the most 'disciplined'—their schools follow a conference 
            blueprint much more closely than the ACC (CV: 0.94).
        """)

# TAB 2: BIG TEN SPOTLIGHT
with tab2:
    st.header("Focus: The Big Ten Conference")
    
    # Comparative Bar Chart
    b10_avg = df[df['is_big_ten'] == True][trope_cols].mean()
    national_avg = df[df['is_big_ten'] == False][trope_cols].mean()
    
    comp_df = pd.DataFrame({
        'Trope': trope_cols,
        'Big Ten': b10_avg.values,
        'National Avg': national_avg.values
    }).melt(id_vars='Trope', var_name='Group', value_name='Frequency')
    
    fig_bar = px.bar(comp_df, x='Trope', y='Frequency', color='Group', barmode='group',
                    title="Does the Big Ten stand out?",
                    color_discrete_map={'Big Ten': '#E00122', 'National Avg': '#777777'})
    st.plotly_chart(fig_bar, use_container_width=True)
    
    st.info("💡 **Insight:** The Big Ten consistently leads in 'Tradition' tropes like **Spelling** and **Colors** compared to the national average.")

# TAB 3: SCHOOL DNA
with tab3:
    st.header("Individual School Profile")
    school_list = sorted(df['school'].unique())
    selected_school = st.selectbox("Select a School", school_list, index=school_list.index("Ohio State"))
    
    school_data = df[df['school'] == selected_school].iloc[0]
    
    # Radar Chart
    categories = ['Aggression', 'Spirit', 'Tempo (Scaled)', 'Duration (Scaled)']
    # Scaling BPM and Duration for the chart (0-4 scale)
    values = [
        school_data['aggression_score'],
        school_data['spirit_score'],
        (school_data['bpm'] / 200) * 4,
        (school_data['sec_duration'] / 180) * 4
    ]
    
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=values,
        theta=categories,
        fill='toself',
        line_color='#E00122'
    ))
    fig_radar.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[0, 4])),
        showlegend=False,
        title=f"DNA of {selected_school}'s Fight Song"
    )
    st.plotly_chart(fig_radar)

    st.subheader(f"Listen to {selected_school}")
spotify_id = school_data['spotify_id']

if pd.notna(spotify_id):
    # Construct the Spotify Embed URL
    embed_url = f"https://open.spotify.com/embed/track/{spotify_id}"
    st.components.v1.iframe(embed_url, height=80)
else:
    st.write("Spotify track not available for this school.")

# RAW DATA SECTION
if show_raw_data:
    st.divider()
    st.subheader("Raw Dataset")
    st.dataframe(df)


st.divider()
footer_col1, footer_col2 = st.columns(2)

with footer_col1:
    st.caption("📊 **Data Credits:** [College Fight Song Dataset](https://github.com/fivethirtyeight/data/blob/master/fight-songs/fight-songs.csv)")
    
with footer_col2:
    st.caption("💻 **Developed by:** [Ananya Datta] | [GitHub](https://github.com/ananyadatta1)")