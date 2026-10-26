import streamlit as st
import pandas as pd

st.title("تطبيق بسيط لتنظيف ملفات الـ CSV")
st.write("هذا التطبيق يساعدك على رفع ملف CSV، معرفة عدد صفوفه، تنظيفه، ثم تحميله.")

uploaded_file = st.file_uploader("اختر ملف CSV لرفعه", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    st.subheader("معلومات الملف قبل التنظيف:")
    original_rows = df.shape[0]
    st.write(f"عدد الصفوف في الملف: {original_rows}")
    
    with st.expander("معاينة البيانات الأصلية"):
        st.dataframe(df)
    
    if st.button("نظّف الملف"):
        df = df.dropna(how='all')
        df = df.drop_duplicates()
        
        for col in df.select_dtypes(include=['object']).columns:
            df[col] = df[col].astype(str).str.strip()
            
        st.success("تم تنظيف الملف بنجاح!")
        cleaned_rows = df.shape[0]
        st.subheader("معلومات الملف بعد التنظيف:")
        st.write(f"عدد الصفوف بعد التنظيف: {cleaned_rows}")
        st.write(f"تم حذف {original_rows - cleaned_rows} صفاً.")
        
        with st.expander("معاينة البيانات بعد التنظيف"):
            st.dataframe(df)
            
        csv_data = df.to_csv(index=False).encode('utf-8-sig')
        
        st.download_button(
            label="تحميل الملف النظيف",
            data=csv_data,
            file_name="cleaned_file.csv",
            mime="text/csv"
        )
