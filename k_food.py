import streamlit as st
def k_food():
    k_food = [
        {
            "name": "경아식당",
            "menu": ["부대찌개", "돼지김치찌개", "제육볶음"],
            "price": [7000, 8000, 9000],
            "url": "https://maps.app.goo.gl/s2sgCz9XKFLKibhr8"
        },
        {
            "name": "고향가마솥곰탕",
            "menu": ["곰탕", "육개장", "도가니탕"],
            "price": [8000, 9000, 12000],
            "url": "https://maps.app.goo.gl/Fes22ZK2xgcshUey9"
        },
        {
            "name": "시골쌈밥",
            "menu": ["돌솥쌈밥", "돼지불고기", "오리불고기"],
            "price": [10000, 12000, 15000],
            "url": "https://maps.app.goo.gl/edfsWcPBqtXkkeYo8"
        }
    ]

    while True:
        money = int(st.number_input("예산은 얼마인가요? "))
        kk = []
        available = False

        for i in range(len(k_food)):
            rprice = k_food[i]['price']
            for k in range(len(rprice)):
                if money >= rprice[k]:
                    kk.append((rprice[k], k_food[i]['menu'][k], k_food[i]['name'], k_food[i]['url']))

        if kk:
            kk.sort(key=lambda x: x[0])
            st.write("예산에 맞는 메뉴예요:")
            for item in kk:
                st.write(f"{item[0]} \"{item[1]}\" {item[2]} {item[3]}")
            available = True

        if available:
            return True  					        # 예산에 맞는 메뉴를 찾으면 True값으로 반복문 빠져나감
        else:
            st.write("예산에 맞는 메뉴가 없어요")	# 예산에 맞는 메뉴가 없으면 False값으로 메인화면 선택으로 되돌아감
            return False