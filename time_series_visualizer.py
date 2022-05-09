import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)

dataset = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', header='infer', parse_dates=True, infer_datetime_format=True) 

df = pd.DataFrame(dataset)

# Clean the data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    df1 = df.copy()
    sns.set_style('dark')
    fig, ax = plt.subplots(figsize=(9, 5))
    sns.lineplot(x='date', y='value', data=df1).set(title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df2 = df.copy()
    df2 = df2.groupby(pd.Grouper(freq="M")).sum()
    df2 = df2.reset_index()

  
    df2['Year'] = pd.to_datetime(df2['date']).dt.year
    df2['Month'] = pd.to_datetime(df2['date']).dt.month_name()
    
    # Draw bar plot
    sns.set_style('dark')
    fig, ax = plt.subplots(figsize=(9, 9))
    sns.barplot(x='Year', y='value', hue='Month', data=df2)
    
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months', loc='upper left', labels= ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
  
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():

    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box = df_box.reset_index()
    df_box['month'] = [d.strftime('%b') for d in df_box['date']]
    df_box['Year'] = pd.to_datetime(df_box['date']).dt.year    

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    df_box1= pd.DataFrame(df_box['Year']).dropna()
    df_box1['value'] = df_box['value']
  
    df_box2 = pd.DataFrame(df_box['month']).dropna()
    df_box2['value'] = df_box['value']
    

    fig, ax = plt.subplots(1, 2, figsize=(25, 25))

    # Draw box plots (using Seaborn)

    sns.boxplot(ax=ax[0], x=df_box1['Year'], y=df_box1['value'])

    ax[0].set_title('Year-wise Box Plot (Trend)')
    ax[0].set(ylabel='Page Views')
    ax[0].set(xlabel='Year')
  
    sns.boxplot(ax=ax[1], x=df_box2['month'],  y=df_box2['value'], order= month_order)  
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    ax[1].set(ylabel='Page Views')
    ax[1].set(xlabel='Month')
    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
