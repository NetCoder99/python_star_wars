class json_helpers():
    @staticmethod
    def getJsonValue(json_str, srch_key):
        if srch_key in json_str['people']:
            return json_str['people'][srch_key]
        else:
            return None   