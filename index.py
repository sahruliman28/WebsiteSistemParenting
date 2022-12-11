from st_on_hover_tabs import on_hover_tabs
import streamlit as st 
import pandas as pd
# from google.colab import files
# from capstone_project import *
st.set_page_config(layout="wide")

df = pd.read_csv("datasets.csv", encoding='utf-8', index_col=None)

st.header("Momimo")
st.markdown('<style>' + open('./style.css').read() + '</style>', unsafe_allow_html=True)


with st.sidebar:
    tabs = on_hover_tabs(tabName=['Dashboard', 'Article', 'Product'], 
                         iconName=['dashboard', 'article', 'money'], default_choice=0)

if tabs == 'Dashboard':
    st.title("Capstone Project Team  - Aplikasi Rekomendasi Produk Anak :sparkles:")
    st.write(
    """
    ##### **Aplikasi rekomendasi produk anak merupakan sebuah implementasi dari projek Machine Learning yang dapat merekomendasikan pemilihan produk sesuai dengan usia anak. Anda dapat memasukkan usia dan manfaat yang dibutuhkan anak untuk mengetahui rekomendasi produk yang Anda butuhkan**
    """)

elif tabs == 'Article':
    st.title("Article For Parent")

elif tabs == 'Product':
    st.title("Search Product and Benefit a Product")

    st.write('---')

tk = 0
st.title('Programming Product Recommendation System')

col1, col2 = st.columns(2)
    #taking book name as input
with col1:
    item = st.text_input('Enter your product search : ')
    
#taking multiple fiels to get similarity
with col2:
    feat = st.selectbox("Select Mode : ",['usia', 'product_name', 'manfaat'])
    if st.button('Search'):
        tk = 1

#st.dataframe(df.head(10))
if tk == 1:
    st.success('Recommending Product similar to '+item)
    rec = st.empty()
    rec = st.dataframe(df_recommendations(item, 'product_name', df, feat), width=700, height=76)

# print(df_recommendations())
