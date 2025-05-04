from patterns.adapter.logger import LoggerAdapter, XmlLogger, JsonLogger

if __name__ == "__main__":
    xml_logger = LoggerAdapter(XmlLogger())
    xml_logger.log_message("<message>hello</message>")

    json_logger = JsonLogger()
    json_logger.log_message("{'message' : 'hello' }")
