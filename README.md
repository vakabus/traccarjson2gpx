# traccarjson2gpx

A conversion script for data dumped from Traccar.

## Requirements

- [Poetry](https://python-poetry.org/)
- Python 3.10 and newer

## Usage

```sh
poetry install  # downloads dependencies (does not affect your whole system)

# place JSON dump in the project's directory and name it input.json
poetry run python convert.py
# the result is in output.gpx
```

## Obtaining JSON dump

Edit the values in the following URL to your likings and open it in a web browser. The JSON report will be downloaded after you provide correct credentials.

```
https://your.traccar.instance/api/positions?deviceId=17&from=2022-07-03T22%3A00%3A00.000Z&to=2022-07-04T22%3A00%3A00.000Z
```


## Licence

GNU GPL v3