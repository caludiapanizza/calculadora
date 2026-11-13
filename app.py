import streamlit as st
st.title("Calculadora")

nombre= st.text_input("¿como te llamas?.Escribi tu nombre aca:")

if nombre:
    st.write("Hola mia  que lindo que estes aca")
    st.write("Vamos a calcular juntos")

numero1 = st.number_input("Pone el primer numero:" , value=0)
numero2 = st.number_input("Pone el segundo numero:" , value=0)

operacion = st.selectbox("¿Que queres hacer?" ,[ "suma", "resta","multiplicacion," "division"])

if st.button("calcular"):
    if operacion == "suma":
        resultado = numero1 + numero2
        st.success(f"mia , la suma es: {resultado}")

elif  operacion == "Resta":
    resultado = numero1 - numero2
    st.success(f"mia, la resta es {resultado}")


elif  operacion == "multiplicacion":
    resultado = numero1 * numero2
    st.success(f"mia, la multiplicacion es {resultado}")

elif  operacion == "division":
    if numero2 == 0:
        st.error("No se puede dividir entre 0")
    else:
        resultado = numero1 / numero2
        st.success(f"mia, la division es: {resultado}")
    else:
        st.write("Primero escribi tu nombre arriba")
    



