import streamlit as st
from render_components.components import RenderComponent

class Page:
    def __init__(self, properties: dict[str, RenderComponent]) -> None:
        self.properties=properties

    @property
    def is_focussed(self):
        try:
            return st.session_state[self.__repr__()]
        except:
            return False
        
    def start(self):
        if self.__repr__() not in st.session_state:
            st.session_state[self.__repr__()] = True

        return self       

    def next(self):
        st.session_state[self.__repr__()] = False

    def __repr__(self) -> str:
        return self.__class__.__name__
    
    def view(self):
        for comp in self.properties.values():
            comp.view()
