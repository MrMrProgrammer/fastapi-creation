**FastAPI Creation** is a powerful CLI tool for scaffolding FastAPI projects quickly and efficiently. It helps developers generate project structures based on different architectural templates, saving time and maintaining consistency across projects.


---


## Features


- Create FastAPI projects with a single command.
- Choose from multiple architectural templates.
- Fully customizable project structure.
- Simple, interactive CLI powered by [Typer](https://typer.tiangolo.com/).


---


## Installation


You can install **FastAPI Creation** via pip:


```bash
pip install fastapi-creation
```


Or if you want to install the latest version from the source:


```bash
git clone https://github.com/username/fastapi-creation.git
cd fastapi-creation
pip install .
```


---


## Usage


Once installed, you can create a new FastAPI project by running:


```bash
fastapi-creation my_project
```


You will be prompted to select a project template:


```
Select a template:
1. clean
2. ddd
3. feature_based
...
Template number [1]:
```


After choosing a template, your project structure will be generated automatically.


---


## Example


```bash
fastapi-creation my_app
```


Output:


```
✅ Project 'my_app' created with template 'clean'
```


---


## Templates & Architecture Details


For a detailed explanation of all available templates and architectural layers, see [TEMPLATES.md](./TEMPLATES.md).


---


## Support & Contribution


If you find this project helpful:


- ⭐ Give it a star on GitHub.
- 🛠️ Contribute to the project by submitting issues or pull requests.
- 💖 Support and spread the word to help the community grow.


---


Made with ❤️ for FastAPI developers.