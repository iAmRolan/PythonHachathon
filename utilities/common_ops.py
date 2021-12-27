import xml.etree.ElementTree as ET


class CommonOps:

    @staticmethod
    def get_data(node_name):
        root = ET.parse("../files/Web_User_to_test.xml").getroot()
        return root.find(".//" + str(node_name)).text
