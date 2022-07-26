def merge(df, df1):
    df = df.merge(df1, on='Country Code', how='left')
    df.rename(columns={'Restaurant Name': 'Restaurant_name'}, inplace=True)

    return df


def india(df, df1):
    df = df.merge(df1, on='Country Code', how='left')
    df = df[df['Country'] == 'India']
    # df.rename(columns={'Restaurant Name': 'Restaurant_name'}, inplace=True)

    return df
