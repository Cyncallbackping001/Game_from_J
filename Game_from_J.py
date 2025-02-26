import streamlit as st

def check(password):
    count_special = 0
    count_eng = 0
    for simbol in password:
        if simbol in "!@#$%^&*()_-+={}[]'><~:;":
            count_special += 1
        elif simbol in "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm":
            count_eng += 1

    if len(password) < 5:
        st.markdown("<h1 style='text-align: center; color: red;'>You...</h1>", unsafe_allow_html=True)
    elif len(password) > 20:
        st.markdown("<h1 style='text-align: center; color: red;'>MAX is 20!</h1>", unsafe_allow_html=True)
    elif "?!" in password:
        st.markdown("<h1 style='text-align: center; color: red;'>you're worthless and terrible!</h1>",unsafe_allow_html=True)
    elif count_special < 4:
        st.markdown("<h1 style='text-align: center; color: red;'>Moron bot! Hello? MINIMUM IS 4!!!!</h1>", unsafe_allow_html=True)
    elif  count_eng == 0:
        st.markdown("<h1 style='text-align: center; color: red;'>Oh, grow up! NOT ENGLISH?!</h1>",unsafe_allow_html=True)
    else:
        st.markdown(
            "<h1 style='text-align: center; color: yellow;'>Am I dreaming or did you do something not useless for once?</h1>",unsafe_allow_html=True)
        st.markdown("<h1 style='text-align: center; color: yellow;'>Equity partner</h1>", unsafe_allow_html=True)
        st.image("SDJ.png")

st.markdown("<h1 style='text-align: center; color: yellow;'>Password game from J</h1>",unsafe_allow_html=True)
st.subheader("J want to play with you >:D")
p = st.text_input("Enter a password",max_chars=50, type= "password")
check(p)
