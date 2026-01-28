# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 10:16:50 2026

@author: vqomf
"""

import streamlit as st

st.write("Vuyiseka Qomfo Streamlit App")

st.write("Day3")

st.title("My first streamlit App")

number = st.slider("pick an number", 1, 100)


st.write(f"you picked {number}")
