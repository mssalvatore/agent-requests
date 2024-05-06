# agent-requests

A simple tool to fire off web requests with different user agents

## Running the tool

```
$ poetry install
...
$ poetry run python -m agent_requests -t http://localhost:8081 -n 5
```

### Command-line options
```
Usage: agent_requests [OPTIONS]

Options:
  -t, --target TEXT             The target URL to send requests to  [required]
  -n, --num-runs INTEGER RANGE  The number of requests to send for each user
                                agent  [x>=0; required]
  --help                        Show this message and exit
```

## Setting the user agents
At the moment the set of user agents is hard coded, so the only way to change
the user agents is to modify the `AGENTS` tuple in the source code.

## Building an executable for distribution

`poetry run pyinstaller agent_requests/agent_requests.py`

The executable will be written to `dist/agent_requests/agent_requests`.
