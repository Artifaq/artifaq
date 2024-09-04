# Artifaq

![Artifaq Logo](logo.png)

[![PyPI version](https://badge.fury.io/py/artifaq.svg)](https://badge.fury.io/py/artifaq)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python Versions](https://img.shields.io/pypi/pyversions/artifaq.svg)](https://pypi.org/project/artifaq/)

Artifaq is a Python web framework built on top of FastAPI, designed to provide a rigid structure and simplified development experience.

## Features

- 🚀 **FastAPI Performance**: Leverage the speed and efficiency of FastAPI.
- 🏗️ **Opinionated Project Structure**: Clear, predefined project organization for immediate productivity.
- 🔧 **Simplified Configuration**: Automatic configuration loading for quick setup.
- 🧩 **Modularity**: Organize your application into reusable and independent modules.
- 🛣️ **Automatic Routing**: Automatic route discovery and registration.
- 🔒 **Built-in Security**: Basic implementations for authentication and authorization.
- 🗃️ **Flexible ORM**: Easy integration with various ORMs (SQLAlchemy, SQLModel, etc.).

## Installation

```bash
pip install artifaq
```

## Quick Start

1. Create a new Artifaq project:

```bash
artifaq new my_project
cd my_project
```

## Project Structure

```
my_project/
├── apps/
│   ├── first_app/
│   │   ├── config.py
│   │   ├── models.py
│   │   └── router.py
│   └── second_app/
│       ├── config.py
│       ├── models.py
│       └── router.py
├── config/
│   ├── app.py
│   ├── database.py
│   └── middleware.py
├── main.py
├── poetry.lock
└── poetry.toml

```

## Documentation

For full documentation, visit [documentation]().

## Contributing

Contributions are welcome! Please check out our [contribution guide](CONTRIBUTING.md) to get started.

## License

Artifaq is distributed under the MIT license. See the `LICENSE` file for more information.

## Support

For help or to report a bug, please [open an issue](https://github.com/Artifaq/artifaq/issues).


---

Built with ❤️ by [ER28](https://github.com/ER-28)