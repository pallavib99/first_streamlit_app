import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.header('Breakfast Menu')
streamlit.text('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.text('🐔 Hard-Boiled Free-Range Egg')
streamlit.text('🥑🍞 Avocado Toast')


streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list=my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
fruit_selected= streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Apple','Banana'])
fruit_to_show= my_fruit_list.loc[fruit_selected]

# Display the table on the page.
streamlit.dataframe(fruit_to_show)
streamlit.header('Fruityvice Fruit Advice!')
#fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
def get_fruityvice_data(this_fruit_choice):
  #streamlit.write('The user entered ', fruit_choice)
    fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
    # write your own comment -what does the next line do? 
    fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
    # write your own comment - what does this do?
    return fruityvice_normalized
#streamlit.text(fruityvice_response.json())
try:
  fruit_choice = streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Please select a fruit to get information.")
  else:
    back_from_function=get_fruityvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLERROR as e:
  streamlit.error()

#streamlit.stop()
def insert_rows(add_fruit):
  with my_cnx.cursor() as my_cur:
    my_cur.execute("insert into fruit_load_list values('jackfruit')")
    return "Thanks for adding"+add_fruit
new_fruit=streamlit.text_input('What fruit would you like to add')
if streamlit.button('Add new fruit'):
  my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
  result_fruit=insert_rows(new_fruit)
  streamlit.text(result_fruit)
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
#my_cur.execute("Select * from fruit_load_list")
#my_data_row = my_cur.fetchone()
#my_data_rows = my_cur.fetchall()
#streamlit.text("Hello from Snowflake:")
streamlit.text("Fruit load list contains:")
#streamlit.text(my_data_rows)


