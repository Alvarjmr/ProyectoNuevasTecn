import streamlit as st
import matplotlib.pyplot as plt

# Set the page title and header
st.title("Proyecto Integrador")
st.header("Bienvenido a nuestro Proyecto Integrador")

# Hero Section with image and project description
st.image("logo.jpg", width=600)
st.write("*Descripción del proyecto:* Se basa en las demandas de los empleados en las oficinas publicas")

# Project Overview
st.subheader("Resumen del Proyecto")
st.write("- Si quiere calcular su liquidación, ingrese la fecha de inicio y de fin de su contrato o relación laboral usando el calendario. Tenga en cuenta que el estimado de liquidaciones y costos se calculan por año calendario.")
st.write("- Ingrese el valor del salario.")


# Features and Benefits
st.subheader("Importante:")
st.write("*Las liquidaciones se calculan y efectúan año a año. La Calculadora no permite ingresar periodos que superen el año calendario.")
st.write("*Recuerde indicar si recibe o no auxilio de transporte. Los trabajadores que devenguen más de dos salarios mínimos no tienen derecho a auxilio de transporte.")
st.write("*El salario devengado no puede ser inferior al Salario Mínimo.")



# Call to Action
st.subheader("¡Toma Acción!")
st.write("*Visite nuestro sitio web:* [Enlace al sitio web del proyecto](https://nominavalentino.com)")
st.write("*Contáctenos:* [Enlace al correo electrónico de contacto](mailto:nominavalentino@gmail.com)")

# Footer with team members and project information
st.subheader("Equipo y Contacto")
st.write("*Miembros del equipo:*")
st.write("- Nombre 1:Alvaro Javier Martinez Rubio")

st.write("*Información de contacto:*")
st.write("Correo electrónico: [Enlace al correo electrónico de contacto](mailto:nominavalentino@gmail.com)")