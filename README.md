# opsgenie-integration-watchdog

Checks OpsGenie integrations state against expected integration state and triggers an OpsGenie alert if an integration differs from the expected state.

## Requirements
- Python 3
- Docker (optional)

## Installation

- Download code from GitHub
    ```
    git clone https://github.com/rbocchinfuso/opsgenie-integration-watchdog.git
    ```

    _Note:  If you don't have Git installed you can also just grab the zip:  https://github.com/rbocchinfuso/opsgenie-integration-watchdog/archive/master.zip_

- Install required python packages

    ``` 
    pip install -r requirements.txt
    ```

- Execute ```_opsgenie-integration-refresh.py```

    ```
    python _opsgenie-integration-refresh.py OPSGENIE_API_KEY
    ```

- Edit the JSON output file (integrations.json) which contains the key value pairs  [INTEGRATION_NAME:ENABLED_STATE
    - Set the value =  True | False

    _Note: The integrations.json file is the control file which the current stat of the integration will be compared to every hour_

## Usage

### Python 3

- Execute ```opsgenie-integration-watchdog.py```

  ```
  python opsgenie-integration-watchdog.py [OPSGENIE_API_KEY]
  ```

### Docker

- Build an image from a Dockerfile

  ```
  docker build -t opsgenie-integration-watchdog .
  ```

- Run Docker container (daemon)

  ```
  docker run -d --restart=on-failure:10 --name opsgenie-integration-watchdog opsgenie-integration-watchdog [OPSGENIE_API_KEY]
  ```

- Run Docker container (interactive)

  ```
  docker run -it --rm --name opsgenie-integration-watchdog opsgenie-integration-watchdog [OPSGENIE_API_KEY]
  ```

  _Note:  Run interactively when testing_

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request :D

## History

- version 0.1 (initial release) - 2017/10/03

## Credits

Rich Bocchinfuso <<rbocchinfuso@gmail.com>>


## License

MIT License

Copyright (c) [2016] [Richard J. Bocchinfuso]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.