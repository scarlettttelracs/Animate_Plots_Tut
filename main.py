import plotly_express as px
import streamlit as st
import pandas as pd

header = st.container()
LifeExp = st.container()
CovidCases = st.container()
with header:
    st.title("This is a test file for animate plots")

with LifeExp:
    #First Graph LifeExp v.s. gdp per capita
    df = px.data.gapminder()
    st.text("This dataset contains data of life experience, population, gdp per capita \nof variate countries.")
    st.write(df.head(10))

    #If put the next 3 lines back and remove "animation_frame="year", animation_group="country"", it will be a normal
    #selection of year and the graph will be just for that year
    #year_options = df['year'].unique().tolist()
    #year = st.selectbox('which year would you like to see?', year_options, 0)
    #df = df[df['year']==year] want to see all the years, so do not filter

    fig = px.scatter(df, x = "gdpPercap", y="lifeExp",
                     size = "pop", color = "continent", hover_name = "continent",
                     log_x=True, size_max = 55, range_x = [100,10000],range_y = [25,90],
                     animation_frame="year", animation_group="country")

    fig.update_layout(width=800)

    st.write(fig)
with CovidCases:

    #Second bar chart, covid cases confirmed v.s. ctry
    #Read from a csv from github
    covid = pd.read_csv("https://raw.githubusercontent.com/shinokada/covid-19-stats/master/data/daily-new-confirmed-cases-of-covid-19-tests-per-case.csv")

    covid.columns = ['Country', 'Code', 'Date', 'Confirmed','Days since confirmed']
    covid['Date'] = pd.to_datetime(covid['Date']).dt.strftime('%Y-%m-%d')

    st.text("This dataset contains numbers of confirmed Covid cases and the corresponding date \nin different countries.")

    st.write(covid.head(20))
    country_options = covid['Country'].unique().tolist()
    date_options = covid['Date'].unique().tolist()
    date = st.selectbox('Which date would you like to see?', date_options, 100)
    country = st.multiselect('Which country would you like to see?', country_options, ['Brazil'])

    covid = covid[covid['Country'].isin(country)]
    #covid = covid[covid['date'] == date]

    fig2 = px.bar(covid, x = 'Country', y = 'Confirmed', color = 'Country',
                  range_y = [0, 35000], animation_group='Country', animation_frame='Date')

    #Speed up the change
    fig2.layout.updatemenus[0].buttons[0].args[1]['frame']['duration'] = 30
    fig2.layout.updatemenus[0].buttons[0].args[1]['transition']['duration'] = 5

    fig2.update_layout(width = 800)

    st.write(fig2)