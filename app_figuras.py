import streamlit as st
import math

# ---------------------------------------------------------
# Configuración de la página
# ---------------------------------------------------------
st.set_page_config(
    page_title="Calculadora de Área y Perímetro",
    page_icon="📐",
    layout="centered"
)

st.title("📐 Calculadora de Área y Perímetro")
st.write(
    "Selecciona una figura geométrica, ingresa sus medidas y obtén "
    "su área y perímetro."
)

# ---------------------------------------------------------
# Funciones de cálculo (una por figura)
# ---------------------------------------------------------
def calcular_rectangulo(base, altura):
    area = base * altura
    perimetro = 2 * (base + altura)
    return area, perimetro


def calcular_cuadrado(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro


def calcular_triangulo(base, altura, lado1, lado2, lado3):
    area = (base * altura) / 2
    perimetro = lado1 + lado2 + lado3
    return area, perimetro


def calcular_circulo(radio):
    area = math.pi * radio ** 2
    perimetro = 2 * math.pi * radio
    return area, perimetro


def calcular_paralelogramo(base, altura, lado):
    area = base * altura
    perimetro = 2 * (base + lado)
    return area, perimetro


# ---------------------------------------------------------
# Interfaz: selección de figura
# ---------------------------------------------------------
figura = st.selectbox(
    "Selecciona la figura:",
    ["Rectángulo", "Cuadrado", "Triángulo", "Círculo", "Paralelogramo"]
)

st.subheader(f"Datos del {figura}")
area = None
perimetro = None

# ---------------------------------------------------------
# Entradas dinámicas según la figura elegida
# ---------------------------------------------------------
if figura == "Rectángulo":
    base = st.number_input("Base", min_value=0.0, step=0.1, format="%.2f")
    altura = st.number_input("Altura", min_value=0.0, step=0.1, format="%.2f")
    if st.button("Calcular"):
        area, perimetro = calcular_rectangulo(base, altura)

elif figura == "Cuadrado":
    lado = st.number_input("Lado", min_value=0.0, step=0.1, format="%.2f")
    if st.button("Calcular"):
        area, perimetro = calcular_cuadrado(lado)

elif figura == "Triángulo":
    st.caption("Para el área se usan base y altura; para el perímetro, los 3 lados.")
    base = st.number_input("Base", min_value=0.0, step=0.1, format="%.2f")
    altura = st.number_input("Altura", min_value=0.0, step=0.1, format="%.2f")
    col1, col2, col3 = st.columns(3)
    with col1:
        lado1 = st.number_input("Lado 1", min_value=0.0, step=0.1, format="%.2f")
    with col2:
        lado2 = st.number_input("Lado 2", min_value=0.0, step=0.1, format="%.2f")
    with col3:
        lado3 = st.number_input("Lado 3", min_value=0.0, step=0.1, format="%.2f")
    if st.button("Calcular"):
        area, perimetro = calcular_triangulo(base, altura, lado1, lado2, lado3)

elif figura == "Círculo":
    radio = st.number_input("Radio", min_value=0.0, step=0.1, format="%.2f")
    if st.button("Calcular"):
        area, perimetro = calcular_circulo(radio)

elif figura == "Paralelogramo":
    base = st.number_input("Base", min_value=0.0, step=0.1, format="%.2f")
    altura = st.number_input("Altura", min_value=0.0, step=0.1, format="%.2f")
    lado = st.number_input("Lado inclinado", min_value=0.0, step=0.1, format="%.2f")
    if st.button("Calcular"):
        area, perimetro = calcular_paralelogramo(base, altura, lado)

# ---------------------------------------------------------
# Resultados
# ---------------------------------------------------------
if area is not None and perimetro is not None:
    st.success("Resultados:")
    col1, col2 = st.columns(2)
    col1.metric("Área", f"{area:.2f}")
    col2.metric("Perímetro", f"{perimetro:.2f}")

st.divider()
st.caption("Desarrollado con Streamlit · Fórmulas geométricas básicas")
