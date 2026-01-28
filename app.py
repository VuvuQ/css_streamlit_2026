# -*- coding: utf-8 -*-
"""
Created on Wed Jan 28 10:16:50 2026

@author: vqomf
"""

import streamlit as st

st.write("Computing SUmmer School")

st.write("day3")

st.tile("My first streamlit App")

number = st.slider("pick an number", 1, 100)

st.write(f"you picked {number}")