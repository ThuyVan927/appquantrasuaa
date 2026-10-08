import streamlit as st

# =========================
# CẤU HÌNH TRANG
# =========================
st.set_page_config(
    page_title="Milk Tea Shop",
    page_icon="🧋",
    layout="wide"
)

# =========================
# CSS
# =========================
st.markdown("""
<style>
    .main {
        background-color: #fff8f5;
    }

    .title {
        text-align: center;
        color: #8B4513;
        font-size: 45px;
        font-weight: bold;
    }

    .subtitle {
        text-align: center;
        color: #a0522d;
        font-size: 20px;
        margin-bottom: 30px;
    }

    .product {
        background-color: white;
        padding: 15px;
        border-radius: 15px;
        box-shadow: 0 3px 10px rgba(0,0,0,0.1);
        margin-bottom: 15px;
    }

    .price {
        color: #d2691e;
        font-size: 20px;
        font-weight: bold;
    }

    .total {
        background-color: #ffe4d6;
        padding: 20px;
        border-radius: 15px;
        font-size: 25px;
        font-weight: bold;
        color: #8B4513;
    }
</style>
""", unsafe_allow_html=True)

# =========================
# DỮ LIỆU SẢN PHẨM
# =========================
products = {
    "Trà sữa truyền thống": 30000,
    "Trà sữa matcha": 35000,
    "Trà sữa socola": 35000,
    "Trà sữa dâu": 35000,
    "Trà sữa khoai môn": 38000,
    "Trà đào": 30000,
    "Trà vải": 30000,
    "Trà chanh": 25000
}

toppings = {
    "Trân châu đen": 5000,
    "Trân châu trắng": 5000,
    "Thạch trái cây": 5000,
    "Pudding trứng": 7000,
    "Kem cheese": 10000,
    "Thạch dừa": 5000
}

# =========================
# TIÊU ĐỀ
# =========================
st.markdown(
    '<div class="title">🧋 MILK TEA SHOP 🧋</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Ngọt ngào trong từng ly trà sữa 💕</div>',
    unsafe_allow_html=True
)

# =========================
# THÔNG TIN KHÁCH HÀNG
# =========================
st.sidebar.header("👤 Thông tin khách hàng")

customer_name = st.sidebar.text_input("Họ và tên")
phone = st.sidebar.text_input("Số điện thoại")

st.sidebar.markdown("---")

# =========================
# CHỌN SẢN PHẨM
# =========================
st.header("🧋 Chọn trà sữa")

product_name = st.selectbox(
    "Chọn món",
    list(products.keys())
)

price = products[product_name]

size = st.radio(
    "Chọn size",
    ["M", "L"],
    horizontal=True
)

if size == "L":
    size_price = 5000
else:
    size_price = 0

sugar = st.select_slider(
    "🍬 Mức đường",
    options=["0%", "30%", "50%", "70%", "100%"],
    value="50%"
)

ice = st.select_slider(
    "🧊 Mức đá",
    options=["0%", "30%", "50%", "70%", "100%"],
    value="50%"
)

# =========================
# TOPPING
# =========================
st.subheader("🍓 Chọn topping")

selected_toppings = st.multiselect(
    "Bạn muốn thêm gì?",
    list(toppings.keys())
)

topping_price = sum(
    toppings[item] for item in selected_toppings
)

# =========================
# SỐ LƯỢNG
# =========================
quantity = st.number_input(
    "🔢 Số lượng",
    min_value=1,
    max_value=20,
    value=1
)

# =========================
# TÍNH TIỀN
# =========================
one_drink_price = price + size_price + topping_price
total = one_drink_price * quantity

st.markdown("---")

st.subheader("🧾 Thông tin đơn hàng")

col1, col2 = st.columns(2)

with col1:
    st.write("**Món:**", product_name)
    st.write("**Size:**", size)
    st.write("**Đường:**", sugar)
    st.write("**Đá:**", ice)

with col2:
    if selected_toppings:
        st.write("**Topping:**", ", ".join(selected_toppings))
    else:
        st.write("**Topping:** Không có")

    st.write("**Số lượng:**", quantity)

st.markdown(
    f'<div class="total">💰 Tổng tiền: {total:,} VNĐ</div>',
    unsafe_allow_html=True
)

# =========================
# ĐẶT HÀNG
# =========================
st.markdown("---")

if st.button("🛒 ĐẶT HÀNG", use_container_width=True):

    if customer_name == "":
        st.warning("⚠️ Vui lòng nhập họ và tên!")

    elif phone == "":
        st.warning("⚠️ Vui lòng nhập số điện thoại!")

    else:
        st.success("🎉 Đặt hàng thành công!")

        st.balloons()

        st.write("### 🧾 HÓA ĐƠN")

        st.write("👤 **Khách hàng:**", customer_name)
        st.write("📞 **Số điện thoại:**", phone)
        st.write("🧋 **Món:**", product_name)
        st.write("📏 **Size:**", size)
        st.write("🍬 **Đường:**", sugar)
        st.write("🧊 **Đá:**", ice)
        st.write("🍓 **Topping:**",
                 ", ".join(selected_toppings)
                 if selected_toppings else "Không có")
        st.write("🔢 **Số lượng:**", quantity)

        st.markdown(
            f"### 💰 Thành tiền: **{total:,} VNĐ**"
        )

        st.info("Cảm ơn bạn đã mua hàng! 🧋💕")
