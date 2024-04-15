import streamlit as st
import pandas as pd

st.set_page_config(layout='wide')

st.title('Customize the Data')

st.write('### Upload files')
file = st.file_uploader('Upload your file')

def distinctcount(x):
    return x.nunique()

# Check if files are uploaded
if file:
    # Read the first file to get the column names
    first_file = pd.read_excel(file)
    column_names = first_file.columns.tolist()
    
    # Display the list of column names in a list format
    column_list = ', '.join(column_names)
    st.write(f'Available column Names: {column_list}')
    
    st.write('### Select data for Customize table:')

    # Dropdown for selecting columns to group by
    group_by_columns = st.multiselect('Select columns to group by:', column_names)

    # Dropdown for selecting columns to aggregate
    agg_columns = st.multiselect('Select columns to aggregate:', column_names)

    # Define aggregation dictionary
    agg_dict = {}

    for col in agg_columns:
        selected_funcs = st.multiselect(f'Select aggregation functions for {col}:', ['sum', 'count','distinctcount', 'mean', 'median','max', 'min'])
        # Convert 'distinctcount' to custom function
        if 'distinctcount' in selected_funcs:
            selected_funcs.remove('distinctcount')
            selected_funcs.append(distinctcount)
        agg_dict[col] = selected_funcs
        
    if st.button('Build a table'):
        
        
                
        # Apply aggregation based on user selection
        result = pd.concat([pd.read_excel(file) for file in files]).groupby(group_by_columns).agg(agg_dict).reset_index()
        
        
        st.write(result)
                
    
