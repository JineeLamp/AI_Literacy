import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import matplotlib.font_manager as fm

#import koreanize_matplotlib
#한글 글꼴
plt.rc('font', family = 'malgun gothic')

def basic():
       #파일 불러오기
       df = pd.read_csv('한국전력공사_지역별 전기차 현황정보_20230331.csv', encoding='EUC-KR')

       #피벗 해제(열의 데이터로 변환)
       df_melt = pd.melt(df, id_vars='기준일', value_vars=['서울', '인천', '경기', '강원', '충북', '충남', '대전', '세종', '경북', '대구', '전북',
              '전남', '광주', '경남', '부산', '울산', '제주', '합계'], var_name='지역', value_name='자동차수')

       #'년', '월' 파생변수 생성
       df_melt['년'] = df_melt['기준일'].str[:4]
       df_melt['월'] = df_melt['기준일'].str[5:7]

       return df_melt

def region_mean(df_melt):   #()값은 프로그램 안에서 쓰는 변수명을 활용
       #**********************************
       #지역별, 년도별 지동차수 평균 계산 - pivot table
       year_region_da = round(pd.pivot_table(df_melt,index='년', columns='지역', values='자동차수', aggfunc='mean'),0) #소숫점없이 0으로 설정
       st.dataframe(year_region_da) #print(year_region_da)

       #행,열 전환
       year_region_da = year_region_da.T
       #행의 데이터 추출, df[(조건)|(조건)], df[(조건)&(조건)]
       region_query = year_region_da[year_region_da.index != '합계']

       #데이터 프레임 이용한 차트
       #year_region_da.plot(kind='bar', rot=0)
       ax = region_query.plot(kind='bar', rot=0) #plt.show()
       fig = ax.get_figure()
       st.pyplot(fig)
       

def mean_2023(df_melt):
       #**********************
       #2023년 자동차수 분석
       df_melt_2023 = df_melt[df_melt['년'] == '2023']
       df_melt_2023 = df_melt_2023[df_melt_2023['지역'] !='합계']

       #피벗 테이블
       df_2023 = pd.pivot_table(df_melt_2023,index='지역', columns='월', values='자동차수', aggfunc='mean')
       st.dataframe(df_2023.T)       #st.table(df_2023): 같은 테이블 형태나 인터렉티브는 무, T는 행,열 변환
       #df_2023 = df_2023.T
       ax = df_2023.plot(kind='bar', rot=0) #plt.show()
       fig = ax.get_figure()
       st.pyplot(fig)
      

def quarter_mean(df_melt):
       #**********************
       #2022년 분기별 분석
       #2022년 데이터추출
       df_2022 = df_melt[df_melt['년'] == '2022']

       #데이터 타입을 정수로 변환
       df_2022['월'] = df_2022['월'].astype(int)

       #조건 비교 함수로 파생변수 생성
       df_2022['분기'] = np.where((df_2022['월'] >= 1) & (df_2022['월'] <= 3), "1분기", 
                            np.where((df_2022['월'] >= 4) & (df_2022['월'] <= 6), "2분기", 
                            np.where((df_2022['월'] >= 7) & (df_2022['월'] <= 9), "3분기", 
                            "4분기")))

       #분기별 자동차수 평균 계산 - pivot table
       quart_region_da = round(pd.pivot_table(df_2022, index='지역',columns='분기',values='자동차수',aggfunc='mean'),0)
       #합계를 제외한 분기별 자동차수 평균
       quart_region_da = quart_region_da[quart_region_da.index != '합계'] 
       st.dataframe(quart_region_da.T)      #print(quart_region_da)
       
       #통계: groupby & 2개 인덱스 숫자 인덱스로 변경:groupby, reset_index()
       #df_2022_da2 = df_2022.groupby(['지역','분기'])[['자동차수']].mean().reset_index() #표형식으로 할 때 계산할 변수에 []한번 더 사용
       #st.dataframe(df_2022_da2) #print(df_2022_da2)

       #판다스를 이용한 차트 작성
       ax = quart_region_da.plot(kind='bar', rot=0)   #plt.show()
       fig = ax.get_figure()
       st.pyplot(fig)

#메인 실행
def elec_exe():
    menu = st.selectbox("분석내용",['선택','지역별/연도별 분석','2023년 지역별 분석', '2022년 분기별 분석'])
    df_melt = basic()       #받은 값을 주려면 기억해야 함 변수명이 같더라도 다른 작업

    if menu == '지역별/연도별 분석':
          region_mean(df_melt)
    elif menu == '2023년 지역별 분석':
          mean_2023(df_melt)       #2023년 지역별 분석
    elif menu == '2022년 분기별 분석':
          quarter_mean(df_melt)    #2022년 분기별 분석
    else:
          st.image('gall.jpg', width=500)

if __name__=='__main__':    #내부호출일때만 화일실행, 외부호출은 미실행
      elec_exe()
