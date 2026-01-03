# 🎶 College Fight Song DNA: A Comparative Analysis
**Theme:** The Exuberant Nonsense of College Sports  
**Goal:** To analyze whether Power Five conferences have distinct "Lyrical Blueprints" using the FiveThirtyEight Fight Song dataset.

## 🚀 The Core Question
Do conferences like the **Big Ten** and **SEC** actually have different "vibes," or is college spirit a monolithic formula? I used Python and Streamlit to engineer new metrics and test these cultural assumptions.

## 🛠️ Tech Stack
- **Language:** Python 3.11
- **Analysis:** Pandas, NumPy, SciPy (T-Tests)
- **Visualization:** Plotly (Interactive Charts)
- **Deployment:** Streamlit

## 🧪 Feature Engineering
To move beyond basic data, I engineered three primary metrics:
- **Aggression Score:** Weighted sum of `fight`, `victory`, `win_won`, and `opponents`.
- **Spirit Score:** Weighted sum of `rah`, `nonsense`, `colors`, and `spelling`.
- **CV (Coefficient of Variation):** Used to measure the "Homogeneity" or consistency of a conference's lyrical brand.

## 📊 Key Findings

### 1. The "Standardized Spirit" (The CV Discovery)
While most fans assume conferences have unique identities, the data shows that the **SEC** and **Big Ten** are the most "disciplined" conferences.
- **SEC (CV: 0.57):** The most standardized blueprint. High aggression with very little deviation between schools.
- **ACC (CV: 0.94):** The "Wild West." Nearly double the variance of the SEC, suggesting no unified conference identity.



### 2. The Lyrical Monolith
Initial T-tests revealed **no statistically significant difference** ($p > 0.05$) between the average aggression of the Big Ten and the SEC. This debunks the myth that regional culture significantly alters fight song lyrics; rather, major programs follow a successful "Power Five Template."

### 3. Big Ten vs. National Average
The Big Ten leads the nation in **"Tradition Tropes"** (Spelling and Colors), confirming that while their aggression levels are average, their commitment to ritualistic elements remains a distinctive feature.

## 🖥️ How to Run the App
1. Clone the repo: `git clone https://github.com/your-username/college-fight-songs.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the app: `streamlit run app.py`

## 👤 Author
- **Ananya Datta** - Aspiring Data Scientist
- **Data Source:** [FiveThirtyEight GitHub](https://github.com/fivethirtyeight/data/tree/master/fight-songs)