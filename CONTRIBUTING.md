# Contributing to MQF-402 Investment Analysis HW 1 (Group 5)

Each person writes their own question in their own notebook. Nobody edits anyone else's notebook. At the end we combine everything into one final notebook.

## What you need

- A GitHub account (ask the repo owner to add you as a collaborator)
- Python 3.11 or newer
- PyCharm Professional (the free 30-day trial works). Notebooks do not run in PyCharm Community. If you are on Community, use VS Code with the Jupyter extension instead.
- Git (PyCharm or macOS will offer to install it if it is missing)

## One-time setup

1. In PyCharm: **File > New > Project from Version Control**.
2. Paste the repo URL: `<REPO-URL>`, sign in to GitHub if asked, and click **Clone**.
3. Create a virtual environment when PyCharm offers. If it does not, click the interpreter name in the bottom-right corner, then **Add New Interpreter > Add Local Interpreter > Virtualenv**.
4. Open the **Terminal** (the `>_` icon on the left). Check that the line starts with `(.venv)`, then run:
```
   pip install -e ".[dev]"
```
5. Run `pytest`. If it says `1 passed`, you are ready.

## Adding your question

1. **Update main.** Click `main` in the top toolbar, choose `main`, then **Update**.
2. **Create a branch.** Click `main` in the toolbar, choose **New Branch**, and name it after your question, for example `add-q2`.
3. **Create your notebook.** Right-click the `notebooks` folder > **New > Jupyter Notebook** and name it `q2` (or `q3`, and so on). Type the name by hand instead of pasting it. Pasted names can hide invisible characters that break tools later.
4. **Set up the top of your notebook.** Add a Markdown cell with the heading `## Question 2`, then a code cell:
```python
   from mqf_hw1.data import load_data
   import matplotlib.pyplot as plt

   df = load_data()
   df.head()
```
5. **Do your work.** Keep all your code, tables, charts, and written explanations under your question heading.
6. **Check it runs from top to bottom.** Restart the kernel and run all cells before you commit.
7. **Commit and push.** Open the Commit panel (Cmd+K), tick your notebook, write a clear message such as `Add Q2 analysis`, and choose **Commit and Push**.
8. **Open a pull request.** On GitHub click **Compare & pull request**, describe what you added, and create it. The repo owner reviews it and merges it.

## Rules

- **One notebook per person.** Only edit your own file. If you need a change in someone else's work, ask them or comment on the pull request.
- **Never commit directly to `main`.** Always use your own branch.
- **Update before you start.** Pull the latest `main` before creating your branch.
- **Do not edit the data file.** It is fixed. If you think it has a problem, tell the group.
- **Do not commit `.venv`, `.idea`, or `*.egg-info`.** If any of these show up in the Commit panel, untick them and tell the repo owner.
- **Shared code goes in `src/mqf_hw1/`.** If a helper is needed by several questions, add it there as a `.py` file and import it in the notebooks. Tell the group first.

## Needing an extra library

If your question needs a package that is not installed (for example `numpy` or `scipy`):

1. Tell the group so two people do not edit the same file at once.
2. Add the package name to the `dependencies` list in `pyproject.toml`.
3. Run `pip install -e ".[dev]"` again.
4. Commit `pyproject.toml` with your notebook. Everyone else re-runs the install command after they update.

## Final submission (repo owner)

1. Merge all pull requests and update `main`.
2. Combine the notebooks in question order:
```
   pip install nbmerge
   nbmerge notebooks/q1.ipynb notebooks/q2.ipynb notebooks/q3.ipynb > notebooks/HW1_final.ipynb
```
   If `nbmerge` causes trouble, create an empty `HW1_final.ipynb` and copy the cells over in order.
3. Open `HW1_final.ipynb`, delete the duplicate data-loading cells so only one remains at the top, and check that the question headings run in order.
4. Restart the kernel and run all cells, so every table and chart shows its output.
5. Export to PDF if the assignment asks for it, then submit as required.

## Troubleshooting

- **`ModuleNotFoundError: mqf_hw1`:** run `pip install -e ".[dev]"` in the Terminal with `(.venv)` showing, then restart the notebook kernel.
- **`ModuleNotFoundError` for another package:** see "Needing an extra library".
- **`pip install` says no `pyproject.toml` found:** run `ls -la` and check the file name. It must be exactly `pyproject.toml`, with no extra characters.
- **`FileNotFoundError` when loading data:** make sure you updated `main` so the `data` folder is up to date.
- **Push rejected:** update from `main` first, then push again.