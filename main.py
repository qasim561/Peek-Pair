import streamlit as st
import joblib
from home import show_home
from demand_predict import show_demand_prediction, predict_units_sold
from sales_predict import show_sales_prediction
from help import main as help_main, get_chatbot_response as help_get_chatbot_response



model_2=joblib.load("model_2.sav")


# Streamlit UI setup
st.sidebar.title(' Navigation')


selection = st.sidebar.radio("Go to", ["Home", "Demand Prediction", "Sales Prediction","Help" , "About"])


if selection == "Home":
    st.write("# <u>PEAK-PAIR</u>",unsafe_allow_html=True) #PeakPair
    st.markdown('Double Vision on Sales & Demand')

    # Display the image
    #st.image('No_01.jpg', width=500)
    #, use_column_width=True
    #st.write("""
    # Welcome to PEAK PAIR #
    #Where we analyze how prices affect product sales and how they are affected by prices.
    #Imagine you're a business owner. You have a product and are attempting to forecast how much of it you will sell over the next few months. You realize it's not a simple assignment. What's hot today could not be so tomorrow since prices fluctuate and new products are released. Here is where our tool is useful.
    #It is quite helpful to get this kind of knowledge in advance. It implies that there won't be any waste because enterprises can produce the ideal number of goods. In addition, it aids in budgeting for advertising. After all, why spend a lot of money on advertising if you only have a few pieces that will sell.
    #""")

    col1, col2 = st.columns([6, 4])
    col2.image('no_09.jpg', width=325)
    col1.write("""
    ### Welcome to PEAK-PAIR 
    Where we analyze how prices affect product sales and how they are affected by prices.
    You have a product for attempting to forecast how much of it you will sell over the next few months. You realize it's not a simple assignment. What's hot today could not be so tomorrow since prices fluctuate and new products are released. Here is where our tool is useful.
    It is quite helpful to get this kind of knowledge in advance. It implies that there won't be any waste because enterprises can produce the ideal number of goods. In addition, it aids in budgeting for advertising. After all, why spend a lot of money on advertising if you only have a few pieces that will sell.
    """)
        




elif selection == "Demand Prediction":
    st.write(show_demand_prediction())
    # Taking user input
    total_price = st.number_input("Total Price", value=250.0, format='%f')
    base_price = st.number_input("Base Price", value=200.0, format='%f')
    if st.button("Predict Units Sold"):
        predicted_units = predict_units_sold(model_2, total_price, base_price)
        st.markdown(f" ## Predicted Units Sold: {predicted_units}")

elif selection == "Sales Prediction":
    show_sales_prediction()

elif selection == "Help":
    help_main()
  
    
elif selection == "About":
    st.write("""
    # <u>About this Porject</u> #
    """,unsafe_allow_html=True)
    # Project Description
    st.markdown("#### Product Demand and Sales Forecasting")

    # Objective
    st.markdown("---")
    st.markdown("#### <u>Objective: </u>",unsafe_allow_html=True)
    st.write("Forecast product demand and sales with machine learning, giving special attention to how product pricing influences demand.")

    # Tools & Technologies
    st.markdown("---")
    st.markdown("#### <u>Tools & Technologies:</u>",unsafe_allow_html=True)
    st.write('\n')
    st.write("##### Language:\n- Python")

    st.write("##### Libraries:\n- **Streamlit** for web-based UI/UX\n- **joblib** for model serialization")

    st.write("##### Machine Learning:\n- **Linear regression**\n- **Decision Trees**")

    # Key Features
    st.markdown("---")
    st.markdown("#### <u>Key Features:</u>",unsafe_allow_html=True)
    st.write("- **Demand Prediction**: Given a product's price (both base and total), the model predicts potential units sold.")
    st.write("- **Sales Prediction**: Forecasts sales figures based on advertising spends across various platforms.")

    # Insights
    st.markdown("---")
    st.markdown("#### <u>Insights:</u>", unsafe_allow_html=True)
    st.write("- Product pricing plays a pivotal role in influencing demand. Especially for non-essential products, a surge in price can lead to a significant dip in demand.")
    st.write("- Such predictions are invaluable for businesses. They help in strategic planning, especially in determining manufacturing and advertising budgets. The aim is to cut unnecessary costs while boosting profits.")

    # Interface
    st.markdown("---")
    st.markdown("#### <u>Interface:</u>", unsafe_allow_html=True)
    st.write("- **Home**: A primer on what the app offers.")
    st.write("- **Demand Prediction**: Users input product pricing data to receive demand predictions.")
    st.write("- **Sales Prediction**: Users enter advertising expenditure to get forecasted sales.")
    st.write("- **About**: Delve into the background and gain a deeper understanding of the application.")

    # Outcome
    st.markdown("---")
    st.markdown("#### <u>Outcome:</u>", unsafe_allow_html=True)
    st.write("This tool is designed for businesses aiming for strategic foresight. It offers predictions that ensure businesses stay nimble and ahead in a constantly evolving market.")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    st.write("\n")
    


    st.markdown("---")
    # Define columns
    left_col1, right_col = st.columns([8,2])

    # Add content to the first column (Text Area)
    with left_col1:
        #st.title("Muhammad Qasim")
        st.markdown("# Muhammad Qasim \n ##### (Creator)")
        st.write("""Data analyst and Python programmer with a lot of practical knowledge. My passion of solving issues brought me to the fields of programming and data analytics, where I've developed my abilities and completed a number of projects with success. Using machine learning, developed strong programs, and analyzing difficult data as a Python expert. I can approach any assignment with accuracy and efficiency  with libraries like scikit learn, Seaborn, pandas, and Selenium, to mention a few.!
        """)

        
        st.markdown('### Connect with me:')
    
        
        col1, col2 = st.columns([1, 10])
        col1.image('https://img.icons8.com/color/24/000000/linkedin.png', width=30)
        col2.markdown('[**Linkedin**](https://www.linkedin.com/in/muhammad-qasim-2576071a6/)')
        

        # Create columns for icon and link with adjusted widths
        col1, col2 = st.columns([1, 10])  # Adjust the ratio based on your preference to minimize space        
        # Display the GitHub icon in the first column using st.image
        col1.image('https://img.icons8.com/ios-glyphs/24/ffffff/github.png', width=30)
        # Display the GitHub link in the second column using st.markdown
        col2.markdown('[**GitHub**](https://github.com/qasim561/)')


        col1, col2 = st.columns([1, 10])
        col1.image('kaggle.png', width=30)
        col2.markdown('[**Kaggle**](https://www.kaggle.com/qasim561)')
    
        col1, col2 = st.columns([1, 10])
        col1.image('https://img.icons8.com/ios-glyphs/24/ffffff/new-post.png', width=30)
        #col2.markdown('[**Email**](mailto:qasimkhann561@gmail.com)')
        col2.markdown('qasimkhann561@gmail.com')


        col1, col2 = st.columns([1, 10])
        col1.image('mobile.png', width=30)
        #col2.markdown('[**Phone**](tel:+92-3113147257)')
        col2.markdown('+92-3113147257')
        


    
    
    # Add content to the second column (Image)
    with right_col:
       st.image('No_02.jpg', width=120)

  
