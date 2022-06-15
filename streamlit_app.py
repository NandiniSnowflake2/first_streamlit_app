import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

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
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?' )
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    fruityvice_resonse = requests.get("https://fruityvice.com/api/fruit/" + fruit_choice)
    fruityvice_normalize = pandas.json_normalize(fruityvice_resonse.json())
    streamlit.dataframe(fruityvice_normalize)
except URLError as e:
  streamlit.error()




my_cur = my_cnx.cursor()
my_cur.execute("select * from fruit_load_list")
my_data_rows = my_cur.fetchall()
streamlit.header("The fruit load list contains:")
streamlit.dataframe(my_data_rows)
def insert_row_snowflake(new_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('from streamlit')")
    return "Thanks for adding"+ new_fruit

add_my_fruit = streamlit.text_input('What fruit would you like to add?')
if streamlit.button('Add a fruit to the list'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  back_from_function = insert_row_snowflake(add_my_fruit)
  streamlit.text(back_from_function)
  


