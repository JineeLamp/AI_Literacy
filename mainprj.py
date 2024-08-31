# Main
import k_food as kf
import fast_food as ff
import bunsik as bs
import streamlit as st

def food_main():
    st.write("맛집 종류를 선택하세요!")
    menu_number = st.radio("종류선택", ["한식","패스트푸드", "분식"], index=None)
    
    if menu_number == '한식':
        st.write("\"한식\"을 선택하셨네요!")
        st.image('k_food.jpg', width=300)
        kf.k_food() # 예산에 따른 메뉴 확인 및 메시지 출력
        #if not kf.k_food():             
        #    st.write("다시 선택해 주세요")
        
    elif menu_number == '패스트푸드':
        st.write("\"패스트푸드\"를 선택하셨네요!")
        st.image('fastfood.jpg', width=300)
        ff.fast_food()
        #if not ff.fast_food():
        #    st.write("다시 선택해 주세요")
        
    elif menu_number == '분식':
        st.write("\"분식\"을 선택하셨네요!")
        st.image('bunsik.jpg', width=300)
        bs.bunsik()
        #if not bs.bunsik():
        #    st.write("다시 선택해 주세요")
       
    