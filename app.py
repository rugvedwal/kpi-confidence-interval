import streamlit as st
import math
import matplotlib.pyplot as plt
import numpy as np


# Function to calculate ROAS
def calculate_roas(conversions, product_price, clicks, cpc):
    total_revenue = conversions * product_price
    total_ad_spend = clicks * cpc
    if total_ad_spend == 0:
        return float('inf')  # Avoid division by zero
    roas = total_revenue / total_ad_spend
    return roas


# Function to calculate the confidence interval for ROAS
def calculate_roas_ci(conversions, clicks, product_price, cpc, confidence_level=0.95):
    # Calculate conversion rate
    conversion_rate = conversions / clicks
    success_rate = conversions / clicks

    # Calculate standard error of the conversion rate
    standard_error = math.sqrt((success_rate * (1 - success_rate)) / clicks)

    # Calculate z-score for the given confidence level
    lower_percentile = (1 - confidence_level) / 2 * 100
    upper_percentile = (1 + confidence_level) / 2 * 100
    z_score = np.abs(np.percentile(np.random.standard_normal(10000), [lower_percentile, upper_percentile]))

    # Calculate margin of error for the conversion rate
    margin_of_error = z_score[1] * standard_error

    # Calculate confidence interval for the conversion rate
    lower_bound_conversion_rate = max(0, conversion_rate - margin_of_error)
    upper_bound_conversion_rate = min(1, conversion_rate + margin_of_error)

    # Calculate ROAS bounds
    lower_bound_roas = (lower_bound_conversion_rate * product_price) / cpc
    upper_bound_roas = (upper_bound_conversion_rate * product_price) / cpc

    return (lower_bound_roas, upper_bound_roas)


# Function to plot ROAS with confidence interval
def plot_roas_with_ci(roas, ci_lower, ci_upper):
    fig, ax = plt.subplots(figsize=(8, 1))  # Fixed chart height to 1 inch
    categories = ['ROAS']
    values = [roas]
    errors = [[roas - ci_lower], [ci_upper - roas]]

    ax.barh(categories, values, xerr=errors, capsize=5, color='blue', alpha=0.7)
    ax.set_xlabel('ROAS')
    ax.set_title('ROAS with Confidence Interval')

    return fig


# Streamlit app
def main():
    st.title("ROAS and Confidence Interval Calculator")

    st.write("Input the following details to calculate the ROAS and its confidence interval.")

    # Input fields
    product_price = st.number_input("Product Price", min_value=0.0, value=100.0, step=0.01)
    cpc = st.number_input("Cost Per Click (CPC)", min_value=0.0, value=1.0, step=0.01)
    clicks = st.number_input("Number of Clicks", min_value=0, value=100)
    conversions = st.number_input("Number of Conversions", min_value=0, value=10)
    confidence_level = st.slider("Confidence Interval Percentage", min_value=50, max_value=99, value=95, step=1) / 100

    if st.button("Calculate ROAS"):
        if clicks == 0 or cpc == 0:
            st.error("Number of clicks and CPC must be greater than zero.")
        elif conversions > clicks:
            st.error("Number of conversions cannot exceed the number of clicks.")
        else:
            roas = calculate_roas(conversions, product_price, clicks, cpc)
            ci_lower, ci_upper = calculate_roas_ci(conversions, clicks, product_price, cpc, confidence_level)

            st.write(f"**ROAS:** {roas:.2f}")
            st.write(
                f"**{confidence_level * 100:.0f}% Confidence Interval for ROAS:** [{ci_lower:.2f}, {ci_upper:.2f}]")

            # Plotting the ROAS and CI with fixed height
            fig = plot_roas_with_ci(roas, ci_lower, ci_upper)
            st.pyplot(fig)


if __name__ == "__main__":
    main()
