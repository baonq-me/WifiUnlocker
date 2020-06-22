#!/usr/bin/env python3

import tornado.ioloop
import tornado.web
import tornado.log
import tornado.options
import logging
from tornado.log import enable_pretty_logging

import time

import importlib
import json
import argparse
import re
import uuid
import subprocess
from gpiozero import LED
from time import sleep

enable_pretty_logging()


# https://gist.github.com/mminer/5464753
class DefaultHandler(tornado.web.RequestHandler):
    """Request handler where requests and responses speak JSON."""

    def prepare(self):
        # Incorporate request JSON into arguments dictionary.
        if self.request.body:
            try:
                json_data = json.loads(self.request.body)
                self.request.arguments.update(json_data)
            except ValueError:
                message = 'Unable to parse JSON.'
                self.send_error(400, message=message)  # Bad Request

        # Set up response dictionary.
        self.response = dict()

    def set_default_headers(self):
        self.set_header('Content-Type', 'application/json')

    def output(self):
        self.write(self.response)


class 
Me(tornado.web.RequestHandler):
    def prepare(self):
        logging.log(logging.INFO, "Preparing LED 26 ...")
        self.relay = LED(26)

    def get(self):
        self.relay.on()
        sleep(1)
        self.relay.off()
        self.relay.close()

        self.write("{\"time\": " + str(time.time()) + "}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='WifiUnlocker Web API')
    parser.add_argument('-p', '--port', nargs=1, help='Define listen port')
    parser.parse_args()
    args = parser.parse_args()

    application = tornado.web.Application([
        (r"/wifiunlocker/open", WifiUnlocker)
    ], debug=True)

    application.listen(args.port[0], "192.168.4.1")
    tornado.ioloop.IOLoop.instance().start()

