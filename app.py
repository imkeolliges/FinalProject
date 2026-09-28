import streamlit as st
import requests

st.set_page_config(layout="wide")

st.title ("✩░▒▓▆▅▃▂▁𝐋𝐲𝐫𝐢𝐜 𝐒𝐩𝐚𝐫𝐤▁▂▃▅▆▓▒░✩")

col1, col2 = st.columns ([2,1])

with col1:
   st.header ("⁺˚⋆｡°✩ 𝚜𝚙𝚊𝚌𝚎 ✸ 𝚏𝚘𝚛 ✸ 𝚕𝚢𝚛𝚒𝚌𝚜 ✩°｡⋆˚⁺")

   txt = st.text_area(
"⁺˚⋆｡°✩ 𝚜𝚙𝚊𝚌𝚎 ✸ 𝚏𝚘𝚛 ✸ 𝚕𝚢𝚛𝚒𝚌𝚜 ✩°｡⋆˚⁺",
     label_visibility="collapsed",
     placeholder="Add your lyrics here",
   )

   word_count = len(txt.split()) if txt else 0
   st.write(f"Word count: {word_count}")

with col2:
    st.subheader ("rhymes and synonyms")
    word = st.text_input ("use for inspiration")

    if st.button ("rhymes"):
     response = requests.get ("https://api.datamuse.com/words", params={"rel_rhy":word})
     data = response.json()

     if data:
        word_list = [item["word"] for item in data]
        st.write(", ".join(word_list))
     else:
        st.write("no rhymes found")

    if st.button ("synonyms"):
     response = requests.get ("https://api.datamuse.com/words", params={"rel_syn":word})
     data = response.json()

     if data:
        word_list = [item["word"] for item in data]
        st.write(", ".join(word_list))
     else:
        st.write("no synonyms found")