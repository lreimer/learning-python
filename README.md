# learning-python

Learning Python. Many small Python experiments.

## CLIs with Click

```bash
pip install click

./greeting.py
./greeting.py --help
./greeting.py --greeting Hi --name Dude
```

## Load tests with Molotov

```bash
pip install molotov
molotov -v -r 100 molotov.py
./molotov.py
```

## Microservice with Flask

```bash
pip install Flask gunicorn Werkzeug

gcloud config set project cloud-native-experience-lab
gcloud run deploy
# confirm everything with Y, choose a desired region
# make sure to allow unauthenticated invocations

https get learning-python-1091663571214.europe-north1.run.app
https get learning-python-1091663571214.europe-north1.run.app name==Leander
```

## Maintainer

M.-Leander Reimer (@lreimer), <mario-leander.reimer@qaware.de>

## License

This software is provided under the MIT open source license, read the `LICENSE`
file for details.
