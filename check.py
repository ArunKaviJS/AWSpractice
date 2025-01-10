import streamlit as st
import pymysql
import pandas as pd

st.title(':red[MY WEBPAGE]')
st.header(':red[My name is AK]')

aws=pymysql.connect(
    host='arunkavidb.c3qi80c6gqw9.ap-south-1.rds.amazonaws.com',
    user='admin',
    password='arun53787',
    port=3306,
    database='awssql'
)
arun=aws.cursor()

arun.execute('use awssql')
arun.execute('''
    select sex , sum(total_bill) as total_bill from tips
group by sex ; 
''')
st.dataframe(arun)

