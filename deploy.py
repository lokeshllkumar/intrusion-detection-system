import streamlit as st
import numpy as np
import pickle as pk

st.title("Intrusion Detection System")

with open("models\logistic_pickle.pkl", "rb") as file:
    logistic_model = pk.load(file)

with open("models\decision_tree_pickle.pkl", "rb") as file:
    decision_tree_model = pk.load(file)

with open("models\gnb_pickle.pkl", "rb") as file:
    gnb_pickle = pk.load(file)

with open("models\gradient_tree_pickle.pkl", "rb") as file:
    gradient_tree_pickle = pk.load(file)