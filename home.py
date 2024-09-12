import streamlit as st
import yaml
from dsl_ast.program import Program

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title("Visual Languages")


left, right = st.columns(2)


if 'pages' not in st.session_state:
    st.session_state['pages'] = [Program().start()]

with left:
    focussed_page = None
    for page in st.session_state['pages']:

        if page.is_focussed:

            page.view()
            focussed_page = page

    if st.button("Next"):
        st.session_state['code'] = focussed_page.build(
            st.session_state.get('code'))
        if (next_step := focussed_page.next()):
            st.session_state['pages'].append(next_step.start())
        st.rerun()

code = yaml.dump(st.session_state.get('code', {}), sort_keys=False)

with right:

    st.code(code, language="yaml", )
    if st.button("Restart"):
        for key in st.session_state.keys():
            del st.session_state[key]
        st.rerun()
