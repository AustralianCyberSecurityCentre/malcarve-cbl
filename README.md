# Malcarve

Detects and extracts obfuscated, embedded content from files.

## Overview

Malcarve is a tool for detecting and extracting obfuscated, embedded content
from files. In particular it is targeted at extracting malicious payloads such
as those contained in malware attack documents and droppers.

This version of malcarve has been adapted from https://github.com/shendo/malcarve. Some functionality has been simplified and improved, while other functionality has been removed.

## Installation

Malcarve requires `gcc` to compile its components written in C:

```
sudo apt install gcc
```

Note that only linux x86_64 is supported.

Install using `pip`:

```
pip install malcarve-cbl
```

If installed in editable mode, the C compilation script will need to be manually called:
```
./malcarve-cbl/malcarve_cbl/ext/build.sh
pip install -e malcarve-cbl
```

## Usage

Binary data can be checked for embedded and/or encrypted data via `carve_buffer()`:

```python
from malcarve_cbl.malcarve_cbl import FoundFormat, carve_buffer

data: bytes = b"abYWJjWVdKakVmTG4wTjZBNlB1RWxwcGxaVTVLU1RzNlRSTVM1N2pRMmRlNDk0eUIwRzEzQ1ZZNExEY1hHT1NP"

found_formats: list[FoundFormat] = carve_buffer(data)
print(found_formats[0].content.decode())
print(found_formats[0].encoding_info.encoding_offsets_string)
print(found_formats[0].encoding_info.keyed_encoding_string)
```

Output:

```
https://exampleurl.com/this/is/an/example
base64(0x0-0x56)->base64(0x2-0x41)->xor(0x6-0x2f)
xor(key:0x79, bytes:1, increment:13)
```

In this case, malcarve found an url which had been xor'd, then base64 encoded twice. the xor was identified as being a 2 byte incrementing xor where every time a set of 2 bytes were encoded, the key incremented by 13. The starting key was 0x79.

## Dependency management

Dependencies are managed in the pyproject.toml and debian.txt file.

Version pinning is achieved using the `uv.lock` file.
Because the `uv.lock` file is configured to use a private UV registry, external developers using UV will need to delete the existing `uv.lock` file and update the project configuration to point to the publicly available PyPI registry instead.

To add new dependencies it's recommended to use uv with the command `uv add <new-package>`
    or for a dev package `uv add --dev <new-dev-package>`

The tool used for linting and managing styling is `ruff` and it is configured via `pyproject.toml`

The debian.txt file manages the debian dependencies that need to be installed on development systems and docker images.

Sometimes the debian.txt file is insufficient and in this case the Dockerfile may need to be modified directly to
install complex dependencies.

## Acknowledgements

This repository was based off of https://github.com/shendo/malcarve
