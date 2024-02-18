import streamlit as st
import pickle
import pandas as pd

pipe = pickle.load(open('pipe.pkl','rb'))

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah','Mohali', 'Bengaluru']

st.title("IPL Win Predictor")

col1,col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("Select the batting team",sorted(teams))

with col2:
    bowling_team = st.selectbox("Select the bowling team",sorted(teams))
# select host city
selected_city = st.selectbox("Select Host city",sorted(cities))
# target
target = st.number_input("Target")

col3,col4,col5 = st.columns(3)

with col3:
    score = st.number_input("Score")
with col4:
    overs = st.number_input("Over Completed")
with col5:
    wickets = st.number_input("Wickets out")

if st.button("Predict Probability"):
    runs_left = target - score
    balls_left = 120 -(overs*6)
    wickets = 10 - wickets
    crr = score/overs
    rrr = (runs_left*6)/balls_left

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],
                  'city':[selected_city],'run_left':[runs_left],
                  'ball_left':[balls_left],'wicket':[wickets],'total_runs_x':[target],
                  'crr':[crr],'rrr':[rrr]})
    result = pipe.predict_proba(input_df)
    loss = (result[0][0])*100
    win = (result[0][1])*100
    st.header(batting_team + "- " +str(round(win)) + "% " )
    st.header(bowling_team + "- " +str(round(loss)) + "% ")