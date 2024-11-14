import os
import json
import argparse
import sys
from git import Repo, InvalidGitRepositoryError, GitCommandError
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def get_git_repo(path):
    """Retrieve the Git repository from the given path."""
    try:
        repo = Repo(path, search_parent_directories=True)
        return repo
    except InvalidGitRepositoryError:
        logging.error("No Git repository found. Please run this command from within a Git repository.")
        raise
    except GitCommandError as e:
        logging.error(f"Git error: {str(e)}")
        raise

def get_all_files(repo):
    """Get all files from the Git repository, including untracked files."""
    git_files = set()
    untracked_files = set()

    # Check if there are any commits in the repository
    if repo.head.is_valid() and repo.head.commit:
        # Get tracked files
        for item in repo.tree().traverse():
            if item.type == 'blob':  # Ensure it's a file
                git_files.add(item.path)
    else:
        logging.warning("The repository has no commits. Only untracked files will be included.")

    # Get untracked files
    untracked_files.update(repo.untracked_files)

    # Combine both sets
    all_files = git_files.union(untracked_files)
    return all_files

def is_image_file(filename):
    """Check if a file is an image based on its extension."""
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico', '.yaml', '.woff'}
    return Path(filename).suffix.lower() in image_extensions

# is_file_name: takes a path to a file and returns False if file is excluded, file can be a relative path
def is_excluded_file_name(file):
    # List of file names or directories to exclude
    excluded_files = [
        'node_modules', 'package-lock.json', 'yarn.lock', '.DS_Store', '.gitignore', '.gitattributes', '.gitmodules', 
        '.git', '.idea', '.vscode', '.env', '.env.local', '.env.development', '.env.test', '.env.production', 
        '.env.staging', '.env.local', '.env.*.local', 'npm-debug.log', 'yarn-debug.log', 'yarn-error.log', 'yarn-integrity'
    ]
    
    # Check if the file is in the list of excluded files or in an excluded directory
    file_name = os.path.basename(file)  # Get the base name of the file
    for excluded in excluded_files:
        # Match either the exact file name or a wildcard match (for .env.*)
        if excluded.startswith('.env.*') and file_name.startswith('.env.') or file_name == excluded:
            return True

    # If it's not excluded, return False
    return False


def build_structure(root_path, files):
    """Build a nested dictionary structure representing the project files."""
    structure = {}
    for file_path in files:
        if is_image_file(file_path) or is_excluded_file_name(file_path):
            continue  # Skip image files
        full_path = Path(root_path) / file_path
        # Ensure the file exists
        if full_path.is_file():
            try:
                with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
            except Exception as e:
                logging.error(f"Error reading file {file_path}: {e}")
                content = f"Error reading file: {e}"

            # Split the path to build the nested dictionary
            parts = file_path.split(os.sep)
            current_level = structure
            for part in parts[:-1]:
                if part not in current_level:
                    current_level[part] = {}
                current_level = current_level[part]
            current_level[parts[-1]] = content
    return structure

def create_snapshot(output_file, root_path=None):
    """Create a JSON snapshot of the project."""
    root_path = root_path or os.getcwd()  # Use specified path or current directory
    try:
        repo = get_git_repo(root_path)
        all_files = get_all_files(repo)
        project_structure = build_structure(root_path, all_files)

        # Output to JSON file
        with open(output_file, 'w', encoding='utf-8') as json_file:
            json.dump(project_structure, json_file, indent=4, ensure_ascii=False)

        logging.info(f"Project snapshot (excluding image files) has been saved to {output_file}")
    except ValueError as e:
        logging.error(f"Error: {str(e)}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Code Buddy Assist - Your coding assistant")
    parser.add_argument('command', help='Command to execute (e.g., snapshot)')
    parser.add_argument('--output', default='project_snapshot_no_images.json', help='Output file name')
    parser.add_argument('--path', default=None, help='Path to the project root (optional)')
    args = parser.parse_args()

    if args.command == 'snapshot':
        create_snapshot(args.output, args.path)
    elif args.command == 'help':
        print("""
Code Buddy Assist - Available Commands:

snapshot                 Creates a structured JSON snapshot of your project, excluding image files.
                         Example: code-buddy-assist snapshot

snapshot --output FILE   Specifies a custom output file name for the project snapshot.
                         Example: code-buddy-assist snapshot --output my_project_snapshot.json

snapshot --path PATH     Specifies the path to the project root. Defaults to current directory.
                         Example: code-buddy-assist snapshot --path /path/to/project

help                     Displays this help message.
                         Example: code-buddy-assist help
""")
    else:
        logging.error(f"Unknown command: {args.command}")
        print("Use 'code-buddy-assist help' to see available commands.")

if __name__ == "__main__":
    main()
