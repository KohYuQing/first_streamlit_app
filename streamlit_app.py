import streamlit 
import requests
import pandas 
import snowflake.connector
from urllib.error import URLError
streamlit.title('My Parents New Healthy Diner')
streamlit.subheader('Breakfast Favourites')
streamlit.markdown('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.markdown('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.markdown('🐔 Hard-Boiled Free-Range Egg')
streamlit.markdown('🥑🍞 Avocado Toast')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
# Let's put a pick list here so they can pick the fruit they want to include 
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
# Display the table on the page.
streamlit.dataframe(my_fruit_list)
