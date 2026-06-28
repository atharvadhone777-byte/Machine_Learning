import streamlit as st
import pandas as pd
import requests
#To run - streamlit run Streamlit.py

#--------------TEXT-------------------
st.title("Title")
st.subheader("Subheader")
st.text("Text")
st.success("Text with green Background") 
st.button("Button")

#--------------FORMS------------------
#1.selectbox
a = st.selectbox("Select Option DropDown: ",["Options A","Option B","Option C","Option D"])
st.write(f"You choose {a}") #Write will also print like text

#2.Button
#To do task only after button is clicked use if-else
if st.button("Generate"):
    st.success("Generated after button click")

#3.Checkbox
b = st.checkbox("Add Checkbox")
#To do a work only checkbox is checked
if b:
    st.success("Checkbox is checked")

#4.Radio buttons
Radio_option = st.radio("Radio option picker",["Option 1","Option 2"])

#5.Slider like brightness slider
Slider_value = st.slider("Slider levels",0,10,5)
# 0 - min, 10 - max, 5 - default choosen value


#----------------INPUTS------------------
Num_inp = st.number_input("Enter a number",min_value=1,max_value=10,step=1) #Max,min values are already set,step is increament & decreament by how much from icons + -
name = st.text_input("Enter yout name")
dob = st.date_input("Select date of birth")

#---------------Layout-----------
#1. Colums - Voting system
col1,col2 = st.columns(2)
with col1:
    st.image("downloadBJP.png")
    vote1 = st.button("Vote BJP")
with col2:
    st.image("downloadSSena.png")
    vote2 = st.button("Vote Shivsena")

if vote1:
    st.success("Votes for BJP")
elif vote2:
    st.success("Votes for Shivsena")

#2. Sidebar 
st.sidebar.title("SIdebar's Title")
#All things done in main page can be done in sidebar

#3. Expander
with st.expander("Instructions Dropdown"):
    st.write("""
    1. Instruction 1
    2. Instruction 2
    3. Instruction 3
""")

#4. Markdown
st.markdown('### Welcome to Chai App') #Title 
st.markdown('> Blockquote')            #Blackquote

#----------------File Manipulation---------------
my_file = st.file_uploader("Upload file",type=["csv"])
if my_file:
    df = pd.read_csv(my_file)
    st.dataframe(df)
    #Now a special code which will give rows containing specific value
    city = df['City'].unique()
    selected_city = st.selectbox("All cities: ",city)
    filtered_data = df[df["City"] == selected_city]
    st.dataframe(filtered_data)


#--------------Request API----------------------
# Currency Converter
st.title("Currency Converter")
amount = st.number_input("Eneter Amount in INR",min_value=1)

target_currency = st.selectbox("Convert to:", ["USD","EUR","GBP","JPY"])

if st.button("Convert"):
    url = "https://api.exchangerate-api.com/v4/latest/INR"
    response = requests.get(url)

    if response.status_code==200:
        data = response.json()
        rate = data["rates"][target_currency] #Rates column mein jaker target currency wala row select karo and uska value store karo
        converted = rate*amount
        st.success(f"{amount} INR = {converted} {target_currency}")
    else:
        st.error("Failed to fetch")


