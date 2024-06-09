# Project Time Management Tool

## Overview

This project provides a simple time management tool for logging work hours on various projects. It allows users to clock-in and clock-out of projects, mark projects as completed, and generate a Gantt chart to visualize the time spent on each project.

## Features

1. **Clock-In**: Log the start time for a project.
2. **Clock-Out**: Log the end time for a project.
3. **Mark Completed**: Mark a project as completed.
4. **Generate Gantt Chart**: Visualize the time spent on each project.

## Prerequisites

- Python 3.x
- pandas
- matplotlib

## Installation

1. Clone the repository or download the source code.
2. Install the required packages using pip:

    ```sh
    pip install pandas matplotlib
    ```

## Usage

### Logging Time

To log time for a project, run the `main` function:

```sh
python main.py
```

This will present the following options:

1. **Clock-In**: Enter the project name to log the start time.
2. **Clock-Out**: Enter the project name to log the end time.
3. **Mark Completed**: Enter the project name to mark it as completed.
4. **Exit**: Exit the program.

### Generating Gantt Chart

To generate a Gantt chart of the logged times, run the `generate_gantt_chart` function:

```sh
python generate_gantt_chart.py
```

This will read the `time_logs.csv` file and create a Gantt chart showing the time spent on each project. The chart will be saved as `gantt_chart.png`.

## File Descriptions

- `main.py`: Contains the main program logic for logging time.
- `generate_gantt_chart.py`: Contains the code for generating the Gantt chart.
- `time_logs.csv`: CSV file where clock-in and clock-out times are logged.
- `completed.csv`: CSV file where completed projects are logged.
- `gantt_chart.png`: Generated Gantt chart image.

## Functions

### log_time(project_name, action)

Logs the time for a given project and action (clock-in or clock-out) to `time_logs.csv`.

**Parameters:**
- `project_name`: Name of the project.
- `action`: Action to log (either 'clockin' or 'clockout').

### mark_completed(project_name)

Marks a project as completed by logging the project name and current timestamp to `completed.csv`.

**Parameters:**
- `project_name`: Name of the project.

### generate_gantt_chart()

Reads the `time_logs.csv` file, processes the data, and generates a Gantt chart showing the time spent on each project. The chart is saved as `gantt_chart.png`.

## Example

1. **Log time**:

    Run the main program:

    ```sh
    python main.py
    ```

    Choose option 1 to clock-in:

    ```
    Enter Choice: 1
    Enter Project name: ProjectA
    ```

    Choose option 2 to clock-out:

    ```
    Enter Choice: 2
    Enter Project name: ProjectA
    ```

2. **Generate Gantt Chart**:

    ```sh
    python generate_gantt_chart.py
    ```

    The Gantt chart will be saved as `gantt_chart.png`.

## Notes

- Ensure the `time_logs.csv` and `completed.csv` files are in the same directory as the scripts.
- If the timestamps in `time_logs.csv` cannot be converted to datetime, the script will print an error message and terminate.

