import streamlit as st

# Set page configuration
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="🔮",
    layout="wide"
)

# Add CSS for animations
st.write("""
    <style>
        @keyframes zoom-in {
            0% {
                transform: scale(0);
            }
            100% {
                transform: scale(1);
            }
        }
        @keyframes slide-in-right {
            0% {
                transform: translateX(100%);
            }
            100% {
                transform: translateX(0);
            }
        }
        @keyframes slide-in-left {
            0% {
                transform: translateX(-100%);
            }
            100% {
                transform: translateX(0);
            }
        }
        @keyframes slide-in-bottom {
            0% {
                transform: translateY(100%);
            }
            100% {
                transform: translateY(0);
            }
        }
        @keyframes slide-in-top {
            0% {
                transform: translateY(-100%);
            }
            100% {
                transform: translateY(0);
            }
        }
        .zoom-in-animation {
            animation: zoom-in 1.5s ease-in-out;
        }
        .slide-in-right-animation {
            animation: slide-in-right 1.5s ease-in-out;
        }
        .slide-in-left-animation {
            animation: slide-in-left 1.5s ease-in-out;
        }
        .slide-in-bottom-animation {
            animation: slide-in-bottom 1.5s ease-in-out;
        }
        .slide-in-top-animation {
            animation: slide-in-top 1.5s ease-in-out;
        }
    </style>
""", unsafe_allow_html=True)

# Header with zoom-in animation
st.markdown('<div class="slide-in-top-animation"><h1>🚀 Welcome to Customer Churn Prediction App!</h1></div>', unsafe_allow_html=True)

# Content with different slide-in animations
st.write('<div class="slide-in-bottom-animation"><h3>Unleash the power of machine learning to predict customer churn!</h3></div>', unsafe_allow_html=True)

# About This App with slide-in-left animation
# st.markdown('<div class="slide-in-right-animation">', unsafe_allow_html=True)
st.markdown('<div class="slide-in-left-animation"><h4>About This App</h4></div>', unsafe_allow_html=True)
st.markdown("""
    The Customer Churn Prediction App is designed to help businesses in the telecommunications industry predict whether a customer is likely to churn (leave the service). By leveraging machine learning techniques, this app provides valuable insights into customer behavior, allowing companies to take proactive measures to improve customer retention.
    """)
st.markdown('</div>', unsafe_allow_html=True)

# Create columns for Key Features, How It Works, and Benefits
col1, col2, col3 = st.columns(3)

# Key Features with slide-in-right animation
with col1:
    st.markdown('<div class="  ">', unsafe_allow_html=True)
    st.markdown("## Key Features")
    st.markdown("""
    - **Model Training:** Train various machine learning models, such as Logistic Regression, Random Forest, and XGBoost, to predict customer churn.
    - **Feature Importance:** Analyze feature importances to understand the drivers of customer churn.
    - **User-Friendly Interface:** Interact with the app through an intuitive and engaging user interface.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# How It Works with slide-in-bottom animation
with col2:
    st.markdown('<div class="slide-in-bottom-animation">', unsafe_allow_html=True)
    st.markdown("## How It Works")
    st.markdown("""
    1. **Data Collection:** Gather customer data from various sources.
    2. **Data Preprocessing:** Clean and preprocess the data for model training.
    3. **Model Training:** Train multiple machine learning models to predict churn.
    4. **Model Evaluation:** Evaluate model performance using various metrics.
    5. **Deployment:** Deploy the best-performing model to make real-time predictions.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Benefits with slide-in-top animation
with col3:
    st.markdown('<div class="slide-in-top-animation">', unsafe_allow_html=True)
    st.markdown("## Benefits")
    st.markdown("""
    - **Improve Customer Retention:** Identify at-risk customers and take proactive measures to retain them.
    - **Optimize Marketing Strategies:** Tailor marketing efforts to target customers who are likely to churn.
    - **Enhance Business Performance:** Reduce churn rates and increase customer lifetime value.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("""
    ---
    © 2024 Customer Churn Prediction Project. All rights reserved.
""")
