import streamlit as st

def bienvenido(nombre):
    mymessage = "Bienvenido /a/e " + nombre
    
myname = st.text_input("Nombre: ")
if (myname):
    mensaje = bienvenido(myname)
    st.write(f"Result: {mensaje}")