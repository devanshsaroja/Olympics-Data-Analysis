import numpy as np
import pandas as pd

def fetch_medal_tally(df, year, country):
    medal_df = df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'])
    flag = 0
    if year == 'Overall' and country == 'Overall':
        temp_df = medal_df
    if year == 'Overall' and country != 'Overall':
        flag = 1
        temp_df = medal_df[medal_df['region'] == country]
    if year != 'Overall' and country == 'Overall':
        temp_df = medal_df[medal_df['Year'] == int(year)]
    if year != 'Overall' and country != 'Overall':
        temp_df = medal_df[(medal_df['Year'] == year) & (medal_df['region'] == country)]

    if flag == 1:
        x = temp_df.groupby('Year').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Year').reset_index()
    else:
        x = temp_df.groupby('region').sum()[['Gold', 'Silver', 'Bronze']].sort_values('Gold',
                                                                                      ascending=False).reset_index()

    x['total'] = x['Gold'] + x['Silver'] + x['Bronze']

    x['Gold'] = x['Gold'].astype('int')
    x['Silver'] = x['Silver'].astype('int')
    x['Bronze'] = x['Bronze'].astype('int')
    x['total'] = x['total'].astype('int')

    return x


def country_year_list(df):
    years = df['Year'].unique().tolist()
    years.sort()
    years.insert(0, 'Overall')

    country = np.unique(df['region'].dropna().values).tolist()
    country.sort()
    country.insert(0, 'Overall')

    return years,country

def data_over_time(df, col):
    # Drop duplicates and count occurrences by year
    nations_over_time = (
        df.drop_duplicates(['Year', col])
        .groupby('Year')
        .size()
        .reset_index(name='Count')
    )
    
    # Rename columns
    nations_over_time.rename(columns={'Year': 'Edition', 'Count': col}, inplace=True)
    
    # Sort by 'Edition'
    nations_over_time = nations_over_time.sort_values(by='Edition')
    
    return nations_over_time



def most_successful(df, sport):
    # Drop rows where Medal is NaN
    temp_df = df.dropna(subset=['Medal'])

    # Filter by sport if specified
    if sport != 'Overall':
        temp_df = temp_df[temp_df['Sport'] == sport]

    # Count medals per athlete
    medal_counts = temp_df['Name'].value_counts().reset_index()
    medal_counts.columns = ['Name', 'Medals']  # Rename columns for clarity

    # Merge with original DataFrame to get additional information
    x = (
        medal_counts
        .head(15)
        .merge(df, on='Name', how='left')[['Name', 'Medals', 'Sport', 'region']]
        .drop_duplicates(subset='Name')  # Ensure unique entries per athlete
    )
    
    return x


def yearwise_medal_tally(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)

    new_df = temp_df[temp_df['region'] == country]
    final_df = new_df.groupby('Year').count()['Medal'].reset_index()

    return final_df

def country_event_heatmap(df,country):
    temp_df = df.dropna(subset=['Medal'])
    temp_df.drop_duplicates(subset=['Team', 'NOC', 'Games', 'Year', 'City', 'Sport', 'Event', 'Medal'], inplace=True)

    new_df = temp_df[temp_df['region'] == country]

    pt = new_df.pivot_table(index='Sport', columns='Year', values='Medal', aggfunc='count').fillna(0)
    return pt


def most_successful_countrywise(df, country):
    # Drop rows without medals
    temp_df = df.dropna(subset=['Medal'])

    # Filter for the specified country
    temp_df = temp_df[temp_df['region'] == country]

    # Count medals by athlete name and reset index
    top_athletes = temp_df['Name'].value_counts().reset_index()
    top_athletes.columns = ['Name', 'Medals']  # Rename columns explicitly

    # Merge with the original DataFrame to fetch additional details
    top_athletes = top_athletes.head(10).merge(df, left_on='Name', right_on='Name', how='left')[
        ['Name', 'Medals', 'Sport', 'region']
    ].drop_duplicates('Name')

    return top_athletes


def weight_v_height(df, sport):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])
    athlete_df['Medal'].fillna('No Medal', inplace=True)

    if sport != 'Overall':
        temp_df = athlete_df[athlete_df['Sport'] == sport]
    else:
        temp_df = athlete_df

    # Drop rows with missing Weight or Height
    temp_df = temp_df.dropna(subset=['Weight', 'Height'])

    return temp_df


def men_vs_women(df):
    athlete_df = df.drop_duplicates(subset=['Name', 'region'])

    men = athlete_df[athlete_df['Sex'] == 'M'].groupby('Year').count()['Name'].reset_index()
    women = athlete_df[athlete_df['Sex'] == 'F'].groupby('Year').count()['Name'].reset_index()

    final = men.merge(women, on='Year', how='left')
    final.rename(columns={'Name_x': 'Male', 'Name_y': 'Female'}, inplace=True)

    final.fillna(0, inplace=True)

    return final