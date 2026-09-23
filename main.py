import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

import streamlit as st
import math

import streamlit as st
import math

# Configuración de la página
st.set_page_config(page_title="Resolución de Ejercicios", layout="wide")

st.sidebar.title("Navegación")
opcion = st.sidebar.radio("Selecciona una sección:", [
    "1. Geometría (Áreas y Perímetros)", 
    "2. Propiedades de los Números", 
    "3. Explicación YOLO"
])

# ==============================================================================
# PUNTO 1: GEOMETRÍA
# ==============================================================================
if opcion == "1. Geometría (Áreas y Perímetros)":
    st.header("1. Cálculo de Área y Perímetro de Figuras Geométricas")
    
    figura = st.selectbox("Selecciona una figura geométrica:", [
        "Cuadrado", "Rectángulo", "Triángulo", "Círculo", "Paralelogramo"
    ])
    
    st.divider()

    # --- CUADRADO ---
    if figura == "Cuadrado":
        st.subheader("Cuadrado")
        
        col1, col2 = st.columns(2)
        with col1:
            lado = st.number_input("Lado (l):", min_value=0.0, value=5.0)
            area = lado ** 2
            perimetro = 4 * lado
            
            st.write("### Fórmulas:")
            st.latex(r"Área = l^2")
            st.latex(r"Perímetro = 4 \cdot l")
            
            st.success(f"**Área:** {area:.2f}")
            st.success(f"**Perímetro:** {perimetro:.2f}")

        with col2:
            st.write("### Representación:")
            st.markdown("""
            ```
            +-----------+
            |           |
            |           |  l
            |           |
            +-----------+
                  l
            ```
            """)

    # --- RECTÁNGULO ---
    elif figura == "Rectángulo":
        st.subheader("Rectángulo")
        
        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Base (b):", min_value=0.0, value=6.0)
            altura = st.number_input("Altura (h):", min_value=0.0, value=4.0)
            
            area = base * altura
            perimetro = 2 * (base + altura)
            
            st.write("### Fórmulas:")
            st.latex(r"Área = b \cdot h")
            st.latex(r"Perímetro = 2 \cdot (b + h)")
            
            st.success(f"**Área:** {area:.2f}")
            st.success(f"**Perímetro:** {perimetro:.2f}")

        with col2:
            st.write("### Representación:")
            st.markdown("""
            ```
            +---------------+
            |               |  h
            +---------------+
                    b
            ```
            """)

    # --- TRIÁNGULO ---
    elif figura == "Triángulo":
        st.subheader("Triángulo")
        
        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Base (b):", min_value=0.0, value=5.0)
            altura = st.number_input("Altura (h):", min_value=0.0, value=4.0)
            lado_a = st.number_input("Lado a:", min_value=0.0, value=5.0)
            lado_c = st.number_input("Lado c:", min_value=0.0, value=5.0)
            
            area = (base * altura) / 2
            perimetro = lado_a + base + lado_c
            
            st.write("### Fórmulas:")
            st.latex(r"Área = \frac{b \cdot h}{2}")
            st.latex(r"Perímetro = a + b + c")
            
            st.success(f"**Área:** {area:.2f}")
            st.success(f"**Perímetro:** {perimetro:.2f}")

        with col2:
            st.write("### Representación:")
            st.markdown("""
            ```
                  /\ 
             a   /  \   c
                / h | \ 
               /----|--\ 
                   b
            ```
            """)

    # --- CÍRCULO ---
    elif figura == "Círculo":
        st.subheader("Círculo")
        
        col1, col2 = st.columns(2)
        with col1:
            radio = st.number_input("Radio (r):", min_value=0.0, value=3.0)
            
            area = math.pi * (radio ** 2)
            perimetro = 2 * math.pi * radio
            
            st.write("### Fórmulas:")
            st.latex(r"Área = \pi \cdot r^2")
            st.latex(r"Perímetro = 2 \cdot \pi \cdot r")
            
            st.success(f"**Área:** {area:.2f}")
            st.success(f"**Perímetro:** {perimetro:.2f}")

        with col2:
            st.write("### Representación:")
            st.markdown("""
            ```
                 ***
              *       *
             *    .--r *
              *       *
                 ***
            ```
            """)

    # --- PARALELOGRAMO ---
    elif figura == "Paralelogramo":
        st.subheader("Paralelogramo")
        
        col1, col2 = st.columns(2)
        with col1:
            base = st.number_input("Base (b):", min_value=0.0, value=6.0)
            lado = st.number_input("Lado inclinado (a):", min_value=0.0, value=4.0)
            altura = st.number_input("Altura (h):", min_value=0.0, value=3.5)
            
            area = base * altura
            perimetro = 2 * (base + lado)
            
            st.write("### Fórmulas:")
            st.latex(r"Área = b \cdot h")
            st.latex(r"Perímetro = 2 \cdot (a + b)")
            
            st.success(f"**Área:** {area:.2f}")
            st.success(f"**Perímetro:** {perimetro:.2f}")

        with col2:
            st.write("### Representación:")
            st.markdown("""
            ```
                 +---------------+
                /               /  a
              /  | h          /
            +---------------+
                    b
            ```
            """)


# ==============================================================================
# PUNTO 2: PROPIEDADES DE LOS NÚMEROS
# ==============================================================================
elif opcion == "2. Propiedades de los Números":
    st.header("2. Evaluación de Números (Par/Impar, Primo, Divisibilidad)")
    
    num = st.number_input("Ingresa un número entero principal:", step=1, value=7)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Evaluación Par / Impar")
        # Explicación
        st.markdown("**¿Cómo sabemos si es par o impar?** Un número es par si al dividirlo entre 2 su residuo es 0 (`num % 2 == 0`). De lo contrario, es impar.")
        
        if num % 2 == 0:
            st.info(f"El número **{num}** es **PAR**.")
        else:
            st.info(f"El número **{num}** es **IMPAR**.")

        st.subheader("Evaluación de Número Primo")
        # Explicación
        st.markdown("**¿Cómo sabemos si es primo?** Un número mayor a 1 es primo si solo tiene dos divisores positivos: el 1 y él mismo.")
        
        is_primo = True
        if num <= 1:
            is_primo = False
        else:
            for i in range(2, int(math.isqrt(abs(num))) + 1):
                if num % i == 0:
                    is_primo = False
                    break
        
        if is_primo:
            st.success(f"El número **{num}** **ES PRIMO**.")
        else:
            st.error(f"El número **{num}** **NO ES PRIMO**.")

    with col2:
        st.subheader("Evaluación de Divisibilidad")
        st.markdown("**¿Cómo sabemos si es divisible por otro número?** Un número $A$ es divisible por $B$ si el residuo de $A / B$ es 0 (`A % B == 0`).")
        
        divisor = st.number_input("Ingresa el segundo número (divisor):", step=1, value=3)
        
        if divisor == 0:
            st.warning("No se puede dividir por cero.")
        else:
            if num % divisor == 0:
                st.success(f"El número **{num}** **ES divisible** exactamente por **{divisor}**.")
            else:
                st.error(f"El número **{num}** **NO es divisible** exactamente por **{divisor}** (Residuo = {num % divisor}).")


