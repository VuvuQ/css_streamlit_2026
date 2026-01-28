# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 10:16:50 2026

@author: vqomf
"""

import streamlit as st

st.title("Vuyiseka Qomfo's Personal Research App")

st.write("Day3")

st.write("My first streamlit App")

number = st.slider("pick an number", 1, 100)


st.write(f"you picked {number}")

