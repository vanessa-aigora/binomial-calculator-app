import streamlit as st
from scipy import stats

st.title("Binomial Test Calculator")

num_correct = st.number_input("Number Correct:", min_value=0, max_value=100, step=1, value=15)
num_total = st.number_input("Total Trials:", min_value=1, max_value=100, step=1, value=20)
p_guess = st.number_input("Hypothesized Probability (0.0-1.0):", min_value=0.0, max_value=1.0, step=0.01, value=0.5, format="%.2f")

if st.button("Calculate P-value"):
    if num_correct > num_total:
        st.error("Number Correct cannot be greater than Total Trials.")
    elif not (0 <= p_guess <= 1):
        st.error("Hypothesized Probability must be between 0 and 1.")
    else:
        p_value = stats.binomtest(num_correct, num_total, p_guess, alternative='two-sided').pvalue
        st.write(f"The p-value is: {p_value:.4f}")
