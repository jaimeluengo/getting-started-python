# Copyright 2019 Google LLC All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from flask import Flask
import logging
import time
app = Flask(__name__)


@app.route('/', methods=['GET'])
def hello_world_handler():
    logging.error('Received call to hello_world_handler.')
    return 'Hello world!'

@app.route('/1mins', methods=['GET'])
def one_minute_handler():
    logging.error('Received call for 1 minute time request.')
    time.sleep(60*1)
    logging.error('Waited successfully 1 minute.')
    return "After waiting 1 mins it still worked!"

@app.route('/3mins', methods=['GET'])
def three_minute_handler():
    logging.error('Received call for 3 minute time request.')
    time.sleep(60*3)
    logging.error('Waited successfully 3 minute.')
    return "After waiting 3 mins it still worked!"

@app.route('/4mins', methods=['GET'])
def four_minute_handler():
    logging.error('Received call for 4 minute time request.')
    time.sleep(60*4)
    logging.error('Waited successfully 4 minute.')
    return "After waiting 4 mins it still worked"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
