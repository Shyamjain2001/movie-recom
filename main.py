import pandas as pd
import streamlit as st
import pandas
import pickle
import requests
def fetch_poster(mid):
    res=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=6d3d342e0307cbd7be18c93d0513527e&language=en-US'.format(mid))
    data=res.json()
    return "https://image.tmdb.org/t/p/w500"+data['poster_path']
def com(movie):
    index = mlist[mlist['title'] == movie].index[0]
    # print(index)
    ten = sorted(list(enumerate(simi[index])), reverse=True, key=lambda x: x[1])[:10]
    recmed = []
    posters=[]
    for i in ten:
        mid=mlist.iloc[i[0]].movie_id
        posters.append(fetch_poster(mid))

        recmed.append(mlist.iloc[i[0]].title)
    return recmed,posters


simi=pickle.load(open('simi.pkl', 'rb'))
st.title('Movie Recommender System')
mdict=pickle.load(open('movies.pkl', 'rb'))
mlist=pd.DataFrame(mdict)



selmoname=st.selectbox(
    'Select a moive',
    mlist['title'].values
)
if st.button:
    rs,pst=com(selmoname)
    col1,col2,col3,col4,col5=st.columns(5)
    for i in range(5):
        with col1:
            st.header(rs[i])
            st.image(pst[i])

