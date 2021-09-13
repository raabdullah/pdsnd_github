import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
cities = ['chicago', 'new york city', 'washington']
months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'saturday', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday']
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
    while True:
        try:
            city= str(input('Which city would you like to investigate? ')).lower()
            if city in cities:
                True
            else:
                print('Oops! That\'s not a valid input. Please, try again!')
                continue
        # TO DO: get user input for month (all, january, february, ... , june)
            month= str(input('Is there a certain month you want to filter by? If irrelevent, please type "all". ')).lower()
            if month in months:
                True
            else:
                print('Oops! That\'s not a valid input. Please, try again!')
                continue

        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
            day= str(input('What day of the week would you like information on? If irrelevent, please type "all". ')).lower()
            if day in days:
                True
                break
            else:
                print('Oops! That\'s not a valid input. Please, try again!')
                continue
            break
        except ValueError:
            print('Oops! That\'s not a valid input. Please, try again!')

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month) + 1
            df = df[df['month'] == month]

    if day != 'all':
            df = df[df['day_of_week'] == day.title()]

    while True:
        view_data = str(input("Would you like to view 5 rows of data? Enter yes or no.")).lower()
        start_loc = 0
        if view_data == 'yes':
            print(df.iloc[start_loc])
            start_loc += 5
            view_display = str(input("Do you wish to continue? Please type yes or no. ")).lower()
            break
        elif view_data == 'no':
            break


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('The most common month: ', common_month)

   # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('The most common day of week: ', common_day)

    # TO DO: display the most common start hour
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('The most common hour: ', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_common_start = df['Start Station'].value_counts()
    print('The most common start station: ', most_common_start)

    # TO DO: display most commonly used end station
    most_common_end = df['End Station'].value_counts()
    print('The most common end station: ', most_common_end)

    # TO DO: display most frequent combination of start station and end station trip
    most_common_trip = df['Start Station'].value_counts() + df['End Station'].value_counts()
    print('The most common trip route: ', most_common_trip)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    start_time_sum = df['Start Station'].sum()
    end_time_sum = df['Start Station'].sum()
    total_travel_time = start_time_sum + end_time_sum
    print('Total travel time: ', total_travel_time, 'seconds.')

    # TO DO: display mean travel time
    mean_travel_time = total_travel_time.mean()
    print('Travel time mean: ', mean_travel_time , 'seconds')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    usertypes_count = df['User Type'].value_counts()
    print('User types count: ', usertypes_count)


    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('Gender count: ', gender_count)
    else:
        print('Sorry! This city does not have gender information! Please, try again.')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print('Earliest year of birth: ', df['Birth Year'].max())
        print('Most recent year of birth: ', df['Birth Year'].min())
        print('Most common year of birth: ', df['Birth Year'].value_counts())
    else:
        print('Sorry! This city does not have birth year information! Please, try again.')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
            city, month, day = get_filters()
            df = load_data(city, month, day)

            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)

            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() != 'yes':
                break


if __name__ == "__main__":
	main()
