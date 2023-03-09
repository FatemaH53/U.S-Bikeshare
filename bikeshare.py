import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
CITY = ['new york city' , 'chicago' , 'washington']
MONTH = ['jan' , 'feb' , 'mar', 'apr', 'may' , 'jun' ]
DAY = ['sunday' , 'monday' , 'tuesday' , 'wednesday' ,'thursday' , 'friday' , 'saturday']

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
        city = input( 'which city? - new york city , chicago or washington \n')
        if city in CITY:
            break
    # TO DO: get user input for month (all, january, february, ... , june)

    while True:
        
        month = input('Which month ? Enter first 3 letters of the month, all small \n')
        if month in MONTH:
            break
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day?\n' )
        if day in DAY:
            break
            
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
    df['day'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all' :
        if month in MONTH:
            month = MONTH.index(month) + 1
            df = df[ df['month'] == month]
        else:
            df = pd.DataFrame([])

            
       
             
    if day != 'all' :
        df = df[ df['day'] == day.title()]
    return df

           
        




   

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    mnths = df['month'] .value_counts().idxmax()
    print("The most common month is : " , mnths)


    # TO DO: display the most common day of week
    Dag = df['day'].value_counts().idxmax()
    print("The most common day is : " , Dag)


    # TO DO: display the most common start hour
    uur = df['hour'].value_counts().idxmax()
    print("The most common start hour is : " , uur)
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    Start_station = df['Start Station'].value_counts().idxmax()
    print("the most used start station : " , Start_station)


    # TO DO: display most commonly used end station
    End_station = df['End Station'].value_counts().idxmax()
    print("the most used end station : " , End_station)


    # TO DO: display most frequent combination of start station and end station trip
    Start_End = df[['Start Station' , 'End Station']] .mode().loc[0]
    print("The most used start station and end station :{} , {}"  .format(Start_End[0] , Start_End[1]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    Total_time = df['Trip Duration'].sum()
   
    print("The total travel time is : " , Total_time)
   
          


    # TO DO: display mean travel time
    Mean_travel = df['Trip Duration'].mean()
    print("The mean travel time is : " , Mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    User_type = df['User Type'].value_counts()
    print("The different counts of user types is:")
    print(User_type.to_string())


    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender = df['Gender'].value_counts()
        print(" The total count of gender is : ")
        print(gender.to_string())
    else:
        print("No gender info avialable.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        
        earliest_DOB = int(df['Birth Year'].min())
        

        print(" The earliest year of birth is : " , earliest_DOB)
        recent_DOB = int(df['Birth Year'].max())
        print("The recent year of birth is : " , recent_DOB)
        common_DOB = int(df['Birth Year'].value_counts().idxmax())
        print("The most common year of birth is : " , common_DOB)
    else:
        print("No birth year column exist")
                          


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def view_data(df):
    view_data = input('\n Would you like to view 5 rows of the trip data? Enter yes or no \n')
    start_loc = 0
    while view_data.lower() == 'yes':
        
        df_display = df.iloc[start_loc:5+start_loc]
        print(df_display)
        start_loc += 5
        view_data = input('Do you wish to continue?\n').lower()
        if view_data != 'yes':
            break     
      
        print('-'*40)
        


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        if len(df) > 0:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
            view_data(df)  
        else:
            print("data frame is empty")
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
