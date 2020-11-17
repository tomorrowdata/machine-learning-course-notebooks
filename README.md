[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/tomorrowdata/machine-learning-course-notebooks.git/master)

# Jupyter Notebooks: Machine Learning
Notebooks for hands-on on machine learning supervised and unsupervised tasks.

## Notebook list

1. Hands-On 1: Python and Pandas Tutorial 
2. Hands-On 2: Unsupervised Learning
3. Hands-On 3: Supervised Learning
4. Hands-On 4: Model Selection

<hr>

## Setup Envornment on Windows

1. Get the Anaconda (Individual Edition) [here](https://www.anaconda.com/products/individual)

2. Install Anaconda on your machine. Pay attention when the installer asks for *Register Anaconda3 as my default Python 3.8*, untick it if you dont want to!

### Create Virtual Environment

   1. Open **Anaconda Navigator** and select *Environments* on the left side panel <br><br>![import-example](images/anaconda-new-env1.PNG)


4. Click *Import* and use the `environment.yml` as specification File. Use *mlenv* as name for the environment
   <br><br>![import-example](images/anaconda-new-env2.PNG)


1. Once installed, go to the *Home* panel and be sure the installed environment is selected <br><br>![import-example](images/anaconda-new-env3.PNG)
2. Launch jupyter notebook and navigate to the repository folder
3. Open the notebook you want to run

## Setup Environment on Linux

### Install miniconda

1. Download [miniconda](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86.sh) the miniconda linux installer
2. Follow instructions [here](https://conda.io/projects/conda/en/latest/user-guide/install/linux.html) for installing miniconda

### Create Virtual Environment

To set up the conda environment with the required packages and running the notebooks, execute the following command:

1. Create a new virtual environment:
`conda env create -n mlenv -f=./environment.yml`

1. Set up the environment:
`conda activate mlenv`

3. Run jupyter notebooks:
`jupyter notebook`

<hr>


# Licence

![the Creative Common BY-SA-4.0 licence](https://tomorrowdata.io/wp-content/uploads/2015/08/88x31.png)

Except where otherwise noted, all content of this **machine-learning-course-notebooks** repository are distributed under [the Creative Common BY-SA-4.0 licence](https://creativecommons.org/licenses/by-sa/4.0/)
