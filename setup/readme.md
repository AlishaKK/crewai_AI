

### **1. UV Setup Commands**
| **Command**                           | **Explanation**                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------|
| `powershell -c "irm ... | iex"`       | Installs UV on Windows using PowerShell.                                       |
| `uv version`                          | Checks the installed version of UV.                                            |
| `uv init --package <project-name>`    | Creates a new UV project with the given name.                                  |
| `uv venv`                             | Creates a virtual environment for the project.                                 |
| `.venv\Scripts\activate`              | Activates the virtual environment.                                             |
| `uv add <package-name>`               | Installs a Python package in the project.                                      |
| `uv run <project-name>`               | Runs the project.                                                              |

---

### **2. LiteLLM Commands**
| **Command**                           | **Explanation**                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------|
| `uv add litellm`                      | Installs LiteLLM in your UV project.                                           |
| `llm.chat(prompt=<your_prompt>)`      | Sends a prompt to the LiteLLM language model and gets a response.              |
| `llm.chat(prompt="Tell me a joke.")`  | Example command to generate a response from the AI model.                      |

---

### **3. CrewAI Commands**
| **Command**                           | **Explanation**                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------|
| `pip install crewai[tools] --user`    | Installs CrewAI and its extra tools for AI processing.                         |
| `tools.add(<task_name>, <task_description>)` | Adds a task to CrewAI's toolbox.                                               |
| `tools.run()`                         | Executes tasks added to CrewAI's toolbox.                                      |

---

### **4. VS Code Commands**
| **Command**                           | **Explanation**                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------|
| `code .`                              | Opens the current project folder in VS Code.                                   |

---

### **5. General Python Commands**
| **Command**                           | **Explanation**                                                                 |
|---------------------------------------|---------------------------------------------------------------------------------|
| `pip install <package>`               | Installs a Python package globally or within your virtual environment.         |
| `pip install python-dotenv`           | Installs the `dotenv` package for managing environment variables.              |

---

## **Step 2: Update the `pyproject.toml` File**

The `pyproject.toml` file is used to configure your Python project dependencies and settings. Here's how to update it step-by-step:

### **1. Open the File**
After running `uv init`, your project folder contains a `pyproject.toml` file. Open it in **VS Code** or any text editor.

---

### **2. Update Dependencies**
Add or update the `[tool.poetry.dependencies]` section with the libraries you need. For example:

```toml
[tool.poetry.dependencies]
python = "^3.10"
litellm = "^0.2.0"
crewai = "^1.1.0"
```

- Replace the versions (e.g., `^0.2.0`) with the desired version or leave them as the latest.

---

### **3. Save and Sync Dependencies**
After editing, install or update the dependencies with UV:
```powershell
uv sync
```

**Explanation:**  
This command ensures all dependencies in `pyproject.toml` are installed in your virtual environment.

---

### **4. Example `pyproject.toml`**
Here’s a full example of what your `pyproject.toml` might look like for a LiteLLM and CrewAI project:

```toml
[tool.poetry]
name = "myproject"
version = "0.1.0"
description = "A sample project using LiteLLM and CrewAI"
authors = ["Your Name <youremail@example.com>"]

[tool.poetry.dependencies]
python = "^3.10"
litellm = "^0.2.0"
crewai = "^1.1.0"

[build-system]
requires = ["poetry-core>=1.0.0"]
build-backend = "poetry.core.masonry.api"
```

---

## **Step 3: Testing Everything**

1. **Activate Your Virtual Environment**
   ```powershell
   .venv\Scripts\activate
   ```

2. **Run the Project**
   ```powershell
   uv run myproject
   ```

3. **Add LiteLLM and CrewAI Code in `src/main.py`**
   Here's a simple test script:
   ```python
   from litellm import LiteLLM
   import crewai

   # Initialize LiteLLM
   llm = LiteLLM(api_key="your_openai_api_key")

   # Initialize CrewAI
   tools = crewai.Toolbox()

   # Test LiteLLM
   response = llm.chat(prompt="Explain what AI is.")
   print("LiteLLM Response:", response)

   # Test CrewAI
   tools.add("Task Example", "Processing with CrewAI tools.")
   tools.run()
   print("CrewAI task completed.")
   ```

---

## **Quick Recap for Beginners**

1. Install UV:  
   ```powershell
   powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
   ```

2. Create a project:  
   ```powershell
   uv init --package myproject
   cd myproject
   ```

3. Set up a virtual environment:  
   ```powershell
   uv venv
   .venv\Scripts\activate
   ```

4. Add LiteLLM:  
   ```powershell
   uv add litellm
   ```

5. Install CrewAI:  
   ```powershell
   pip install crewai[tools] --user
   ```

6. Edit `pyproject.toml` and sync dependencies:  
   ```powershell
   uv sync
   ```

7. Write your Python code in `src/main.py` and test it:  
   ```powershell
   uv run myproject
   ```


