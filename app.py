import streamlit as st
import pandas as pd

import config

df = pd.read_csv(config.table_name, index_col=0)

edited_df = st.data_editor(df, num_rows="dynamic")

m,n = st.slider("Choose Money Location", min_value=0, max_value=len(edited_df.T.columns), value=(0,len(edited_df.T.columns)), step=1)
st.bar_chart(edited_df.T,y=edited_df.T.columns[m:n])