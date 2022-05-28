# Standard Python Module

from fileinput import filename
from io import StringIO, BytesIO

# EDA packages

import pandas as pd
import numpy as np
from pandas_profiling import ProfileReport

# Impoerting the Dependencies

from matplotlib.pyplot import title
import matplotlib.pyplot as plt

# core package

import streamlit as st
import plotly.express as px

# comonents packages

import streamlit.components.v1 as components
from streamlit_option_menu import option_menu
from streamlit_pandas_profiling import st_profile_report
from io import StringIO, BytesIO 
import seaborn as sns 
from PIL import Image

plt.style.use("ggplot")

# set page congiguration
st.set_page_config(page_title='Data Analysis of Automative Industry',page_icon=":new_moon_width_face:")

# using for ignoring warning of bar_chart 
st.set_option('deprecation.showPyplotGlobalUse', False)
showPyplotGlobalUse = False

# make the menu bar(given some option) Horizontal
selected = option_menu(
		menu_title=None,
		options=["HOME","CAR_Segment","Generate_report","Reviews"],
		icons=["house","ant-design:car-filled","book","book"],
		menu_icon="cast",
		orientation="horizontal",
		# set colors style text-size background and padding of the menu bar
		styles={
			"container":{"padding":"6","background-color": "#fafafa"},
			"icon": {"color":"orange","font-size":"13px"},
            "nav-link": {"font-size":"13px","text-align":"center","margin":"15px","--hover-color":"#eee"},
			"nav-link-selected":{"background-color":"red"},
		})

# import multiple xlsx datasheet for making a website

# used car dat sheet ater cleaning
clean_car_file='dataweb\cleaningfiless.xlsx' 
clean_car=pd.read_excel(clean_car_file,
				  usecols='E:V') # using only E to V column of above excel sheet
clean_car2=pd.read_excel(clean_car_file,
				  usecols='A:B') # unsing only A to B Column of above exccel sheet

# used car datasheet without cleaning 
car_file='dataweb\cars_ds_final.xlsx' 
car=pd.read_excel(car_file,
				  usecols='N') # using only N column of above excel sheet

# used sales_company wise datasheet 
sal_comp_file='dataweb\sales-companywise.xlsx'
sal_comp=pd.read_excel(sal_comp_file,
				  usecols='B:F') # using only B to F column of above excel sheet

# used sales_state wise datasheet 
sel_state_file='dataweb\sale-Statewise.xlsx'
sal_sate=pd.read_excel(sel_state_file,
				  usecols='B:D') # using only B to D column of above excel sheet


# check choose option and set the page 
if selected=="HOME":
    
	# set home and using HTML for effective page 
	html_temp = """
		<div style="background-color:skyblue;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;">DATA ANALYSIS AND VISUALIZATION</h1>
		</div>
		"""
	components.html(html_temp)

 # in home page  set selcectbox  of side and give some option 
	st.sidebar.title('Using All Datasets')
	col=st.sidebar.selectbox("Select a Excel File",['Cleaning','Sales(Sate-wise)','Sales(company-wise)'])
    
# check what are you select and set the home page according this 

	if col=='Cleaning':
		st.subheader("Showing All Data")
		st.dataframe(clean_car) # showing data of cleaning file 


	if col=='Sales(Sate-wise)':
		st.subheader("Showing All Data")
		st.dataframe(sal_sate)  # showing data of cleaning file

	if col=='Sales(company-wise)':
		st.subheader("Showing All Data")
		st.dataframe(sal_comp)  # showing data of cleaning file

# title in side bar of home page 
	st.sidebar.title('Top Analysis')
	  # make checkbox to select any one ya multiple

# first checkbox
	if st.sidebar.checkbox("Top 5 cars"):
		plt.figure(figsize=(8,5))
		st.subheader('TOP 5 CARS LIST')
		# showing top 5 list
		st.write(clean_car2['Make'].value_counts()[0:5])
		st.subheader('BAR_CHART TOP 5 CARS LIST')
		# showing chart
		st.write(plt.bar(list(clean_car2['Make'].value_counts()[0:5].keys()),list(clean_car2['Make'].value_counts()[0:5]),color="b"))
		st.pyplot()

# second checknox
	if st.sidebar.checkbox("TOP 10 CARS"):
		plt.figure(figsize=(8,5))
		st.subheader('TOP 10 CARS LIST')
		# showing list of top 10 car
		st.write(clean_car2['Make'].value_counts()[0:10])
		st.subheader('BAR_CHART TOP 10 CARS LIST')
		# showing chart
		st.write(plt.bar(list(clean_car2['Make'].value_counts()[0:10].keys()),list(clean_car2['Make'].value_counts()[0:10]),color="r"))
		st.pyplot()

# Third checkbox
	if st.sidebar.checkbox("Top Car making companies"):
		clean_car2.dropna(inplace=True)
		st.header('Analyzing by Pie chart of CAR BRAND')
		pie_chart=px.pie(clean_car2,
			 	 values='no.',
				  title='Top Car making companies',
			  	names='Make')
		st.plotly_chart(pie_chart) # pie char code

# fourth checkbox
	if st.sidebar.checkbox('MOSTLY USED FUEL TYPE'):
		st.subheader('MOSTLY USED FUEL TYPE LIST')
		st.write(car['Fuel_Type'].value_counts())
		plt.figure(figsize=(8,5))
		st.subheader('MOSTLY USED FUEL TYPE ANALYZING BY BAR-CHART')
		# bar chart
		st.write(plt.bar(list(car['Fuel_Type'].value_counts().keys()),list(car['Fuel_Type'].value_counts()),color="orange"))
		st.pyplot()

# make a hadding in side bar of home page
	st.sidebar.title('SALES Analysis')
	st.sidebar.subheader("YEAR (2021-22) ANALYSIS")

#first checkbox
	if st.sidebar.checkbox('ap21'):
		sns.barplot(x=sal_comp['OEM'],y=sal_comp['ap21'],estimator=np.median) # bar ploat code
		plt.xticks(rotation='vertical')
		st.pyplot()

# second Checkbox
	if st.sidebar.checkbox('ap22'):
		sns.barplot(x=sal_comp['OEM'],y=sal_comp['ap22'],estimator=np.median)
		plt.xticks(rotation='vertical')
		st.pyplot()
	
	st.sidebar.subheader("ANALAZING MODEL WISE SELLING")
    # checkbox
	if st.sidebar.checkbox("ANALYSIS of CATEGORIES of CAR "):
		plt.figure(figsize=(16,7))
		sns.countplot(data=sal_comp, y='Bodystyle',alpha=.6,color='blue')
		plt.title('Cars by car body type',fontsize=30)
		plt.xticks(fontsize=14)
		plt.yticks(fontsize=14)
		plt.xlabel('')
		plt.ylabel('')
		st.pyplot()

	st.sidebar.subheader('STATE_WISE SALES ANALYSIS')

	if st.sidebar.checkbox("YEAR (2021-22) ANALYSIS"):
		sns.barplot(x=sal_sate['State_name'],y=sal_sate['Rank1'],estimator=np.median)
		plt.xticks(rotation='vertical')
		st.pyplot()

	if st.sidebar.checkbox("YEAR (2021-22) ANALYSIS (%-wise)"):
		sns.barplot(x=sal_sate['State_name'],y=sal_sate['Rank2'],estimator=np.median)
		plt.xticks(rotation='vertical')
		st.pyplot()



	st.set_option('deprecation.showPyplotGlobalUse', False)
	showPyplotGlobalUse = False


	st.sidebar.title("Data Visualization")
# checkbox
	if st.sidebar.checkbox("Between Ex-Showroom price and Comapny"):
		st.subheader("DATA visualization BY BAR-PLOT BETWEEN Ex-Showroom_Price && COMPANY")
		st.write(sns.barplot(x=clean_car2['Make'],y=clean_car['Ex-Showroom_Price'])) # bar ploat 
		plt.xticks(rotation='vertical')
		st.pyplot()

	if st.sidebar.checkbox("Between Ex-Showroom price and Petrol"):
		st.subheader("DATA visualization BY BARPLOT BETWEEN Ex-Showroom_Price && PETROL")
		st.write(sns.barplot(x=clean_car['Petrol'],y=clean_car['Ex-Showroom_Price']))
		plt.xticks(rotation='horizontal')
		st.pyplot()
    
	st.sidebar.title("Visualization All Features")
	if st.sidebar.checkbox("Correlation Plot"):
		f,ax = plt.subplots(figsize=(14,10))
		st.sidebar.subheader("VISUALIZATION of ALL FEATURES")
		st.write(sns.heatmap(clean_car.corr(), annot=True, fmt=".001f",ax=ax))
		st.pyplot()


# code of car segement menu bar

if selected=="CAR_Segment":
	st.subheader("CAR SEGMENT ANALYSIS")
	nf=pd.read_csv('dataweb\carsegment.csv')
	st.dataframe(nf)
#view image code
	image = Image.open("images\carhatchbags.webp")
	st.image(image, caption='DIFFERENT SEGMENT')
	image = Image.open("images\second.webp")
	st.image(image, caption='HATCHBACK SENERIO IN INDIA') # for image caption down the image


# code of genarate report

if selected=="Generate_report":
	st.subheader("Automated EDA with Pandas Profile")
	data_file = st.file_uploader("Upload CSV",type=['csv']) # code of file upload option
	if data_file is not None:
		df = pd.read_csv(data_file)
		st.dataframe(df.head())  # showing all data of selected datsheet(csv)
		profile = ProfileReport(df)
		st_profile_report(profile) # genarete report of data sheet(csv)



# code of Review 
if selected=="Reviews":
		st.subheader("Review Analysis")
		#file read using pandas datarame
		review_file='dataweb\Reviews.xlsx' 
		compair_file='dataweb\Allfeatures.xlsx'
		af=pd.read_excel(compair_file,
				usecols='A:I',
				skiprows=1	)
		if st.checkbox("Check All Features of Hyundai Elantra "):
			sns.barplot(x=af['Terms'],y=af['Freq'],estimator=np.median)
			plt.xticks(rotation='vertical')
			st.pyplot()

		if st.checkbox("Check All Features of Honda Civic "):
			sns.barplot(x=af['Terms2'],y=af['Freq2'],estimator=np.median)
			plt.xticks(rotation='vertical')
			st.pyplot()

		if st.checkbox("Check All Features of Ford Focus "):
			sns.barplot(x=af['Terms3'],y=af['Freq3'],estimator=np.median)
			plt.xticks(rotation='vertical')
			st.pyplot()




		st.subheader("CHOOSE AN OPTION")
		# make radio boton
		select_option = st.radio(
     	"",
     	('Performance BEST/WORST features of each Group', 'Comfort BEST/WORST features of each Group', 'Value BEST/WORST features of each Group','Technology BEST/WORST features of each Group',))

		if select_option == 'Performance BEST/WORST features of each Group':
			md=pd.read_excel(review_file,
				  usecols='A:I'
				  )
			md=md.fillna('')
			st.subheader("Performance BEST/WORST features of each Group")
			st.dataframe(md)
			image = Image.open("images\image2.jpeg")
			st.image(image, caption='Performance BEST/WORST features of each Group')



		elif select_option == 'Comfort BEST/WORST features of each Group':
			nd=pd.read_excel(review_file,
				  usecols='L:S'
				  )
			nd=nd.fillna('')
			st.subheader("Comfort BEST/WORST features of each Group")

			st.dataframe(nd)
			
			
		


		elif select_option == 'Value BEST/WORST features of each Group':
			rd=pd.read_excel(review_file,
				  usecols='W:AC'
				  )
			rd=rd.fillna('')
			st.subheader("Value BEST/WORST features of each Group")

			st.dataframe(rd)
			
			image = Image.open("images\image1.jpeg")
			st.image(image, caption='Value BEST/WORST features of each Group')
		
	
		
		elif select_option == 'Technology BEST/WORST features of each Group':
			sd=pd.read_excel(review_file,
				  usecols='AH:AP'
				  )
			sd=sd.fillna('')
			st.subheader("Technology BEST/WORST features of each Group")
			st.dataframe(sd)
			image = Image.open("images\image3.jpeg")
			st.image(image, caption='')






hide_menu_style="""
<style>
       #MainMenu{visibility:hidden;}
	   footer{visibility:hidden;}
</style> 
	   """
st.markdown(hide_menu_style,unsafe_allow_html=True)

