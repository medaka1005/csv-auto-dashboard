import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib_fontja

st.set_page_config(layout="wide")

st.title("CSV自動分析ダッシュボード")

uploaded_file = st.file_uploader("CSVをアップロードしてください", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df)

    product_rank = (
        df.groupby("商品名", as_index=False)["売上金額"]
        .sum()
        .sort_values(by="売上金額", ascending=False)
    )

    date_sales = df.groupby("日付", as_index=False)["売上金額"].sum()

    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            "<h2 style='text-align: center'>商品別売上（グラフ）</h2>",
            unsafe_allow_html=True,
        )
        plt.figure()
        plt.bar(product_rank["商品名"], product_rank["売上金額"])
        st.pyplot(plt.gcf())
        plt.close()

    with col2:
        st.markdown(
            "<h2 style='text-align: center'>日別売上推移（グラフ）</h2>",
            unsafe_allow_html=True,
        )
        plt.figure()
        plt.plot(date_sales["日付"], date_sales["売上金額"])
        st.pyplot(plt.gcf())
        plt.close()
