import streamlit as st
import pandas as pd
from io import BytesIO

def merge_workbooks(files):
    # Load workbooks
    dfs = [pd.read_excel(file, engine='openpyxl') for file in files]
    
    # Merge dataframes
    merged_df = pd.concat(dfs, ignore_index=True)
    
    return merged_df

def main():
    st.set_page_config(layout='wide')
    st.title("Merge Workbooks")

    # Upload files
    uploaded_files = st.file_uploader("Upload your Excel files", type=["xlsx", "xls","csv"], accept_multiple_files=True)
    
    if uploaded_files:
        st.write(f"Uploaded {len(uploaded_files)} files:")
        # for file in uploaded_files:
        #     st.write(file.name)
        
        # Merge and download
        if st.button("Merge and Download"):
            merged_df = merge_workbooks(uploaded_files)
            
            merge = merged_df.groupby(by=merged_df['SKU'])['Quantity'].sum().reset_index()
            
            # Convert DataFrame to CSV bytes
            csv_buffer = BytesIO()
            merged_df.to_csv(csv_buffer, index=False)
            csv_buffer.seek(0)
            
            st.write('### Merged DataFrame')
            st.write(merged_df)
            st.download_button("Download Merged Data", data=csv_buffer,file_name='Mergedfile.csv',mime='text/csv')

            
if __name__ == "__main__":
    main()
