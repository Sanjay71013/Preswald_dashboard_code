from preswald import connect, get_df, query, table, text, plotly
import plotly.express as px

connect()  # Initialize connection to preswald.toml data sources
text("# My Data Analysis App")
df = get_df("data/nba.csv")  # Load data
table(df, title="Original Data")

sql = "SELECT * FROM nba WHERE PPG > 25"
filtered_df = query(sql, 'data/nba.csv')
table(filtered_df, title="Filtered Data")

fig = px.scatter(df, x="3PA", y="2PA", color="POS")
plotly(fig)