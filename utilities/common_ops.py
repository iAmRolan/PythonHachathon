import xml.etree.ElementTree as ET
from test_cases import conftest


class CommonOps:

    @staticmethod
    def get_data(node_name):
        path = conftest.get_data_path
        root = ET.parse(path).getroot()
        return root.find(".//" + str(node_name)).text
