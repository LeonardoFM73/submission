import streamlit as st
import pandas as pd
import joblib

# Load model
model, column_order = joblib.load("model/model.pkl")

# Dictionary untuk mapping label ke angka untuk kolom kategorikal
mappings = {
    "Marital_status": {
        "Single": 1, 
        "Married": 2, 
        "Widower": 3, 
        "Divorced": 4, 
        "Facto union": 5, 
        "Legally separated": 6},
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
    "Course": {
        "Biofuel Production Technologies": 33, 
        "Animation and Multimedia Design": 171,
        "Social Service (evening attendance)": 8014, 
        "Agronomy": 9003, 
        "Communication Design": 9070,
        "Veterinary Nursing": 9085, 
        "Informatics Engineering": 9119, 
        "Equinculture": 9130,
        "Management": 9147, 
        "Social Service": 9238, 
        "Tourism": 9254, 
        "Nursing": 9500,
        "Oral Hygiene": 9556, 
        "Advertising and Marketing Management": 9670, 
        "Journalism and Communication": 9773,
        "Basic Education": 9853, 
        "Management (evening attendance)": 9991
    },
    "Daytime_evening_attendance": {
        "Daytime": 1, 
        "Evening": 0
    },
    "Previous_qualification": {
        "Secondary education": 1,
        "Higher education - bachelor's degree": 2,
        "Higher education - degree": 3,
        "Higher education - master's": 4,
        "Higher education - doctorate": 5,
        "Frequency of higher education": 6,
        "12th year of schooling - not completed": 9,
        "11th year of schooling - not completed": 10,
        "Other - 11th year of schooling": 12,
        "10th year of schooling": 14,
        "10th year of schooling - not completed": 15,
        "Basic education 3rd cycle (9th/10th/11th year) or equiv.": 19,
        "Basic education 2nd cycle (6th/7th/8th year) or equiv.": 38,
        "Technological specialization course": 39,
        "Higher education - degree (1st cycle)": 40,
        "Professional higher technical course": 42,
        "Higher education - master (2nd cycle)": 43
    },
    "Nacionality": {
        "Portuguese": 1, 
        "German": 2, 
        "Spanish": 6, 
        "Italian": 11, 
        "Dutch": 13, "English": 14,
        "Lithuanian": 17, "Angolan": 21, "Cape Verdean": 22, "Guinean": 24, "Mozambican": 25,
        "Santomean": 26, "Turkish": 32, "Brazilian": 41, "Romanian": 62, "Moldova (Republic of)": 100,
        "Mexican": 101, "Ukrainian": 103, "Russian": 105, "Cuban": 108, "Colombian": 109
    },
    "Mothers_qualification": {
        "Secondary Education - 12th Year of Schooling or Eq.": 1,
        "Higher Education - Bachelor's Degree": 2,
        "Higher Education - Degree": 3,
        "Higher Education - Master's": 4,
        "Higher Education - Doctorate": 5,
        "Frequency of Higher Education": 6,
        "12th Year of Schooling - Not Completed": 9,
        "11th Year of Schooling - Not Completed": 10,
        "7th Year (Old)": 11,
        "Other - 11th Year of Schooling": 12,
        "10th Year of Schooling": 14,
        "General commerce course": 18,
        "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
        "Technical-professional course": 22,
        "7th year of schooling": 26,
        "2nd cycle of the general high school course": 27,
        "9th Year of Schooling - Not Completed": 29,
        "8th year of schooling": 30,
        "Unknown": 34,
        "Can't read or write": 35,
        "Can read without having a 4th year of schooling": 36,
        "Basic education 1st cycle (4th/5th year) or equiv.": 37,
        "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
        "Technological specialization course": 39,
        "Higher education - degree (1st cycle)": 40,
        "Specialized higher studies course": 41,
        "Professional higher technical course": 42,
        "Higher Education - Master (2nd cycle)": 43,
        "Higher Education - Doctorate (3rd cycle)": 44
    },
    "Fathers_qualification": {
        "Secondary Education - 12th Year of Schooling or Eq.": 1,
        "Higher Education - Bachelor's Degree": 2,
        "Higher Education - Degree": 3,
        "Higher Education - Master's": 4,
        "Higher Education - Doctorate": 5,
        "Frequency of Higher Education": 6,
        "12th Year of Schooling - Not Completed": 9,
        "11th Year of Schooling - Not Completed": 10,
        "7th Year (Old)": 11,
        "Other - 11th Year of Schooling": 12,
        "2nd year complementary high school course": 13,
        "10th Year of Schooling": 14,
        "General commerce course": 18,
        "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.": 19,
        "Complementary High School Course": 20,
        "Technical-professional course": 22,
        "Complementary High School Course - not concluded": 25,
        "7th year of schooling": 26,
        "2nd cycle of the general high school course": 27,
        "9th Year of Schooling - Not Completed": 29,
        "8th year of schooling": 30,
        "General Course of Administration and Commerce": 31,
        "Supplementary Accounting and Administration": 33,
        "Unknown": 34,
        "Can't read or write": 35,
        "Can read without having a 4th year of schooling": 36,
        "Basic education 1st cycle (4th/5th year) or equiv.": 37,
        "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.": 38,
        "Technological specialization course": 39,
        "Higher education - degree (1st cycle)": 40,
        "Specialized higher studies course": 41,
        "Professional higher technical course": 42,
        "Higher Education - Master (2nd cycle)": 43,
        "Higher Education - Doctorate (3rd cycle)": 44
    },
    "Mothers_occupation": {
        "Student": 0,
        "Legislative/Executive, Directors & Managers": 1,
        "Intellectual and Scientific Specialists": 2,
        "Technicians and Intermediate Professions": 3,
        "Administrative Staff": 4,
        "Personal Services, Security & Sales": 5,
        "Farmers & Skilled Agricultural/Fishery/Forestry Workers": 6,
        "Skilled Workers in Industry/Construction/Crafts": 7,
        "Machine Operators and Assemblers": 8,
        "Unskilled Workers": 9,
        "Armed Forces": 10,
        "Other Situation": 90,
        "Blank": 99,
        "Health Professionals": 122,
        "Teachers": 123,
        "ICT Specialists": 125,
        "Science & Engineering Technicians": 131,
        "Health Technicians/Professionals": 132,
        "Legal/Social/Sports/Cultural Technicians": 134,
        "Secretaries & General Office Workers": 141,
        "Accounting/Finance/Registry Operators": 143,
        "Other Administrative Support Staff": 144,
        "Personal Service Workers": 151,
        "Sellers": 152,
        "Personal Care Workers": 153,
        "Skilled Construction Workers (non-electrician)": 171,
        "Printing/Jewelry/Artisan/Precision Workers": 173,
        "Food/Wood/Clothing Industry Workers": 175,
        "Cleaning Workers": 191,
        "Unskilled Agricultural/Fishery/Forestry Workers": 192,
        "Unskilled Industry/Construction/Transport Workers": 193,
        "Meal Preparation Assistants": 194
    },
    "Fathers_occupation": {
        "Student": 0,
        "Legislative/Executive, Directors & Managers": 1,
        "Intellectual and Scientific Specialists": 2,
        "Technicians and Intermediate Professions": 3,
        "Administrative Staff": 4,
        "Personal Services, Security & Sales": 5,
        "Farmers & Skilled Agricultural/Fishery/Forestry Workers": 6,
        "Skilled Workers in Industry/Construction/Crafts": 7,
        "Machine Operators and Assemblers": 8,
        "Unskilled Workers": 9,
        "Armed Forces": 10,
        "Other Situation": 90,
        "Blank": 99,
        "Armed Forces Officers": 101,
        "Armed Forces Sergeants": 102,
        "Other Armed Forces Personnel": 103,
        "Admin/Commercial Services Directors": 112,
        "Hotel/Catering/Trade/Services Directors": 114,
        "Science/Engineering Specialists": 121,
        "Health Professionals": 122,
        "Teachers": 123,
        "Finance/Admin/PR Specialists": 124,
        "Science/Engineering Technicians": 131,
        "Health Technicians/Professionals": 132,
        "Legal/Social/Sports/Cultural Technicians": 134,
        "ICT Technicians": 135,
        "Secretaries & Data Operators": 141,
        "Accounting/Finance/Registry Operators": 143,
        "Other Administrative Support Staff": 144,
        "Personal Service Workers": 151,
        "Sellers": 152,
        "Personal Care Workers": 153,
        "Protection & Security Services": 154,
        "Market-Oriented Farmers": 161,
        "Subsistence Farmers/Fishermen/Hunters": 163,
        "Skilled Construction Workers (non-electrician)": 171,
        "Metal/Metalworking Workers": 172,
        "Electricians & Electronics Workers": 174,
        "Food/Wood/Clothing Industry Workers": 175,
        "Fixed Plant/Machine Operators": 181,
        "Assembly Workers": 182,
        "Drivers & Equipment Operators": 183,
        "Unskilled Agricultural/Fishery/Forestry Workers": 192,
        "Unskilled Industry/Construction/Transport Workers": 193,
        "Meal Preparation Assistants": 194,
        "Street Vendors/Service Providers": 195
    },


    "Displaced": {"Yes": 1, "No": 0},
    "Educational_special_needs": {"Yes": 1, "No": 0},
    "Debtor": {"Yes": 1, "No": 0},
    "Tuition_fees_up_to_date": {"Yes": 1, "No": 0},
    "Gender": {"Male": 1, "Female": 0},    
    "Scholarship_holder": {"Yes": 1, "No": 0},
    "International": {"Yes": 1, "No": 0}
}

numeric_columns_between = {
    "Application_order": {"label": "Application Order (0 = first choice, 9 = last choice)", "min": 0, "max": 9},
    "Previous_qualification_grade": {"label": "Grade of previous qualification (0-200)", "min": 0, "max": 200},
    "Admission_grade": {"label": "Admission grade (0-200)", "min": 0, "max": 200},
    "Age_at_enrollment": {"label": "Age at enrollment (years)", "min": 0, "max": 100},
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
    "Unemployment_rate",
    "Inflation_rate",
    "GDP" 
]
prediction_labels = {
    0: "Dropout",
    1: "Enrolled",
    2: "Graduate"
}

# Title
st.title("Student Status Prediction App")

# Sidebar / Input Form
with st.form("student_form"):
    inputs = {}

    # Dropdown untuk kolom kategorikal
    for col, mapping in mappings.items():
        inputs[col] = st.selectbox(col, list(mapping.keys()))

    for col, config in numeric_columns_between.items():
        inputs[col] = st.number_input(
        config["label"],
        min_value=config["min"],
        max_value=config["max"],
        step=1
    )
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

    if prediction == "Graduate":
        st.success("Prediction: Graduate 🎓")
    elif prediction == "Enrolled":
        st.success("Prediction: Enrolled 📚")
    elif prediction == "Dropout":
        st.error("Prediction: Dropout ❌")
