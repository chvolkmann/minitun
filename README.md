# minitun

CLI utility for quickly forwarding SSH ports.

## Installation

From the official Python Package Index (PyPI)

```bash
pip install minitun
```

or directly from Git repository

```bash
pip install git+https://github.com/chvolkmann/minitun.git
```

## Usage

```bash
minitun <SSH_HOST> [PORT_SPECS]...
```

### Examples

```bash
# forwards port 3000 to port 3000 on my-server
# forwards port 8080 to port 80   on my-server
minitun my-server 3000 8080:80
```
