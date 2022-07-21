import streamlit as st
import sqlite3
import pandas as pd
import os.path
con = sqlite3.connect('db.db')
cur = con.cursor()

def login_user(id, pw):
    cur.execute(f"SELECT * FROM users WHERE id = '{id}' and pwd = '{pw}'")
    return cur . fetchone()
menu = st.sidebar.selectbox('MENU', options=['로그인','회원가입','회원목록'])

if menu == '로그인':
    st.subheader('로그인')

    login_id = st.text_input('아이디', placeholder = "아이디를 입력하세요")
    login_pw = st.text_input('패스워드' ,
                             placeholder = "비밀번호를 입력하세요",
                             type = 'password')

    login_btn = st.button('로그인')
    if login_btn:
        user_info = login_user(login_id, login_pw)

        file_name = './img/'+user_info[0]+'.jpg'

        if os.path.exists(file_name):
            st.sidebar.image(file_name)
            st.sidebar.write(file_name)
        else :
            st.sidebar.write(user_info[4], '님 환영합니다.')
            st.write(user_info[4],'님 환영합니다')


if menu == '회원가입':
    st.subheader('회원가입')
    st.sidebar.write('회원가입')

    uid = st.text_input('아이디', max_chars=10)
    upw = st.text_input('비밀번호', type = 'password')
    upw_chk = st.text_input('비밀번호확인', type='password')
    uage = st.text_input('나이', max_chars=3)
    uname = st.text_input('사용자 이름', max_chars=16)
    ugender = st.radio('성별', options = ['남', '여'], horizontal= True)
    ubtn = st.button('회원가입')
    st.error('오류 발생')

    if ubtn:
        if upw != upw_chk:
            st.error('비밀번호가 일치하지 않습니다')
            st. warning('비밀번호가 일치하지 않습니다')
            st.stop()
        cur.execute(f"INSERT INTO users(id, pwd, gender, age, name) "
                    f"VALUES('{uid}','{upw}','{ugender}','{uage}','{uname}')")

        con.commit()
        st.success('회원가입이 성공했습니다.')

if menu == '회원목록':
    st.subheader('회원목록')
    df = pd.read_sql('SELECT name, age, gendder FROM users', con)
    st.dataframe(df)
    st.sidebar.write('회원목록')

    st.video('https://www.youtube.com/watch?v=XEmVFbn6P6Y')
