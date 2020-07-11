import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input('Would you like to see data for Chicago, New York City, or Washington?\n').lower()
    while city != 'chicago' and  city != 'new york city' and city != 'washington':
        city = input('Please try again \nChicago, New York City, Washington\n').lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    user_choice = input('Would you like to filter the data by month, day, or not at all?\nType ''none'' for no time filter.\n').title()
    while user_choice != 'Month' and user_choice != 'Day' and  user_choice !='None':
       user_choice = input('Please, try again \nMonth, Day, or None:\n').title()

    if user_choice == 'Month':
        day = 'all'
        month = input('Which month - January, February, March, April, May, or June?\n').title()
        while month!='January' and month!='February' and month!='March' and month!='April' and  month!='May' and month!='June':
            month = input('Please try again \nJanuary, February, March, April, May, or June?\n').title()
    elif user_choice == 'Day':
        month= 'all'
        day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n').title()
        while day!='Monday' and day!='Tuesday' and day!='Wednesday' and day!='Thursday' and  day!='Thursday' and day!='Fdriday' and day!='Saturday' and day!='Sunday':
            day = input('Please try again \nSunday, Monday, Tuesday, Wednesday...\n').title()


    elif user_choice =='None':
        month='all'
        day='all'


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze Chicago, New York City, or Washington
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
        Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
   # df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month.lower()) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['January', 'February', 'March', 'April', 'May', 'June']
    print('Most common month: {}'.format(months[df['month'].mode()[0]-1]))

    # TO DO: display the most common day of week
    print('Most common day of the week: {}'.format(df['day_of_week'].mode()[0]))

    # TO DO: display the most common start hour
    #print( df['hour'].mode()[0])
    print('Most common start hour: {}'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    input('Press ENTER to continue.')


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nMost commonly used start station: \n{}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('\nMost commonly used end station: \n {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print('\nMost frequent combination of start station and end station trip :\n {}'.format(df.groupby(['Start Station','End Station']).size().idxmax()))
  #  print(df.groupby(['Start Station','End Station']).size().idxmax())
 #   print(df[['Start Station','End Station']].mode()[0])
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    input('Press ENTER to continue.')

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal travel time: {} hours'.format(df['Trip Duration'].sum()/3600))

    # TO DO: display mean travel time
    print('\nMean travel time: {} seconds.'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    input('Press ENTER to continue.')

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type=df['User Type'].value_counts()
    print('\nCounts of user types: \n{}'.format(user_type))

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        gender = df['Gender'].value_counts()
        print('\nCounts of Gender: \n{}'.format(gender))

    # TO DO: Display earliest, most recent, and most common year of birth
        print("\nEarliest year of birth: {}".format(df['Birth Year'].min()))
        print("\nMost recent year of birth: {}".format(df['Birth Year'].max()))
        print("\nMost common year of birth: {}".format(df['Birth Year'].mode()[0]))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    user_raw = input(' Do you want to see 5 rows of data?').title()
    start_loc = 0
    while user_raw == 'Yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        user_raw = input("Do you wish to continue?: ").title()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
