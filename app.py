import streamlit as st

# ---------- Custom CSS ----------
st.markdown("""
    <style>
    body {
        background-color: #f5f7fa;
    }

    .main-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        color: #2c3e50;
    }

    .card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }

    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 8px;
        height: 3em;
        width: 100%;
        font-size: 16px;
    }

    .stTextInput>div>div>input {
        border-radius: 8px;
    }

    .stNumberInput>div>div>input {
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)


# ---------- Customer Class ----------
class Customer:
    def __init__(self, name, account_number, age, mobile_number, balance):
        self.name = name
        self.account_number = account_number
        self.age = age
        self.mobile_number = mobile_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient Balance"
        self.balance -= amount
        return self.balance


# ---------- Session Storage ----------
if "customers" not in st.session_state:
    st.session_state.customers = {}


# ---------- Title ----------
st.markdown('<p class="main-title">🏦 Smart Banking App</p>', unsafe_allow_html=True)


# ---------- Sidebar ----------
menu = ["Create Account", "View Account", "Deposit", "Withdraw"]
choice = st.sidebar.radio("📌 Navigation", menu)


# ---------- Create Account ----------
if choice == "Create Account":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("✨ Create New Account")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        age = st.number_input("Age", min_value=1)

    with col2:
        account_number = st.text_input("Account Number")
        mobile_number = st.text_input("Mobile Number")

    balance = st.number_input("Initial Balance", min_value=0.0)

    if st.button("Create Account"):
        if account_number in st.session_state.customers:
            st.error("⚠️ Account already exists!")
        else:
            customer = Customer(name, account_number, age, mobile_number, balance)
            st.session_state.customers[account_number] = customer
            st.success("✅ Account Created Successfully!")

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- View Account ----------
elif choice == "View Account":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("🔍 View Account Details")

    acc_no = st.text_input("Enter Account Number")

    if st.button("Search"):
        customer = st.session_state.customers.get(acc_no)

        if customer:
            st.markdown(f"""
                **👤 Name:** {customer.name}  
                **🎂 Age:** {customer.age}  
                **📱 Mobile:** {customer.mobile_number}  
                **💰 Balance:** ₹{customer.balance}
            """)
        else:
            st.error("❌ Account not found")

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- Deposit ----------
elif choice == "Deposit":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💵 Deposit Money")

    acc_no = st.text_input("Account Number")
    amount = st.number_input("Amount", min_value=0.0)

    if st.button("Deposit"):
        customer = st.session_state.customers.get(acc_no)

        if customer:
            new_balance = customer.deposit(amount)
            st.success(f"✅ Deposited! New Balance: ₹{new_balance}")
        else:
            st.error("❌ Account not found")

    st.markdown('</div>', unsafe_allow_html=True)


# ---------- Withdraw ----------
elif choice == "Withdraw":
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("💸 Withdraw Money")

    acc_no = st.text_input("Account Number")
    amount = st.number_input("Amount", min_value=0.0)

    if st.button("Withdraw"):
        customer = st.session_state.customers.get(acc_no)

        if customer:
            result = customer.withdraw(amount)
            if result == "Insufficient Balance":
                st.error("⚠️ Insufficient Balance")
            else:
                st.success(f"✅ Withdraw Successful! Balance: ₹{result}")
        else:
            st.error("❌ Account not found")

    st.markdown('</div>', unsafe_allow_html=True)