import os
import json
import argparse
import sys
from git import Repo, InvalidGitRepositoryError, GitCommandError

def get_git_repo(path):
    try:
        repo = Repo(path, search_parent_directories=True)
        return repo
    except InvalidGitRepositoryError:
        raise ValueError("No Git repository found. Please run this command from within a Git repository.")
    except GitCommandError as e:
        raise ValueError(f"Git error: {str(e)}")

def get_all_files(repo):
    git_files = set()
    untracked_files = set()

    # Check if there are any commits in the repository
    if repo.head.is_valid() and repo.head.commit:
        # Get tracked files
        for item in repo.tree().traverse():
            if item.type == 'blob':  # Ensure it's a file
                git_files.add(item.path)
    else:
        print("Warning: The repository has no commits. Only untracked files will be included.")

    # Get untracked files
    untracked_files.update(repo.untracked_files)

    # Combine both sets
    all_files = git_files.union(untracked_files)
    return all_files

def is_image_file(filename):
    image_extensions = {'.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp', '.svg', '.ico', '.yaml'}
    _, ext = os.path.splitext(filename.lower())
    return ext in image_extensions

def build_structure(root_path, files):
    structure = {}
    for file_path in files:
        if is_image_file(file_path):
            continue  # Skip image files
        full_path = os.path.join(root_path, file_path)
        # Ensure the file exists
        if os.path.isfile(full_path):
            with open(full_path, 'r', errors='ignore') as f:
                try:
                    content = f.read()
                except Exception as e:
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

def create_snapshot(output_file):
    root_path = os.getcwd()  # Or specify the path to your project
    repo = get_git_repo(root_path)
    
    all_files = get_all_files(repo)
    project_structure = build_structure(root_path, all_files)

    # Output to JSON file
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(project_structure, json_file, indent=4, ensure_ascii=False)

    print(f"Project snapshot (excluding image files) has been saved to {output_file}")
    
def main():
    parser = argparse.ArgumentParser(description="Code Buddy - Your coding assistant")
    parser.add_argument('command', help='Command to execute')
    parser.add_argument('--output', default='project_snapshot_no_images.json', help='Output file name')
    args = parser.parse_args()

    if args.command == 'snapshot':
        try:
            create_snapshot(args.output)
        except ValueError as e:
            print(f"Error: {str(e)}")
            sys.exit(1)
    else:
        print(f"Unknown command: {args.command}")
        print("Currently, the only valid command is 'snapshot'.")

if __name__ == "__main__":
    main()