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

src_bytes = st.number_input("src_bytes")
dst_bytes = st.number_input("dest_bytes")
same_srv_rate = st.number_input("same_srv_rate")
flag = st.number_input("flag")
diff_srv_rate = st.number_input("diff_srv_rate")
dst_host_srv_count = st.number_input("dst_host_srv_count")
dst_host_same_srv_rate = st.number_input("dst_host_same_srv_rate")
count = st.number_input("count")
protocol_type = st.number_input("protocol_type")
serror_rate = st.number_input("serror_rate")

predicted_class = gnb_pickle.predict(np.array([[src_bytes, dst_bytes, same_srv_rate, flag, diff_srv_rate, dst_host_srv_count, dst_host_same_srv_rate, count, protocol_type, serror_rate]]))

if st.button("Predict"):
    if predicted_class == 1:
        st.write("Predicted class: Normal")
    elif predicted_class == 0:
        st.write("Predicted class: Anomaly")