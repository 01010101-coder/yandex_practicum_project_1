def count_by_time(city, day, time1, time2, df):
    df_time = df[df['day'] == 'Monday']
    df_time = df_time[df_time['time'] >= time1]
    df_time = df_time[df_time['time'] <= time2]
    df_time = df_time.groupby('genre')['genre'].count().sort_values(ascending=False)
    return df_time