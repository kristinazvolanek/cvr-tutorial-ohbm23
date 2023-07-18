# Material for the OHBM 2023 Educational Course Tutorial, "One person's noise is another person's signal: hands-on tutorial to model cerebrovascular reactivity in BOLD fMRI data"

This repository contains the example code to follow along with the OHBM 2023 Educational Course Tutorial _One person's noise is another person's signal: hands-on tutorial to model cerebrovascular reactivity in BOLD fMRI data_, part of the Educational Course [_Physiologic fMRI signals: friend or foe? How and why to measure, model, and account for physiology_](https://ww6.aievolution.com/hbm2301/index.cfm?do=ev.viewEv&ev=1241). See [here](https://physiopy.github.io/ohbm23_tutorials/) for the other tutorials in the same Educational Course.

Thank you to Stefano Moia for preparing these instructions! If you followed along with his tutorial in this course (see [here](https://github.com/smoia/ohbm2023noisetutorial/tree/master)), you will only need to install `phys2cvr`.

**Note that building wxPython may take 30-45 minutes depending on your system, so plan accordingly!**

# Laptop setup

To follow this tutorial, you will need a laptop, requiring a little bit of setup beforehand.

## 0. Prerequisites
You will need a laptop with python installed, as well as `pip`. Python version should be 3.7 or above.
You also need to download the files in this repository, either [zipped in a package](https://github.com/kristinazvolanek/cvr-tutorial-ohbm23/archive/refs/heads/main.zip) or by locally cloning the repository.

## 1. Optional - Set up a virtual environment
The best way to ensure the software functioning without changing anything in your system is using a virtual environment.
For that, first install `virtualenv`:

``` shell
pip install -U virtualenv
```
(Note you might need to use `pip3` instead of `pip`, depending on your OS and setup, to work with python 3)

Then, create and activate the virtual environment - in this case I called it _ohbm23cvr_, but you can use a different name:

``` shell
virtualenv ohbm23cvr
source ohbm23cvr/bin/activate
``` 

Note that the first command above will create a folder where you called it from, and the second command assumes this is the case - if you want you can specify a different path though.

Once you activated the virtual environment, you can proceed with package installation

## 2. Package installation

You will need to install a few python packages. First and foremost, [_wxPython_](). Its installation depends on the OS you are using.
While you can find [detailed instructions here](https://wxpython.org/pages/downloads/), following is the summary.

### Install _wxPython_ on Windows and macOS  
**This might take awhile!! (~30-45 minutes)**
``` shell
pip install -U wxPython
```
(Note you might need to use `pip3` instead of `pip`, depending on your OS and setup, to work with python 3)

### Install _wxPython_ on Linux  
**This might take awhile!! (~30-45 minutes)**
Check [this folder](https://extras.wxpython.org/wxPython4/extras/linux/) for the right python package, depending on the version of GTK you are using, as well as your OS, then using the link to the right folder, install _wxPython_ version _4.2.0_, if possible.
In this example, I will assume we're working with GTK3 on Ubuntu 20.04:
``` shell
pip install -U \
    -f https://extras.wxpython.org/wxPython4/extras/linux/gtk3/ubuntu-20.04 \
    wxPython==4.2.0
```
(Note you might need to use `pip3` instead of `pip`, depending on your OS and setup, to work with python 3)

### Install all other packages
You also need to install `peakdet` and `phys2cvr`. Optionally, you can also install `ipython`, a nice CLI environment to work with python.

The fastest option is to use the _requirements.txt_ file in this repository:
``` shell
pip install -U -r path/to/requirements.txt
```
(Note you might need to use `pip3` instead of `pip`, depending on your OS and setup, to work with python 3)

Alternatively, you can install directly what you need. Please ensure to install matplotlib version 3.6.3 or below, otherwise you will incur a deprecation error:
``` shell
pip install -U peakdet phys2cvr matplotlib==3.6.3 ipython
```
(Note you might need to use `pip3` instead of `pip`, depending on your OS and setup, to work with python 3)

## 3. Check the installation
Within the virtual environment, you can either call _pip_ to list your packages (`pip list` or `pip3 list`), or open _ipython_ and import `peakdet` and `phys2cvr`
```python
import peakdet
import phys2cvr
```

If you have no issues doing that, you're all good to go!

**Note that peakdet's GUI might not work in GUI-like environments like Jupyter notebooks or Spyder**

## 4. Download files for the tutorial

You can downlaod some files that contain data for the tutorial - we will be using these files during the live tutorial.

All the files can be downloaded in a zip folder [here](https://files.de-1.osf.io/v1/resources/3txqr/providers/osfstorage/64a2071867aff81111edfe26/?zip=). 

This folder includes [BOLD fMRI data](https://osf.io/3txqr/files/osfstorage/64a2055138091110953c3347), associated [physiological data](https://osf.io/3txqr/files/osfstorage/64a2045ca2a2f4115443670b) including CO2, [motion parameters](https://osf.io/3txqr/files/osfstorage/64a20459a2a2f411544366ff), [brain mask](https://osf.io/3txqr/files/osfstorage/64a2045738091110953c32fa), and [gray matter mask](https://osf.io/3txqr/files/osfstorage/64a204576513ba100d3a3bfe).
