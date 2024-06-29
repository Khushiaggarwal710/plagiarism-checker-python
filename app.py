import streamlit as st 
import plagiarism

st.title("Plagiarism Checker")

text1 = st.text_input("Text 1")
text2 = st.text_input("Text 2")

submit_button = st.button("Submit")

if submit_button:
    if not text1 or not text2:
        st.warning("Both text fields must be filled out before submitting.")

    else:   
        output = plagiarism.check_plagiarism(text1,text2)

        if(len(output)):
            output = '\n'.join(output)
            output_box = st.text_area("Plag Output:",value = output,height=400)
        else:
            output_box = st.text_area("Plag Output:",value = "No Plagiarism Found")
