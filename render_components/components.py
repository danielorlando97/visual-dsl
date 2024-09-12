import streamlit as st
from uuid import uuid4

class RenderComponent:
    def view():
        pass

class TextForm(RenderComponent):
    def __init__(
            self, 
            label,
            description=None,
            placeholder=None,
        ) -> None:
        super().__init__()

        self._label = label
        self._description = description
        self._placeholder = placeholder

        self._value = None

    @property
    def value(self):
        return self._value

    def view(self):
        self._value = st.text_input(
            label=self._label, 
            value=self._value,
            placeholder=self._placeholder,
            help = self._description,
            # label_visibility ("visible", "hidden", or "collapsed")
        )

class NumberForm(RenderComponent):
    def __init__(
            self, 
            label,
            description=None,
            placeholder=None,
        ) -> None:
        super().__init__()

        self._label = label
        self._description = description
        self._placeholder = placeholder

        self._value = None

    @property
    def value(self):
        return self._value

    def view(self):
        self._value = st.number_input(
            label=self._label, 
            value=self._value,
            placeholder=self._placeholder,
            help = self._description,
            # label_visibility ("visible", "hidden", or "collapsed")
        )

class ChoiceForm(RenderComponent):
    def __init__(self, 
        options,
        label,
        description=None
    ) -> None:
        super().__init__()

        self._label = label
        self._description = description
        
        self.options = options
        self._value = None

    @property
    def value(self):
        return self._value    

    def view(self):

        index = None
        if self._value:
            index = self.options.index(self._value)

        self._value = st.selectbox(
            label=self._label, 
            options=self.options, 
            index=index,
            help = self._description,
            # label_visibility ("visible", "hidden", or "collapsed")
        )

class DictForm(RenderComponent):
    def __init__(self, item_name, description=None, default=None) -> None:
        super().__init__()

        self._label = item_name
        self._description = description

        self.items = [
            {'key': key, 'value': val}
            for key, val in (default or {}).items()
        ]
    
    def _add_item(self):
        self.items.append({'key': '', 'value': ''})

    @property
    def value(self):
        return {
            x['key']:x['value']
            for x in self.items
        }

    def view(self):
        st.subheader(
            self._label, 
            divider= True,
            help= self._description
        )

        l, r = st.columns(2)
        for idx, entry in enumerate(self.items):
            entry['key'] = l.text_input(
                f"Llave {idx+1}", 
                value=entry['key'], 
                key=f"item_key_{idx}_{hash(self)}",
                label_visibility='collapsed'
            )
            
            entry['value'] = r.text_input(
                f"Valor {idx+1}", 
                value=entry['value'], 
                key=f"item_value_{idx}_{hash(self)}",
                label_visibility='collapsed'
            )

        if l.button(f"Add {self._label}"):
            self._add_item()
            st.rerun()

        if r.button(f"Remove {self._label}", disabled=not bool(self.items)):
            self.items.pop()
            st.rerun()


class ListForm(RenderComponent):
    def __init__(self, item_name, description=None, default=None) -> None:
        super().__init__()

        self._label = item_name
        self._description = description

        self.items = default or []
    
    def _add_item(self):
        self.items.append('')

    @property
    def value(self):
        return self.items
    
    def view(self):
        st.subheader(
            self._label, 
            divider= True,
            help= self._description
        )

        l, r = st.columns(2)
        for idx, value in enumerate(self.items):
            if idx % 2 == 1:
                self.items[idx] = l.text_input(
                    f"Llave {idx+1}", 
                    value=value, 
                    key=f"item_key_{idx}_{hash(self)}",
                    label_visibility='collapsed'
                )
            
            if idx % 2 == 0:
                self.items[idx] = r.text_input(
                    f"Llave {idx+1}", 
                    value=value, 
                    key=f"item_key_{idx}_{hash(self)}",
                    label_visibility='collapsed'
                )

        if l.button(f"Add {self._label}"):
            self._add_item()
            st.rerun()

        if r.button(f"Remove {self._label}", disabled=not bool(self.items)):
            self.items.pop()
            st.rerun()