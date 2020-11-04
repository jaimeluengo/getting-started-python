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
import time
app = Flask(__name__)


@app.route('/3mins', methods=['GET'])
def three_minute_handler():
    time.sleep(60*3)
    return "After waiting 3 mins it still worked!"

@app.route('/4mins', methods=['GET'])
def four_minute_handler():
    time.sleep(60*4)
    return "After waiting 4 mins it still worked"


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
