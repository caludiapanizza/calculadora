import streamlit as st
st.title(" Mi aplicacion- calculadora")
st.write("Bienvenidos, padres , proyecto de Informatica 9-°")

nombre= st.text_input("¿Cual es el nombre?")
st.write("Hola " , nombre)

 def suma(num1, num2):
     st.write(num1 + num2)

suma(3, 4)


def resta(num1, num2):
 st.write(num1 - num2)

def multiplicacion(num1, num2):
    st.write(num1 * num2)
    
multiplicacion(2, 2)

def division(num1, num2):
    st.write(num1 / num2)


    if st.button("Ver suma"):
        st.write(" suma", suma(3, 4))

        
    if st.button("Ver resta"):
        st.write(" resta", resta(6,7))

        
    if st.button("Ver multiplicacion")
        st.write(" multiplicacion", multiplicacion(2, 2))

    
    if st.button("Ver division"):
        st.write(" division", division(5, 6))
        

        
    
