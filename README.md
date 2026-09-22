CAS Introduction 2026 — Longitudinal Hands-On
================================

:::info
**TL;DR**

1. **Setup:** follow the [Setup Quick Start](https://github.com/cerncas/hands-on-python/blob/main/Setup_QuickStart.md) of the transverse hands-on, if not already done. Nothing more to install.
2. **Download** the longitudinal exercises next to the transverse ones, from the terminal (**Miniforge Prompt** on Windows):

   ```bash
   cd ~/Documents
   git clone https://github.com/cerncas/hands-on-longitudinal-exercises.git
   ```

   No `git`? Download the [ZIP](https://github.com/cerncas/hands-on-longitudinal-exercises/archive/refs/heads/main.zip) and unpack it in your `Documents` folder.
3. **Open the notebooks** in JupyterLab, exactly as for the transverse ones.

:::

# What we will do

Two hands-on sessions on longitudinal beam dynamics, in **Python**, in a **Jupyter notebook**, on **your own laptop**:

| Session | Indico page | Notebook |
| --- | --- | --- |
| RF system calculations | [Hands-ON calculations (longitudinal) - Intro](https://indico.cern.ch/event/1622828/contributions/7202974/) | `01_LongitudinalHandsOnRFSystemCalculations_A_HadronSynchrotron.ipynb` **or** `01_LongitudinalHandsOnRFSystemCalculations_B_ElectronStorageRing.ipynb`, choose according to your interest |
| Longitudinal tracking | [Hands-ON calculations (longitudinal) - III](https://indico.cern.ch/event/1622828/contributions/7202999/) | `02_LongitudinalHandsOnTracking.ipynb`, where you write a tracking code, **or** `02_LongitudinalHandsOnTrackingAnimations.ipynb`, where the code is given and you only change input parameters and watch animations |

In the notebooks, the functions to complete are marked `# FILL`, and the other cells give you the first variables and a few hints as comments: the rest is yours. The **solutions** are given at the same time, in the `solutions` folder: use them whenever you are stuck, or to check your result. They come **without outputs**, run them on your laptop to see the results. A printable **PDF** of the solutions with all outputs is attached to the Indico pages.

The `cheat_sheet` folder contains the **longitudinal formulas** used during the sessions and a short **Python example** notebook. The slides are on the Indico pages.

The notebooks use only `numpy`, `scipy` and `matplotlib`, which are already in the `cas` environment of the transverse setup.

# 1. Setup

Same laptop, same setup as the transverse hands-on: the [Setup Quick Start](https://github.com/cerncas/hands-on-python/blob/main/Setup_QuickStart.md) gets you from an empty laptop to a running notebook in about 20 minutes. If you did it already, there is nothing more to install.

The full [Setup Instructions](https://github.com/cerncas/hands-on-python/blob/main/Setup_Instructions.md) are the reference if you want other ways to install, more troubleshooting, or an introduction to Python.

# 2. Download the material

Same as Step 3 of the Quick Start, with the longitudinal repository. Open a terminal (**Miniforge Prompt** on Windows) and run:

```bash
cd ~/Documents
git clone https://github.com/cerncas/hands-on-longitudinal-exercises.git
```

On Windows, the first line is `cd %USERPROFILE%\Documents`.

You now have a folder `hands-on-longitudinal-exercises` next to `hands-on-lattice-exercises`, containing the notebooks, the solutions and the cheat sheets.

> 🎬 **GIF 1:** terminal, the two commands, the new folder appearing in the file explorer next to the transverse one.

No `git`? Either `conda install -c conda-forge git`, or download the [ZIP](https://github.com/cerncas/hands-on-longitudinal-exercises/archive/refs/heads/main.zip), unpack it in your `Documents` folder, and rename the unpacked folder to `hands-on-longitudinal-exercises`.

> 🎬 **GIF 2 (optional):** download the ZIP from GitHub, unpack it in Documents, rename the folder.

**Updates.** If we announce a new version of the material during the school, run in the course folder:

```bash
git pull
```

Your own modified notebooks are not overwritten: if `git pull` complains about them, rename your copies first. Without `git`, download the ZIP again and unpack it next to the old folder.

# 3. Open the notebooks

Exactly as for the transverse hands-on, from the longitudinal folder this time:

```bash
conda activate cas
cd ~/Documents/hands-on-longitudinal-exercises
jupyter lab
```

Your browser opens on JupyterLab listing the notebooks. Double-click the notebook of the session.

> 🎬 **GIF 3:** terminal with the three commands, JupyterLab opening, double-click on the `02_` notebook.

# 4. Check that it works

Run the first cell of a notebook (`Shift`+`Enter`). It only contains imports and should print nothing. If it does, you are ready.

For the tracking session, you can also open `02_LongitudinalHandsOnTrackingAnimations.ipynb` and run it entirely (*Run → Run All Cells*): after a short while you should get a small movie with a play button.

> 🎬 **GIF 4 or screenshot:** the animations notebook with an animation and its play button.

:::success
**You are set. See you at CAS!**
:::

# Troubleshooting

- **`git: command not found`.** Install it with `conda install -c conda-forge git` (any environment), or use the ZIP.
- **JupyterLab does not show the longitudinal notebooks.** JupyterLab only shows the folder it was started in: stop it (`Ctrl`+`C` twice), `cd` to the longitudinal folder, and start it again. Alternatively start it from `Documents` to see both hands-on folders.
- **`ModuleNotFoundError: No module named 'support_functions'`.** The tracking notebook must stay in the folder where `support_functions.py` is. Do not move or copy it elsewhere; if you did, put it back and restart the kernel (*Kernel → Restart Kernel*).
- **`ModuleNotFoundError` for numpy, scipy or matplotlib.** JupyterLab is not running in the `cas` environment. Stop it, run `conda activate cas`, then `jupyter lab` again.
- **The animation shows as a wall of text, or nothing.** Run the cell again; the animation must be produced by the last line of the cell. Reloading the browser page also helps.
- **Anything about conda, the terminal or the installation.** See the [Setup Instructions](https://github.com/cerncas/hands-on-python/blob/main/Setup_Instructions.md#troubleshooting), which cover many more cases.

Still stuck? Come to the school anyway and find a tutor before the first session, with the complete error message.

# If you are new to Python

A basic knowledge is enough: variables, lists, `for` loops, functions, and numpy arrays. The notebook `cheat_sheet/PythonExample.ipynb` covers everything used in the hands-on; go through it if you want to warm up.

For more, see the introduction to Python in the [Setup Instructions](https://github.com/cerncas/hands-on-python/blob/main/Setup_Instructions.md#a-very-short-introduction-to-python).
