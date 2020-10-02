import time
import pandas as pd
import numpy as np

# Create dictionaries of datasets related to bike share systems for U.S. three major cities:
CITY_DATA = { 'Chicago': 'chicago.csv',
              'NYC': 'new_york_city.csv',
              'Washington': 'washington.csv' }

# Defining 'get_month' function, Using Docstrings for documentation:
def get_month():
    """ Using input() function, while loop to iterate until break, and .lower() method, to filter by month """
    months_of_year = ['january','february','march','april','may','june','july','august','september','october','november','december']
    while True:
        month = input('\nWhich month? Select january,february,march,april,may,june,july,august,september,october,november,december\n')
        month = month.lower()
        if (month in months_of_year):
            break
    return month

# Defining 'get_day' function, using Docstrings for documentation:
def get_day():
    """ Using input() function, while loop to iterate untile break, and .lower() method, to filter by weekday """
    day_of_week = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    while True:
        day = input('\nWhich day? Select monday,tuesday,wednesday,thursday,friday,saturday,sunday\n')
        day = day.lower()
        if(day in day_of_week):
            break
    return day

# Defining 'get filters' function
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze datasets:
    INPUTS
    - city (Chicago, New York City, Washington)
    - month (month of the year) name of the month to filter by, or "all" to apply no month filter
    - day (day of the week) name of the day of week to filter by, or "all" to apply no day filter

    OUTPUTS
    Analyzing the related datasets
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    US_cities = ['Chicago','NYC','Washington']
    while True:
        city = input('\nPlease select one of the following cities:(Chicago, NYC, Washington)\n')
        if (city in US_cities):
            break

    while True:
        filters = [1,2,3,4]
        filter = input('\nWhat would you like to filter by\n 1:month\n 2:day\n 3:both\n 4:not at all\n Type 1,2,3, or 4\n')
        filter = int(filter)
        if (filter in filters):
            break
    if (filter == 1):
        month = get_month()
        day = 'all'
    elif (filter == 2):
        day = get_day()
        month = 'all'
    elif (filter == 3):
        month = get_month()
        day = get_day()
    elif (filter == 4):
        month = 'all'
        day = 'all'

    print('-'*40)
    return city, month, day

# Defining 'load_data' function
def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Arguments:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # Load dataset file into Pandas DataFrame:
    df = pd.read_csv(CITY_DATA[city])
    # Convert the 'Start Time' column to datetime using to_datetime() method
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # Extract month from 'Start Time' column to create a new column by using .dt.month attribute pandas
    # Extract day of week from 'Start Time' column to create a new column by using .dt.weekday attribute pandas
    df['Start Time'] = df['Start Time'].dt.month
    df['Start Time'] = df['Start Time'].dt.weekday_name
    # Filter by month if applicable, use the index of the month list to get the corresponding int month:
    if month != 'all':
        months_of_year = ['january','february','march','april','may','june','july','august','september','october','november','december']
        month = months_of_year.index(month) + 1
        df = df[df['month'] == month]
    # Filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df
# Statistics Computed
# Popular times of Travel

def time_statistics(df):
    """ Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Find the most common month,day of week, and hour of week using dataframe.mode() function to get the value that appears most often among a set of values:
    # Display the most common month
def common_month(df):
    df['month'] = df['Start Time'].dt.month_name()
    popular_month = df['month'].mode()[0]
    print('The most common month: ',popular_month)

    # Display the most common day of week
def common_day(df):
    df['day_of_week'] = df['Start Time'].dt.day_name()
    popular_day = df['day_of_week'].mode()[0]
    print('The most common day: ',popular_day)

    # Display the most common start hour of a day
def common_hour(df):
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour:',popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Definition of most frequent times of travel function
def time_statistics(df, month, day):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    if(month=='all' and day=='all'):
        # display the most common month
        common_month(df)
        # display the most common day of week
        common_day(df)
        # display the most common start hour
        common_hour(df)
    elif(month!='all' and day=='all'):
        # display the most common day of week
        common_day(df)
        # display the most common start hour
        common_hour(df)
    elif(month=='all' and day!='all'):
        # display the most common start hour
        common_hour(df)
        # display the most common month
        common_month(df)
    elif(month!='all'and day!='all'):
        common_hour(df)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



# Popular stations and trip
def station_statistics(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

def station_statistics(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start_station=df['Start Station'].mode()[0]
    print('Most Popular Start Station:',popular_start_station)

    # display most commonly used end station
    popular_end_station=df['End Station'].mode()[0]
    print('Most Popular End Station:',popular_end_station)

    # display most frequent combination of start station and end station trip
    # Use pandas Dataframe.to_string() function to render the given DataFrame to a console-friendly tabular output.
    # Use cat() function to concatenating two columns of string ('Start_Station' and 'End_Station') into new column 'Journey' in Pandas DataFrame:
    df['Journey'] = df['Start Station'].str.cat(df['End Station'],sep=' to ')
    popular_start_end = df['Journey'].mode().to_string(index=False)
    print('Most Popular most frequent combination of start station and end station, journey: ',popular_start_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# Trip Duration
def trip_duration_statistics(df):
    """ Displays statistics on the total and average trip duration. """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time: ',total_travel_time)

    # display arithmetic mean of travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Mean travel time: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# User Info
def user_statistics(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    # use value_counts() function to get a Series containing counts of unique values
    user_types = df['User Type'].value_counts()
    print('User type:\n', user_types)

    # Display counts of gender
    if city == 'NYC' or city == 'Chicago':
        gender_types = df['Gender'].value_counts()
        print('Gender type: \n', gender_types)

    # Display earliest, most recent, and most common year of birth
    earliest_birth_year = int(df['Birth Year'].min())
    print('The earliest birth year: ', earliest_birth_year)

    most_recent_birth_year = int(df['Birth Year'].max())
    print('The most recent birth year: ', most_recent_birth_year)

    most_common_birth_year = int(df['Birth Year'].mode()[0])
    print('The most common birth year: ', most_common_birth_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Using Pyton's main blook to make sure that the script is directly run on its own,
# because the special built-in variable called __name__ will only ever be equal to the string "__main__".
# In other words, the condition if __name__ == "__main__" is just checking whether this module is the main program.

# Use Dataframe.iloc[] for integer-location based indexing for selection by position,(start= 0, end= 5, flag= 1),
# A slice object with integers 0:5.

def main():
    while True:
        city, month, day = get_filters()
        load_data(city, month, day)
        df = load_data(city, month, day)
        time_statistics(df,month,day)
        station_statistics(df)
        trip_duration_statistics(df)
        user_statistics(df, city)
        flag = 1
        start = 0
        end = 5
        while(flag == 1):
            flag = int(input('\nWould you like to view individual trip data? \nType 1 or 2 \n1:True\n2:Flase\n'))
            while((flag != 1) and (flag !=2)):
                flag=int(input('\nPlease enter available input: '))
            print(df.iloc[start:end])
            start += 5
            end += 5

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        restart = restart.lower()
        while((restart != 'yes') and (restart != 'no')):
            restart = input('\nPlease enter available input: ')
        if restart == 'no':
            break
        elif restart == 'yes':
            continue


if __name__ == "__main__":
	main()
