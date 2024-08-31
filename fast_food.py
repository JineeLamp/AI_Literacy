import streamlit as st
def fast_food():
    fast_food = [
        {
            "name": "맥도날드",
            "menu": ["빅맥세트", "상하이버거세트", "베이컨 디럭스세트"],
            "price": [6500, 6900, 7500],
            "url": "https://maps.app.goo.gl/kSMABjF6J5Xo4cBeA"
        },
        {
            "name": "버거킹",
            "menu": ["와퍼세트", "몬스터x세트", "갈릭불고기버거세트"],
            "price": [7500, 9500, 7000],
            "url": "https://maps.app.goo.gl/677iHRU6swVuF1Bo8"
        },
        {
            "name": "kfc",
            "menu": ["징거버세트", "치킨너겟10조각", "오리지널치킨2조각"],
            "price": [6900, 5500, 6000],
            "url": "https://maps.app.goo.gl/nMFutQkWwMsC9HB57"
        }
    ]

    #while True:
    #    money = int(st.number_input("예산은 얼마인가요? "))
    # 예산 입력 받기
    money = st.number_input("예산은 얼마인가요? ", min_value=0, step=1000)
    if money > 0:
        kk = []
        available = False

        for i in range(len(fast_food)):
            rprice = fast_food[i]['price']
            for k in range(len(rprice)):
                if money >= rprice[k]:
                    kk.append((rprice[k], fast_food[i]['menu'][k], fast_food[i]['name'], fast_food[i]['url']))

        if kk:
            kk.sort(key=lambda x: x[0])
            st.write("*"*75)
            st.write("예산에 맞는 메뉴예요:")
            for item in kk:
                st.write(f"{item[0]} \"{item[1]}\" {item[2]} {item[3]}")
            st.write("*"*75)
            available = True

        if available:
            return True  					      # 예산에 맞는 메뉴를 찾으면 True값으로 반복문 빠져나감
        else:
            st.write("예산에 맞는 메뉴가 없어요")	# 예산에 맞는 메뉴가 없으면 False값으로 메인화면 선택으로 되돌아감
            return False
    else:
        st.write("예산을 입력해 주세요")  # 예산이 0이거나 입력되지 않은 경우