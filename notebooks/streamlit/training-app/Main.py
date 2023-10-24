import streamlit as st

st.markdown("# Streamlit Hands-On")

st.markdown("You can find a streamlit cheat sheet [here](https://docs.streamlit.io/library/cheatsheet).")

st.markdown("### Exercise 1 - Playground")
st.markdown(
    """
        This exercise is intended to give you a feeling for creating a streamlit app.

        - Use the *1_Playground.py* file in *./pages* for this exercise.
        - A person is described by his/her *first name*, *last name*, *gender*, *date of birth* and *height*. Use useful widgets for each parameter and print out the result.  
        - Move the widgets to the sidebar and show only the result on the main window.
        - Try to store all generated people and show them in a table. 
        - Feel free to pimp your app!

    """
    )

st.markdown("### Exercise 2 - Stromnetz")
st.markdown(
    """
        Let's have a look on some real data. You can find the **Netzentwicklungsplan Strom** in *../data* together with the data of the figures from chapters 2 and 3.
        
        - Use the *2_Stromnetz.py* file in *./pages* for this exercise. 
        - Start with exploring the excel files. It is useful to do this in a notebook.
        - Visualize at least **2** of the data sets inside this streamlit app in different tabs. You can use either plotly or matplotlib (or both).
        - Feel free to pimp your app!

    """
    )