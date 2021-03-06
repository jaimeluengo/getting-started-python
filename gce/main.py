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
    logging.info('Received call to hello_world_handler.')
    return 'Hello world!'

@app.route('/<int:num_seconds>', methods=['GET'])
def one_minute_handler(num_seconds):
    logging.info('Received call for '+str(num_seconds)+' s time request.')
    time.sleep(num_seconds)
    logging.info('Waited successfully '+str(num_seconds)+' s.')
    return 'After waiting '+str(num_seconds)+' s it still worked!'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
