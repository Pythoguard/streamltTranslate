import streamlit as st
import datetime as dt
from googletrans import Translator

trans=Translator()

st.title('First streamlit project')
now=dt.datetime.now()

st.write(f"it is now {now}")

input_text=st.text_input('Enter English  Word')
dict={'hindi':'hi','English':'en','japani':'ja'}
option = st.selectbox( 'Choose Language in this menu',('hindi','English','japani'))



if st.button('Translate'):

    result=trans.translate(input_text,dest=dict[option]).text
    st.success(result)
    st.write(type(dict[option]))
    st.write('You selected:',dict[option])
