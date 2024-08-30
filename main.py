import streamlit as st
import electric_car as ec
import pybasic as pb
import mainprj as mp    #team project
import car_predict as cp
import intro as it


#로그인 화면
st.sidebar.title(">>로그인")
user_id = st.sidebar.text_input("아이디(ID) 입력",value='abc',max_chars=10)
user_pw = st.sidebar.text_input('패스워드 입력', value='',type='password')

#st.write(user_id)
#st.write(user_pw)

if user_id =='abc' and user_pw == '1234':
    st.sidebar.title("***KBWC AI Literacy Portfolio***")
    #st.image('gall.jpg')

    menu = st.sidebar.radio('포트폴리오 선택', ['소개','파이썬기초','탐색적 분석: 전기자동차 수요', '머신러닝: 자동차 가격예측', '미니프로젝트: 맛집 추천'], index=None)
    st.sidebar.write(menu)

    if menu =='탐색적 분석: 전기자동차 수요':
        ec.elec_exe()
    elif menu == "머신러닝: 자동차 가격예측":
        cp.aiml_main()
    elif menu == "파이썬기초":
        pb.basic()
    elif menu == "미니프로젝트: 맛집 추천":
        mp.food_main()
    elif menu == "소개":
        it.intro_main()
        



