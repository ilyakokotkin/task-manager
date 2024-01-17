
# WhatsApp Scheduler

This Python script allows you to schedule the opening and closing of desktop task processes at specified times.

## Features

- Schedule opening and closing of desktop apps.
- Flexibility to specify the path to the executable.
- Uses Object-Oriented Programming principles and Test Driven Development.

## Requirements

- Python 3
- `schedule` Python module

## Installation

Clone this repository or download the script. Install the required Python module:

```bash
pip install schedule
```

## Usage

### Command Line Arguments

You can pass the path to the executable as a command line argument:

```bash
python main.py "path_to__executable"
```

### Environment Variables

Alternatively, set the path as an environment variable `TASK_PATH`:

```bash
export TASK_PATH="path_to_p_executable"
```

### Configuration File

Or use a configuration file `config.json` with the following content:

```json
{
    "path_to_task": "path_to_task_executable"
}
```

## Running the Script

Run the script using Python. Ensure that it's continuously running to maintain the schedule:

```bash
python main.py
```

## Testing

Tests are written using `pytest`. Run the tests with:

```bash
pytest
```

## License

This project is licensed under the MIT License.

