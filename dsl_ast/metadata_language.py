from render_components.page import Page
from render_components.components import ChoiceForm, TextForm, NumberForm, DictForm, ListForm

#########################################################
# NotOrdinalStringColumn
#########################################################
class NotOrdinalStringColumn(Page):
    def __init__(self) -> None:
        super().__init__(
            properties={
                "domain": ListForm(
                    item_name="Domain",
                )
            }   
        )

    def next(self):
        super().next()
        return None

    def build(self, code):
        code['domain'] = self.properties['domain'].value

        return code

#########################################################
# OrdinalStringColumn
#########################################################
class OrdinalStringColumn(Page):
    def __init__(self) -> None:
        super().__init__(
            properties={
                "map": DictForm(
                    item_name="Map",
                )
            }   
        )

    def next(self):
        super().next()
        return None

    def build(self, code):
        code['map'] = self.properties['map'].value

        return code

#########################################################
# OrdinalNumberColumn
#########################################################
class OrdinalNumberColumn(Page):
    def __init__(self) -> None:
        super().__init__(
            properties={
                "domain": ListForm(
                    item_name="Domain",
                )
            }   
        )

    def next(self):
        super().next()
        return None

    def build(self, code):
        code['domain'] = self.properties['domain'].value

        return code

#########################################################
# RealNumberColumn
#########################################################
class RealNumberColumn(Page):
    def __init__(self) -> None:
        super().__init__(
            properties={
                "min": NumberForm(
                    label="Min Value",
                ),
                "max": NumberForm(
                    label="Max Value",
                )
            }   
        )

    def next(self):
        super().next()
        return None

    def build(self, code):
        code['min_value'] = self.properties['min'].value
        code['max_value'] = self.properties['max'].value

        return code
    
#########################################################
# IntegerNumberColumn
#########################################################
class IntegerNumberColumn(RealNumberColumn):
    pass

#########################################################
# Language Start Node
#########################################################

class MetadataLanguage(Page):
    CHILDREN = {
        "NotOrdinalStringColumn": NotOrdinalStringColumn,
        "OrdinalStringColumn": OrdinalStringColumn,
        "OrdinalNumberColumn": OrdinalNumberColumn,
        "RealNumberColumn": RealNumberColumn,
        "IntegerNumberColumn": IntegerNumberColumn,
    } 

    def __init__(self) -> None:
        super().__init__(
            properties={
                "type": ChoiceForm(
                    options=list(self.CHILDREN.keys()),
                    label='Choice witch kind of column do you want to config'
                )
            }   
        )

    def next(self):
        super().next()
        return self.CHILDREN[self.properties['type'].value]()

    def build(self, code):
        code['type'] = self.properties['type'].value

        return code