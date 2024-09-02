# Code BuddyCode Buddy is a command-line utility to assist with coding tasks.

## Installation

To install Code Buddy, run the following command:

```
pip install code-buddy
```

## Usage

Currently, Code Buddy supports the following command:

### Create a Project Snapshot

To create a snapshot of your project (excluding image files), use the `snapshot` command:

```
code-buddy snapshot
```

This will create a JSON file named `project_snapshot_no_images.json` in your current directory, containing a structured representation of your project files.

You can specify a custom output file name using the `--output` option:

```
code-buddy snapshot --output my_project_snapshot.json
```

Note: The `snapshot` command requires that you run it from within a Git repository.

## License

This project is licensed under the MIT License.
