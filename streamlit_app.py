import streamlit
import pandas
import requests
my_fruitlist = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruitlist = my_fruitlist.set_index('Fruit')
streamlit.title('My Parents New Healthy Diner')
streamlit.header('Breakfast Favorites')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach and Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
fruits_selected = streamlit.multiselect('Pick Some Fruits', list(my_fruitlist.index), ['Avocado', 'Strawberries'])
fruits_to_show = my_fruitlist.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.header('Fruitycive Fruit Advice')
fruit_choice = streamlit.text_input('What fruit would you like information about?' , 'kiwi' )
streamlit.write('The user entered', fruit_choice)
fruityvice_resonse = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)


fruityvice_normalize = pandas.json_normalize(fruityvice_resonse.json())
streamlit.dataframe(fruityvice_normalize)


