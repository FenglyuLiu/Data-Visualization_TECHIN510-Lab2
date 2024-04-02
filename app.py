import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Penguins Explorer",
    page_icon="🐧",
    layout="centered",  # centered, wide
    initial_sidebar_state="auto",
    menu_items=None
)

# Sidebar content
st.sidebar.title("🐧 Penguins Explorer")
st.sidebar.markdown("""
    This app allows you to explore the Palmer Penguins dataset. You can filter the data based on species, island, and bill length, and visualize the distribution of penguin features.
""")

st.write("")
st.write("")

# Load data
df = pd.read_csv('https://raw.githubusercontent.com/mcnakhaee/palmerpenguins/master/palmerpenguins/data/penguins.csv')


# Sidebar filters
st.sidebar.markdown("### Filters")
species = st.sidebar.multiselect('Species', df['species'].unique(), default=df['species'].unique())
island = st.sidebar.multiselect('Island', df['island'].unique(), default=df['island'].unique())
bill_length_range = st.sidebar.slider('Bill Length (mm)', float(df['bill_length_mm'].min()), float(df['bill_length_mm'].max()), (float(df['bill_length_mm'].min()), float(df['bill_length_mm'].max())))

# Filter data
filtered_df = df[(df['species'].isin(species)) & (df['island'].isin(island)) & (df['bill_length_mm'] >= bill_length_range[0]) & (df['bill_length_mm'] <= bill_length_range[1])]

# Show filtered data
with st.expander("### Raw Data"):
    st.write(filtered_df)

st.write("")
st.write("")

# Visualizations
st.markdown("### 🍕 Data Visualizations")
st.markdown("#### 1. Bill Length Distribution by Species")
st.write("")
st.write("")
fig, ax = plt.subplots(figsize=(10, 6))  # Adjust figure size (width, height) as needed
sns.histplot(data=filtered_df, x='bill_length_mm', hue='species', kde=True, ax=ax, edgecolor='white')


# Set axes to light gray and remove top and right borders
border_color = '#000000'  # Light gray color
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_color(border_color)
ax.spines['left'].set_color(border_color)
ax.tick_params(axis='x', colors=border_color)  # Change the color of the x-axis ticks
ax.tick_params(axis='y', colors=border_color)  # Change the color of the y-axis ticks
st.pyplot(fig)



st.write("")
st.write("")
st.write("")



st.markdown("#### 2. Pairplot of Penguin Features")
st.write("")
st.write("")
pairplot_fig = sns.pairplot(filtered_df, hue='species')

# Increase the size of the legend
plt.legend(prop={'size': 12})

st.pyplot(pairplot_fig)

st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")




st.markdown("### 🐧 Findings")

# Display the insights using markdown
st.markdown("""
#### Penguin Species Analysis Insights

##### 1. Bill Length and Depth
 Adelie penguins tend to have shorter and deeper bills compared to the other species. Gentoos have longer and shallower bills, while Chinstraps have bills that are intermediate in length but also quite deep, similar to Adelies.

##### 2. Flipper Length
 Gentoo penguins seem to have the longest flippers, followed by Chinstraps and then Adelies. There’s a noticeable separation between the species based on flipper length, which could be a significant distinguishing characteristic.
            
##### 3. Body Mass
  Gentoo penguins are generally heavier than the other species. Adelie penguins have a wide range of body masses, but most of them are lighter than Gentoos. Chinstrap penguins appear to have the least variation in body mass and are on the lighter side compared to Gentoos.
            
##### 4. Kernel Density Estimates
  Kernel Density Estimates: The diagonal plots show the distribution of each variable for each species. Adelie penguins' bill length and depth are normally distributed, whereas Gentoos' flipper length and body mass show a skewed distribution towards the higher values.
            
##### 5. Correlations
  There appear to be positive correlations between flipper length and body mass, as well as bill length and flipper length. The correlations are species-specific and can be quite strong, as indicated by the clustering of the data points. put these findings into structured markdown format
            
""")

