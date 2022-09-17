import logging

logging.basicConfig(level=logging.DEBUG,
                    filename="log.log",
                    format="%(asctime)s - %(levelname)s : %(filename)s %(message)s")

logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")