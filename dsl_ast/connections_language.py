from render_components.page import Page
from render_components.components import ChoiceForm, TextForm, DictForm


#########################################################
# APIConnection
#########################################################

class ApiConnectionUrlConfig(Page):
    def __init__(self) -> None:
        super().__init__(
            properties={
                "host": TextForm(
                    label="Api Host",
                    placeholder="https://"
                ),
                "endpoint": TextForm(
                    label="Api Endpoint",
                    placeholder='/'
                ),
                "headers": DictForm(
                    item_name="Headers",
                    default={
                        'Content-Type': 'application/json'
                    }
                ),
                "params": DictForm(
                    item_name="Params"
                ),
            }   
        )

    def next(self):
        super().next()
        return None

    def build(self, code):
        code['connection_params']['type'] = 'api'
        code['connection_params']['host'] = self.properties['host'].value
        code['connection_params']['endpoint'] = self.properties['endpoint'].value
        code['connection_params']['headers'] = {
            item['key'] : item['value']
            for item in self.properties['headers'].items
        }
        code['connection_params']['params'] = {
            item['key'] : item['value']
            for item in self.properties['params'].items
        }

        return code


#########################################################
# S3Connection
#########################################################

class S3ConnectionConfig(Page):
    def __init__(self) -> None:
        super().__init__(
            properties={
                "bucket": TextForm(
                    label="Bucket Name",
                    placeholder='s3://'
                ),
                "path": TextForm(
                    label="S3 Subpath",
                    description="This field supports parameterization using the syntaxes, for example, `/courses/{organization}/{term}/{campus}/{origin}`",
                    placeholder='/'
                ),
            }   
        )

    def next(self):
        super().next()
        return None

    def build(self, code):
        code['connection_params']['type'] = 's3'
        code['connection_params']['bucket'] = self.properties['bucket'].value
        code['connection_params']['path'] = self.properties['path'].value

        return code

#########################################################
# Language Start Node
#########################################################

class ConnectionsLanguage(Page):
    CHILDREN = {
        "API": ApiConnectionUrlConfig,
        "S3": S3ConnectionConfig,
        "JDBC": None,
    } 

    def __init__(self) -> None:
        super().__init__(
            properties={
                "data_code": TextForm(
                    label="Write a data code for the new connection",
                    description="Remember the format of data codes are `{data_domain_code}/{data_entity_code}`",
                    placeholder="{data_domain_code}/{data_entity_code}"
                ),
                "type": ChoiceForm(
                    options=list(self.CHILDREN.keys()),
                    label='Choice witch kind of connection do you want to build'
                ),
                "search_params": DictForm(
                    item_name="Search Params",
                    default={
                        'tenant': '',
                        'env': ''
                    }
                ),
            }   
        )

    def next(self):
        super().next()
        return self.CHILDREN[self.properties['type'].value]()

    def build(self, code):
        code['data'] = self.properties['data_code'].value
        code |= self.properties['search_params'].value
        code['connection_params'] = {}

        return code