from matplotlib import image
import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
st.title("Palmer's Penguin")
st.text("This project is done by Ishita!")
st.image('penguins_cran.jpg',caption="Palmers Penguins")
st.subheader("What is Palmers penguin dataset?")
st.text('''The Palmer penguins dataset by Allison Horst, Alison Hill, and Kristen Gorman is a dataset for data exploration & visualization, as an alternative to the Iris dataset.

The dataset contains data for 344 penguins. There are 3 different species of penguins in this dataset, collected from 3 islands in the Palmer Archipelago, Antarctica.

Data were collected and made available by Dr. Kristen Gorman and the Palmer Station, Antarctica LTER, a member of the Long Term Ecological Research Network.

Data are available by CC-0 license in accordance with the Palmer Station LTER Data Policy and the LTER Data Access Policy for Type I data.
''')
st.image('penguins.jpg',caption="Species of Palmers penguin")
st.sidebar.header("Select the species you want to know about :")
st.subheader("Click on the side boxes to know more about the species")
if st.sidebar.checkbox("Adelie"):
    st.text('''Adélie penguins: Palmer Station Antarctica LTER and K. Gorman. 2020.
Structural size measurements and isotopic signatures of foraging among adult male and female Adélie penguins
(Pygoscelis adeliae) nesting along the Palmer Archipelago near Palmer Station, 2007-2009 ver 5.
Environmental Data Initiative. 
    ''')
   
if st.sidebar.checkbox('Gentoo'):
    st.text('''Gentoo penguins: Palmer Station Antarctica LTER and K. Gorman. 2020.
Structural size measurements and isotopic signatures of foraging among adult male and female Gentoo penguin (Pygoscelis papua) nesting along the Palmer Archipelago near Palmer Station, 2007-2009 ver 5. 
Environmental Data Initiative. 
    ''')   
if st.sidebar.checkbox("Chinstrap"):
    st.text('''Chinstrap penguins: Palmer Station Antarctica LTER and K. Gorman. 2020.
Structural size measurements and isotopic signatures of foraging among adult male and female Chinstrap penguin (Pygoscelis antarcticus) nesting along the Palmer Archipelago near Palmer Station, 2007-2009 ver 6.
Environmental Data Initiative.
    ''')     
st.text('''
The dataset that is attached with the Penguin file that contains :
different body measurements for three species of penguins from three islands in the Palmer Archipelago, Antarctica
 ''')
st.subheader("Click on the side boxes to know more about the penguins ") 
st.sidebar.header("Want to know more about penguins in depth, Click below :")
if st.sidebar.checkbox("Bill"):

     st.text('''Bill - Emperor Penguins have a hard, pointed bill
(also called the beak) which they use to get food. 
The bill is black with a yellow- orange streak.
''') 
if st.sidebar.checkbox("Flipper"):
    st.text(''' Flipper - Very few birds have true flippers, but all penguin species do.
Their wings are flat, thin, and broad with a long, tapered shape and a blunt, rounded tip.
Because of this severe, streamlined shape, penguins cannot fly, but they are powerful,
agile swimmers and adept underwater hunters
    ''')
if st.sidebar.checkbox("Body mass"):  
    st.text("Body mass - Penguin's body weight ")  
st.sidebar.header("Penguin's body part")    
if st.sidebar.checkbox("Penguin"):    
    st.image('body.jpeg',caption="Penguin's body part")

px=st.selectbox('What do you want the x axis to be?',
                  ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g' ])
piy=st.selectbox('What do you want the y axis to be?',
                   ['bill_length_mm', 'bill_depth_mm', 'flipper_length_mm', 'body_mass_g' ])
pf=st.file_uploader("Kindly select the CSV file attached within")
if pf is not None:
    penguins_df=pd.read_csv(pf)
else:
    st.stop()    
sns.set_style('darkgrid')
markers={"Adelie" : "X", "Gentoo": "s", "Chinstrap": "o"}
fig, ax = plt.subplots() 
ax = sns.scatterplot(data = penguins_df, 
                       x=px,
                       y=piy,
                       hue='species',
                       markers=markers, 
                       style='species')
plt.xlabel(px) 
plt.ylabel(piy) 
plt.title("Scatterplot of Palmer's Penguins") 
st.pyplot(fig) 




#THIS IS MY CODE ~~~ ISHITA BISWAS (BCA 1ST YEAR)