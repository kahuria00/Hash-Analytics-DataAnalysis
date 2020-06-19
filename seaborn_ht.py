
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


life_expectancy_df=pd.read_csv("C:/Users/Admin/Documents/HashAnalyticsProjects/gapminder-FiveYearData.csv")

life_expectancy_df_pivot=pd.pivot_table(life_expectancy_df, 'lifeExp','continent', 'year')
life_expectancy_plot=sb.heatmap(life_expectancy_df_pivot)
plt.title('Life expectancy across continents(1952-2007)')
figure =life_expectancy_plot.get_figure() 
figure.savefig('seaborn_heatmap.png')