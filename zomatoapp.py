# import preprocessor as preprocessor
import streamlit as st
import pandas as pd
import merger
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import help
import plotly.express as px

# import seaborn as sns


df = pd.read_csv('zomato.csv', encoding="ISO-8859-1")
df1 = pd.read_excel('Country-Code.xlsx')

data = merger.merge(df, df1)
temp = merger.india(df, df1)

st.sidebar.title('Zomato Analysis')
# st.sidebar.image("C:\Users\lenovo\PycharmProjects\python\zomato\Zomato_logo.png")

menu = st.sidebar.radio(
    'Select a Option',
    ('Overview', 'India analysis')
)

if menu == 'Overview':
    restaraunt = data['Restaurant_name'].unique().shape[0]
    city = data['City'].unique().shape[0]
    country = data['Country'].unique().shape[0]
    cuisine = data['Cuisines'].unique().shape[0]

    st.title('Overview')

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.header('Restaurant')
        st.title(restaraunt)

    with col2:
        st.header('Countries')
        st.title(country)

    with col3:
        st.header('Cities')
        st.title(city)

    with col4:
        st.header('Cuisines')
        st.title(cuisine)

    fig, ax = plt.subplots(figsize=(5, 3))
    ax = data['Country'].value_counts().plot(kind='bar', color='green')
    st.title('How Many Countries Uses Zomato Application')
    st.pyplot(fig)

    fig, ax = plt.subplots(figsize=(20, 10))
    ax = df.Cuisines.value_counts().head(20).plot(kind='pie', autopct='%.0f%%')
    plt.axis('off')
    st.title('Popular cuisines On Zomato App')
    st.pyplot(fig)

    fig, ax = plt.subplots()
    color = ['#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ff9999']
    ax = df['Currency'].value_counts().plot(kind='barh', color=color)
    st.title('Currencies')
    st.pyplot(fig)

    stopwords = set(STOPWORDS)
    comment_words = ''
    for line in data.Restaurant_name:
        words = line.lower().split()
        comment_words += ' '.join(words) + ' '
    wordcloud = WordCloud(width=1000, height=800, background_color='black', colormap='OrRd', stopwords=stopwords,
                          min_font_size=10).generate(comment_words)
    plt.figure(figsize=(9, 9), facecolor=None)
    plt.imshow(wordcloud)
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title('Frequent Words in Restaurant Names')
    st.pyplot()

    country_list = data['Country'].unique().tolist()
    country_list.sort()
    # country_list.insert(0,'Overall')
    # st.sidebar('Select A Country',country_list)
    country_df = st.sidebar.selectbox('Select A Country ', options=country_list)

    st.title('Top Restaurants Of ' + country_df)
    top = help.top_rated_rest(data, country_df)
    st.table(top)

    rest = help.country_wise_rest(data, country_df)
    fig = px.line(rest, x='Restaurant_name', y='Average Cost for two', width=800, height=600)
    st.title('Average Cost Of ' + country_df + ' Restaurants')
    st.plotly_chart(fig)

if menu == 'India analysis':
    name = temp['Restaurant Name'].unique().shape[0]
    cityy = temp['City'].unique().shape[0]
    cuisines = temp['Cuisines'].unique().shape[0]

    st.title('Overview')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header('Restaurants')
        st.title(name)

    with col2:
        st.header('Cities')
        st.title(cityy)

    with col3:
        st.header('Cuisines')
        st.title(cuisines)

    fig, ax = plt.subplots(figsize=(10, 6))
    color = ['#e377c2', '#7f7f7f', '#bcbd22', '#17becf', '#ff9999']
    ax = temp['Cuisines'].value_counts().sort_values(ascending=False).head(10).plot(kind='barh', color=color)
    st.title('Popular Cuisines in India')
    st.pyplot(fig)

    city_list = temp['City'].unique().tolist()
    city_list.sort()
    city_list = st.sidebar.selectbox('Select A City ', options=city_list)

    st.title('Top Restaurants of ' + city_list)
    city_rest = help.city_rest(temp, city_list)
    st.table(city_rest)

    city_cost = help.city_avg_cost(temp, city_list)
    fig = px.line(city_cost, x='Restaurant Name', y='Average Cost for two', width=800, height=600)
    st.title('Average Cost Of ' + city_list + ' Restaurants')
    st.plotly_chart(fig)
