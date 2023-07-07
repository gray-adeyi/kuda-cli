# Kuda cli
A command line app for interacting with kuda open API.

![utility in use](./kuda-cli.gif)

## Installation
Binaries of kuda cli be found [here](). Alternatively, Kuda cli can be installed from pypi
with pip as shown below.
```bash
pip install kuda-cli
```

## First time configurations
You're required to add your kuda credentials on first use as shown below
```bash
kuda config EMAIL API_KEY
```
This sets up your kuda cli for use in development mode you
can add an optional `--mode production` to use this utility in production mode. These credentials can be
removed with `kuda reset`. Run `kuda --help` to see available commands