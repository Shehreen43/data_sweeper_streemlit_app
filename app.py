import streamlit as st
import pandas as pd

# Set the title
st.title("📂 Advanced Data Sweeper")
st.write("Transform your files between CSV and Excel formats with built-in data cleaning and visualization.")

# Upload file
uploaded_file = st.file_uploader("Upload your files (CSV or Excel)", type=["csv", "xlsx"])

if uploaded_file is not None:
    try:
        # Check file type
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file, on_bad_lines="skip")  # Skip bad lines
        else:
            df = pd.read_excel(uploaded_file)

        st.success("✅ File successfully loaded!")

        # Show data preview
        st.subheader("📊 Data Preview")
        st.write(df.head())

        # Show column details
        st.subheader("🔍 Column Information")
        st.write(df.info())

        # Download cleaned data
        st.subheader("📥 Download Cleaned File")
        cleaned_csv = df.to_csv(index=False).encode("utf-8")
        st.download_button("Download CSV", cleaned_csv, "cleaned_data.csv", "text/csv")

    except Exception as e:
        st.error(f"❌ Error loading file: {e}")

