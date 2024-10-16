# learning-python

Learning Python. Many small Python experiments.

## Prerequisites

```bash
# make sure you have at least Python 3.12 installed
python -m venv .venv
source .venv/bin/activate
```

## CLIs with Click

```bash
pip install click

./greeting.py
./greeting.py --help
./greeting.py --greeting Hi --name Dude
```

## Microservice with Flask

```bash
pip install Flask gunicorn Werkzeug
gunicorn -w 1 microservice:app
http get localhost:8000 name==Leander

gcloud config set project cloud-native-experience-lab
gcloud run deploy
# confirm everything with Y, choose a desired region
# make sure to allow unauthenticated invocations

https get learning-python-1091663571214.europe-north1.run.app
https get learning-python-1091663571214.europe-north1.run.app name==Leander
```

## Load tests with Molotov

```bash
pip install molotov
molotov -v -r 10 molotov.py
./molotov.py
```

## Maintainer

M.-Leander Reimer (@lreimer), <mario-leander.reimer@qaware.de>

## License

This software is provided under the MIT open source license, read the `LICENSE`
file for details.
