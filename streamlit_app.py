import streamlit as st

st.title("Keira's first app")
st.write(
    "Running on caffeine and confusion [docs.streamlit.io](https://docs.streamlit.io/)."
)
st.image("IMG_1889.jpeg", width=200)

st.title("Code Hard, Cry Harder")
st.header("Aplikasi Mengecek Nilai Genap/Ganjil")
angka = st.number_input("write a number:", value=0, step=1)

if(angka % 2) == 0:
    st.write(f"{angka} adalah Bilangan Genap")
else:
    st.write(f"{angka} adalah Bilangan Ganjil")
