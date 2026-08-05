import streamlit as st

st.title("🛒แอปพลิเคชั่นคำนวณราคาสินค้ารวม VAT 7%")

price = st.number_input("กรอกราคาสินค้า (บาท):", value=0.0)

# คำนวณ VAT 7% และราคารวม
vat = price * 0.07
net_price = price + vat

# แสดงผลการคำนวณ
st.header(f"• ภาษีมูลค่าเพิ่ม (VAT 7%): **{vat:.2f}** บาท")
st.header(f"• ราคารวม VAT: **{net_price:.2f}** บาท")

st.divider()
st.write("นายอัขวิน สิริสุชากุล เลขที่ 18 ม.4/2")
