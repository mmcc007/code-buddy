# Code Buddy Assist

Code Buddy Assist is a powerful tool designed to enhance your coding experience by leveraging Large Language Models (LLMs) to provide comprehensive support for your codebase. It bridges the gap between your project and AI, offering assistance from high-level architectural decisions down to detailed bug fixing.

## What Code Buddy Assist Does

1. **Project Snapshot Creation**: Generates a structured JSON representation of your project, providing a clear overview of your codebase structure.

2. **LLM Integration**: Utilizes a carefully crafted prompt to set up an AI coding assistant tailored to your needs, whether using Claude, GPT, or other compatible LLMs.

3. **Contextual Code Understanding**: By combining the project snapshot with the AI prompt, Code Buddy Assist enables the LLM to understand your specific project context.

4. **Multi-level Support**:
   - **Architectural Guidance**: Assists with high-level design decisions and project structure optimization.
   - **Code Review**: Offers suggestions for code improvements and best practices.
   - **Bug Fixing**: Helps identify and resolve issues in your code.
   - **Feature Development**: Provides guidance on implementing new features.
   - **Documentation**: Assists in creating and improving code documentation.

5. **Continuous Learning**: As you interact with the AI through your project context, it becomes increasingly familiar with your codebase, offering more tailored and insightful assistance over time.

Code Buddy Assist transforms the way developers interact with AI, creating a personalized coding companion that understands the nuances of your project and can assist at every stage of development.

## Benefits of LLM Independence

Some LLM-based code assistants run into usage limits or restrictions, which can interrupt the development workflow. Since Code Buddy Assist is LLM-independent, it allows you to easily switch to another LLM when running into usage limits or when specific LLM features are needed. This flexibility ensures continuous and uninterrupted coding assistance, adapting to your evolving needs.

## Installation

To install Code Buddy Assist, run the following command:

```
pip install code-buddy-assist
```

## Usage

Currently, Code Buddy Assist supports the following command:

### Create a Project Snapshot

To create a snapshot of your project (excluding image files), use the `snapshot` command:

```
code-buddy-assist snapshot
```

This will create a JSON file named `project_snapshot_no_images.json` in your current directory, containing a structured representation of your project files.

You can specify a custom output file name using the `--output` option:

```
code-buddy-assist snapshot --output my_project_snapshot.json
```

Note: The `snapshot` command requires that you run it from within a Git repository.

## Using the Code Buddy Prompt with an LLM

Code Buddy Assist includes a prompt file (`coding_buddy_prompt.txt`) that can be used with Large Language Models (LLMs) to create an AI coding assistant. Here's how you can use it:

1. Locate the `coding_buddy_prompt.txt` file in the root directory of the Code Buddy Assist Assist project.

2. Choose an LLM platform or API (e.g., OpenAI's GPT, Anthropic's Claude, or any other compatible service).

3. When starting a new conversation or session with the LLM, begin by pasting the entire contents of `coding_buddy_prompt.txt` as the initial prompt.

4. The LLM will now assume the role of Code Buddy Assist, an AI coding assistant with the characteristics and capabilities described in the prompt.

5. You can then proceed to ask coding-related questions, request help with debugging, or seek advice on best practices.

Note: This prompt can be used to create a Claude Project in Anthropic's Claude platform or a custom GPT in OpenAI's GPT platform. This allows you to have a persistent AI coding assistant tailored to your needs.

Example interaction:
```
Human: Hello, I need help with a Python function.
AI: Hello! I'm Code Buddy Assist, your AI coding assistant. I'd be happy to help you with your Python function. Could you please provide more details about what you're trying to accomplish or share the code you're working on? This will help me give you more accurate and tailored assistance.
```

## Uploading the Project Snapshot to an LLM

After creating a project snapshot, you can upload it to an LLM to provide context about your project structure. Here's how:

1. Create the project snapshot as described above.

2. Open the generated JSON file (e.g., `project_snapshot_no_images.json`).

3. In your conversation with the LLM, you can paste the contents of the JSON file to provide context about your project structure. For example:

```
Human: Here's the project snapshot:

[PASTE JSON CONTENT HERE]

AI: Thank you for providing the project snapshot. I've received it and will use it to better understand your project structure. How can I assist you further today?
```

## License

This project is licensed under the MIT License.
