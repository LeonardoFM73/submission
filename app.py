import streamlit as st
import pandas as pd
import joblib

# Load model
model, column_order = joblib.load("model/model.joblib")

# Dictionary untuk mapping label ke angka untuk kolom kategorikal
mappings = {
    "Application_mode": {
        "1st phase - general contingent": 1, 
        "Ordinance No. 612/93": 2,
        "1st phase - special contingent (Azores Island)": 5, 
        "Holders of other higher courses": 7,
        "Ordinance No. 854-B/99": 10, 
        "International student (bachelor)": 15,
        "1st phase - special contingent (Madeira Island)": 16, 
        "2nd phase - general contingent": 17,
        "3rd phase - general contingent": 18, 
        "Ordinance No. 533-A/99, item b2) (Different Plan)": 26,
        "Ordinance No. 533-A/99, item b3 (Other Institution)": 27, 
        "Over 23 years old": 39,
        "Transfer": 42, 
        "Change of course": 43, 
        "Technological specialization diploma holders": 44,
        "Change of institution/course": 51, 
        "Short cycle diploma holders": 53,
        "Change of institution/course (International)": 57
    },

    "Debtor": {"Yes": 1, "No": 0},
    "Tuition_fees_up_to_date": {"Yes": 1, "No": 0},
    "Gender": {"Male": 1, "Female": 0},    
    "Scholarship_holder": {"Yes": 1, "No": 0},
}

numeric_columns = [
    "Curricular_units_1st_sem_credited", 
    "Curricular_units_1st_sem_enrolled",
    "Curricular_units_1st_sem_evaluations", 
    "Curricular_units_1st_sem_approved",
    "Curricular_units_1st_sem_grade",
    "Curricular_units_1st_sem_without_evaluations",
    "Curricular_units_2nd_sem_credited", 
    "Curricular_units_2nd_sem_enrolled",
    "Curricular_units_2nd_sem_evaluations", 
    "Curricular_units_2nd_sem_approved",
    "Curricular_units_2nd_sem_grade",
    "Curricular_units_2nd_sem_without_evaluations", 
]


# Title
st.title("Student Status Prediction App")

# Sidebar / Input Form
with st.form("student_form"):
    inputs = {}

    # Dropdown untuk kolom kategorikal
    for col, mapping in mappings.items():
        inputs[col] = st.selectbox(col, list(mapping.keys()))

    # Numeric input
    for col in numeric_columns:
        inputs[col] = st.number_input(col, min_value=0.0, step=1.0)

    submitted = st.form_submit_button("Predict")

# Saat tombol submit ditekan
if submitted:
    # Ubah label ke angka
    model_input = {}
    for col, val in inputs.items():
        if col in mappings:
            model_input[col] = mappings[col][val]
        else:
            model_input[col] = val

    # Prediksi
    input_df = pd.DataFrame([model_input])
    input_df = input_df[column_order]
    prediction = model.predict(input_df)[0]

    if prediction == 2:
        st.success("Prediction: Graduate 🎓")
    elif prediction == 1:
        st.success("Prediction: Enrolled 📚")
    elif prediction == 0:
        st.error("Prediction: Dropout ❌")
