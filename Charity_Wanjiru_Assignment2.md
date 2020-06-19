# HASHANALYTICS DATA ANALYSIS INTERNSHIP-Charity Wanjiru #
##ASSIGNMENT 2##
### HEATMAPS WITH SEABORN###

Installations needed


- pandas
- seaborn
- matplotlib

The first step after installing the needed packages, Create new project and inside the project create new file where all the code goes.
Then import the packages you will need. For example `import pandas as pd`




To get started you need to import all the packages like so

    `import pandas as pd`
    import matplotlib.pyplot as plt
    import seaborn as sb 

Read read your csv file 

    `life_expectancy_df=pd.read_csv("C:/Users/Admin/Documents/HashAnalyticsProjects/gapminder-FiveYearData.csv")`
make your data into pivot table with the specific columns

    life_expectancy_df_pivot=pd.pivot_table(life_expectancy_df, 'lifeExp','continent', 'year')

Using Seaborn plot a heatmap 

    life_expectancy_plot=sb.heatmap(life_expectancy_df_pivot)

using matplotlib I defined the heatmap title

    plt.title('Life expectancy across continents(1952-2007)')
    
saving the png image

    figure =life_expectancy_plot.get_figure() 
    figure.savefig('seaborn_heatmap.png')





