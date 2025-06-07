import streamlit as st

# ── Business-logic layer ──────────────────────────────────────────────────────
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self._balance = initial_balance
        self.__pin = "5678"                       # private
        st.toast(f"Account created for {self.owner}")

    # public actions
    def deposit(self, amt: float) -> None:
        if amt > 0:
            self._balance += amt
            st.success(f"Deposited ${amt:.2f}.  New balance: ${self._balance:.2f}")
        else:
            st.error("Deposit amount must be positive.")

    def withdraw(self, amt: float) -> None:
        if amt <= 0:
            st.error("Withdrawal amount must be positive.")
        elif amt > self._balance:
            st.error(f"Insufficient funds (balance ${self._balance:.2f}).")
        else:
            self._balance -= amt
            st.success(f"Withdrew ${amt:.2f}.  New balance: ${self._balance:.2f}")

    # controlled (encapsulated) getters
    def get_balance(self) -> float:
        st.info(f"Current balance: ${self._balance:.2f}")
        return self._balance

    def get_pin(self) -> str:
        st.warning("⚠️ Accessing a private value for demo purposes.")
        st.write(f"Private pin (via name-mangling): `{self._BankAccount__pin}`")
        return self.__pin

# ── Session helpers ───────────────────────────────────────────────────────────
def account() -> BankAccount | None:
    """Return the BankAccount stored in session_state (if any)."""
    return st.session_state.get("acct")

def create_account():
    with st.form("create_acct", clear_on_submit=True):
        owner   = st.text_input("Owner's name", placeholder="Minendra")
        initial = st.number_input("Initial balance ($)", min_value=0.0, value=0.0,
                                  step=100.0, format="%.2f")
        submitted = st.form_submit_button("Create account")
        if submitted:
            st.session_state.acct = BankAccount(owner, initial)

# ── UI ────────────────────────────────────────────────────────────────────────
st.title("🏦 Simple BankAccount Demo (Encapsulation)")

if account() is None:
    st.write("### Create an account to begin:")
    create_account()
    st.stop()

acct = account()
st.write(f"**Welcome, {acct.owner}!**")

# Deposit / Withdraw layout
col1, col2 = st.columns(2, gap="large")
with col1:
    st.subheader("Deposit")
    amt = st.number_input("Amount to deposit ($)", min_value=0.0, value=0.0,
                          step=50.0, format="%.2f", key="dep")
    if st.button("Deposit", key="dep_btn"):
        acct.deposit(amt)

with col2:
    st.subheader("Withdraw")
    amt_w = st.number_input("Amount to withdraw ($)", min_value=0.0, value=0.0,
                            step=50.0, format="%.2f", key="wd")
    if st.button("Withdraw", key="wd_btn"):
        acct.withdraw(amt_w)

# Balance & pin actions
st.divider()
c1, c2 = st.columns(2)
if c1.button("Show balance"):
    acct.get_balance()

if c2.button("Reveal (private) pin"):
    acct.get_pin()

# Direct (discouraged) attribute access to illustrate encapsulation limits
with st.expander("🔎 Peek behind the curtain (not recommended)"):
    st.code(
        f"Direct _balance  : {acct._balance}\n"
        f"Direct __pin (mangled) : {acct._BankAccount__pin}",
        language="python",
    )
