# homepanelapi [![Build Status](https://travis-ci.com/timmo/python-homepanelapi.svg?branch=master)](https://travis-ci.com/timmo/python-homepanelapi)

Python Package for Home Panel's API.

## Install

Installation **Requires Python version 3.6+**

```bash
pip install homepanelapi
```

### Example

```bash
homepanelapi --host localhost --port 8234 --username username --password password --page Home --card Image --command expand
```

#### CLI options

| param        | alias | description                       |
| ------------ | ----- | --------------------------------- |
| `--host`     | `-h`  | Home Panel's Hostname.            |
| `--port`     | `-P`  | The Home Panel Port.              |
| `--ssl`      | `-s`  | Use ssl?                          |
| `--username` | `-u`  | Your Home Panel Username.         |
| `--password` | `-p`  | Your Home Panel Password.         |
| `--endpoint` | `-e`  | The path after the host and port. |
| `--data`     | `-d`  | Data to send.                     |
