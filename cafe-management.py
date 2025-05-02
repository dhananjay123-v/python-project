import streamlit as st

menu={
    "Pizza":120,
    "Burger":80,
    "maggie":50,
    "Dal-Bhat":30,
    "Coffey":20
}

st.title("Aditya Hotel Management 🍵")
st.subheader("Menu")

# Display item
st.table([{"Item":item,"Price":price} for item,price in menu.items()])

# initilizing session state for order management
if 'order' not in st.session_state:
    st.session_state.order = []
    
# ordering
selected_item=st.selectbox("Select An item to order:",list(menu.keys()))

if st.button("Add to Order"):
    st.session_state.order.append(selected_item)
    st.success(f"{selected_item} Added to Your order !")

# display order
if st.session_state.order:
    st.subheader("🛒 your order")
    order_summery= {item:st.session_state.order.count(item) for item in set(st.session_state.order)}
    total_amount=sum(menu[item]*qty for item,qty in order_summery.items())
    
    st.table([{"Item":item,"Quantity":qty,"Price($)":menu[item]*qty} for item,qty in order_summery.items()])
    st.write(f"### 💰 Total Amount : ${total_amount}")
    
    if st.button("Confirm Order"):
        st.success("✅ Order confirmed! Thank You. Enjoy your meal! 🥣")
        st.session_state.order=[]  # reset after a new order
