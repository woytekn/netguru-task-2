import logging


class Logger:

    def __init__(self, context):
        self.current_scenario = ''
        self.current_step = ''
        self.logger = None
        self.context = context

    def logg_info(self, log):
        scenario_info = '[' + self.current_scenario + '][' + self.current_step + ']'

        return scenario_info, log

    def critical(self, log):
        log = self.logg_info(log)
        self.logger.critical(log)

    def warning(self, log):
        log = self.logg_info(log)
        self.logger.warning(log)

    def debug(self, log):
        log = self.logg_info(log)
        self.logger.debug(log)

    def error(self, log):
        log = self.logg_info(log)
        self.logger.error(log)

    def info(self, log):
        log = self.logg_info(log)
        self.logger.info(log)

    def log(self, log):
        log = self.logg_info(log)
        self.logger.log(log)

    def exception(self, log):
        log = self.logg_info(log)
        self.logger.exception(log)

    def shutdown(self):
        logging.shutdown()
