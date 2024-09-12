from render_components.page import Page
from render_components.components import ChoiceForm
from dsl_ast.connections_language import ConnectionsLanguage
from dsl_ast.metadata_language import MetadataLanguage

class Program(Page):
    CHILDREN = {
        "Connections": ConnectionsLanguage,
        "MetaData": MetadataLanguage,
    } 

    def __init__(self):
        super().__init__(
            properties={
                "languages": ChoiceForm(
                    options=list(self.CHILDREN.keys()),
                    label='Choice witch kind of dsl do you want to build'
                )
            }   
        )

    def next(self):
        super().next()
        return self.CHILDREN[self.properties['languages'].value]()

    def build(self, code):
        return {}