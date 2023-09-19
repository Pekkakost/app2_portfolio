import pandas
import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")


with col2:
    st.title("Ardit Sulce")
    content = """
    Heippa, nauttaa silta etta aika vaativa kurssi,
    kuitenkin hyvaa opetusta ja oppii myos 
    kovakalloinenkin mies
    
    """

    st.info(content)

content2 = """
    nain se menee varmaan paremmin voi jatkaa hyvinkin pitkalle taytyy muistaaa
    
    """
st.write(content2)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])
df = pandas.read_csv("data.csv", sep=";")

with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source code]({row['url']})")