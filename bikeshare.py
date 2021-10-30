import time
import pandas as pd
import numpy as np

#Selection of categories used for user filtering

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months =  ['all', 'january', 'february', 'march', 'april', 'may', 'june' ]
days =  ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday' ]
   
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
     name_city = input("\nChose a city to analyze between chicago, new york city, washington please\n")
            if name_city.lower() in CITY_DATA:
                city_access = CITY_DATA[name_city.lower()]
            else:
            print("\nSorry, we did not find the selected city, please choose one of the given options. thank you.\n")
                
                
    # TO DO: get user input for month (all, january, february, ... , june)
    month_name = input("\nEnter the month to analyze, you must write the complete name, you can select any month betwwen January and june\n")
        if month_name.lower() in months:
            month_access = month_name.lower()
        else:
            print("\nwe cannot filter the selected option, please enter a month that falls within the given range.\n")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_name = input("\nPlease enter the day of the week on which you want to perform the analysis.\n")
        if day_name.lower() in days:
            day_access = day_name.lower()
        else:
            print("\we can't find the day entered, remember to enter the full name\n")
   print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
df = pd.read_csv(CITY_DATA[city])
# convert the Start Time column to datatime
df['Start Time'] = pd.to_datetime(df['Start Time'])
#extract month and day of week from start time to create 
df['month'] = df['Start Time'].dt.month
df['day_week'] = df['Start Time'].dt.day_name
df['hour'] = df['Start Time'].dt.hout
#filter by month if applicable
if month != 'all':
    months =  ['january', 'february', 'march', 'april', 'may', 'june' ]
    month = months.index(month) + 1
# filter by month to create the new dataframe
    df = df [df['month'] == month]
# filter by day of week if applicable
if day != 'all'
    df = df [df['day_week'] == day.title()]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
   print("the most common month is:", df['month'].mode()[0])

    # TO DO: display the most common day of week
    print("the most common day of week is:", df['day_week'].mode()[0])

    # TO DO: display the most common start hour
    print("the most common start hour is:", df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("the most commonly used start station is:", df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print("the most commonly used end station is:", df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print(" the most frequent combination of start station and end station trip is:", ( df['Start Station'] + " " +df['End Station'])mode()[0])
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time is:", df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("The mean travel time is:", df['Trip Duration'].mean())

    print("The max travel time is:", df['Trip Duration'].max())


    print("The min travel time is:", df['Trip Duration'].min())

    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of user types is:", df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if city_access == 'chicago.csv' or  city_access == 'new_york_city.csv':
        print("the counts of gender is:", df['Gender']..value_counts())
    else:
        print("the city entered does not have this information")

    # TO DO: Display earliest, most recent, and most common year of birth
    if city_access == 'chicago.csv' or  city_access == 'new_york_city.csv':
        print("The earliest birth is", df['Birth Year'].max())
        print("The most recent birth is", df['Birth Year'].min())
        print("The most common birth is", df['Birth Year'].mode()[0])
        

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

print(df.head())
    x = 0
    while true:
        rows = input("\nyou want to see five more rows? Enter yes or no\n")
            if rows.lower() != 'yes':
                return
            x = x + 5
            print(df.head(x + 5))
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        while true:
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
        

if __name__ == "__main__":
	main()
