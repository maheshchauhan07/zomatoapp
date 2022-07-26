def top_rated_rest(data, country):
    data = data[data['Country'] == country]

    x = data['Restaurant_name'].value_counts().reset_index().head(10).merge(data, left_on='index',
                                                                            right_on='Restaurant_name', how='left')[
        ['index', 'City', 'Address', 'Locality', 'Aggregate rating']].drop_duplicates('index').reset_index(drop=True)
    x.rename(columns={'index': 'Restaurant Name'}, inplace=True)

    return x


def country_wise_rest(data, country):
    data = data[data['Country'] == country]

    x = data.groupby('Restaurant_name').sum()['Average Cost for two'].head(20).reset_index()

    return x


def city_rest(temp, city):
    temp = temp[temp['City'] == city]

    x = temp['Restaurant Name'].value_counts().reset_index().head(11).merge(temp, left_on='index',
                                                                            right_on='Restaurant Name', how='left')[
        ['index', 'City', 'Address', 'Locality', 'Aggregate rating']].drop_duplicates('index').reset_index(drop=True)
    x.rename(columns={'index': 'Restaurant Name', 'Aggregate rating': 'Rating'}, inplace=True)
    return x


def city_avg_cost(temp, city):
    temp = temp[temp['City'] == city]
    x = temp.groupby('Restaurant Name').sum()['Average Cost for two'].head(11).reset_index()

    return x
