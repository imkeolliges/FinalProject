import streamlit as st


st.set_page_config(layout="wide")

st.title ("✩░▒▓▆▅▃▂▁𝐋𝐲𝐫𝐢𝐜 𝐒𝐩𝐚𝐫𝐤▁▂▃▅▆▓▒░✩")

st.header ("⁺˚⋆｡°✩ 𝚜𝚙𝚊𝚌𝚎 ✸ 𝚏𝚘𝚛 ✸ 𝚕𝚢𝚛𝚒𝚌𝚜 ✩°｡⋆˚⁺")

txt = st.text_area(
"⁺˚⋆｡°✩ 𝚜𝚙𝚊𝚌𝚎 ✸ 𝚏𝚘𝚛 ✸ 𝚕𝚢𝚛𝚒𝚌𝚜 ✩°｡⋆˚⁺",
label_visibility="collapsed",
    placeholder="Add your lyrics here",
)

st.write(f"You wrote {len(txt)} characters.")