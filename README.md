# Detection of age of a person using brain MRI scans


Collaborators: [Harry Jiang](https://github.com/jxx1998), [Zixian (Sunnie) Ma](https://github.com/zixianma) and [Prabhjot Singh Rai](https://github.com/raiprabh).


### Booting and shutting down the GPU instance

1. Visit AWS website [here](https://oreochip.signin.aws.amazon.com/console) and login via your IAM username and password.
2. Under find services, search `EC2`.
3. Click on `Running Instances`. You should see a dashboard with all the instances. We are interested in `p2.xlarge` (instance ID: `i-0d97a15182c8f6a45`). Select it and click on `Actions` in the top bar, then `Instance State` and then `Start` or `Stop`.

**VERY IMPORTANT: Please stop the instance after your work**

### SSH in the console

On the same EC2 page, when you have selected the particular instance, towards the bottom there is `Description` tab. Under this, you will find `Public DNS (IPv4)`. It should be something like `ec2-54-212-67-222.us-west-2.compute.amazonaws.com`(might change whenever we restart the instance). This is required to ssh and view the notebook on the web browser.

1. From your terminal, run the command `ssh USER@public-dns-ipv4`. For example `ssh prabhjot@ec2-54-212-67-222.us-west-2.compute.amazonaws.com`. You should be successfully logged in.
2. Run the command `passwd` if you are logging in for the first time to change VM password for your user.

#### First time setups

Since there are multiple users accessing the same machine and we want to share the already installed libraries (PyTorch, CUDA etc) among all of us, we would need to do some basic setup for the same.

##### Library path setup
1. `vim ~/.profile` to edit the profile for the user.
2. Append the following line after the last line in the file, then save and quit.
    ```
    export PATH=/home/ubuntu/anaconda3/envs/pytorch_p36/bin:/home/ubuntu/anaconda3/bin/:/home/ubuntu/bin:/home/ubuntu/.local/bin:/home/ubuntu/anaconda3/bin/:/usr/local/cuda/bin:/usr/local/bin:/opt/aws/bin:/usr/local/mpi/bin:/usr/local/cuda/bin:/usr/local/bin:/opt/aws/bin:/home/ubuntu/src/cntk/bin:/usr/local/mpi/bin:/usr/local/cuda/bin:/usr/local/bin:/opt/aws/bin:/usr/local/mpi/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:$PATH
    ```
3. `source ~/.profile` to restart the profile.

##### Jupyter notebook configuration setup
This is required to access the port directly on public IP of our instance.

1. At your home directory, run `jupyter notebook --generate-config`.
2. `vim ~/.jupyter/jupyter_notebook_config.py`
3. Append the following lines towards the end of the file, then save and quit.
    ```
    c.NotebookApp.kernel_spec_manager_class = 'environment_kernels.EnvironmentKernelSpecManager'
    c.NotebookApp.iopub_data_rate_limit = 10000000000
    c.NotebookApp.ip = '*'
    c.NotebookApp.open_browser = False
    ```
4. Finally, run the command `jupyter notebook password` to setup password for your notebook.
 

##### Github repository setup

Steps 1 and 2 describe the best way to setup github access to your VM user (via ssh). 

1. Let's begin with creating a new ssh key pair. Run the command `ssh-keygen -t rsa -C "YOUR_EMAIL_ADDRESS"` to create a new ssh keygen. Highly recommended to set a password when prompted for this key since three of us are sharing a single machine.
2. Add this new created ssh key to your Github Account. Replicate the steps 1 to 8 in [this](https://help.github.com/en/enterprise/2.15/user/articles/adding-a-new-ssh-key-to-your-github-account) article.
3. That's all! Now we are all set to clone the repository. In your home directory, `git clone git@github.com:raiprabh/brain-age.git` to clone the repository. You'll be asked your ssh key password you entered while creating your key.
4. If everything went great, you should see `brain-age` in your home directory.

 
### Running jupyter notebook

1. Make sure to activate the right virtual environment prior running the instance. Run the command `source /home/ubuntu/anaconda3/bin//activate pytorch_p36` to activate pytorch with CUDA python environment.
2. Change directory to root of project (`cd ~/brain-age`).
3. Run `jupyter notebook`. It should show the port on which the notebook is running (this might also change, since three of us may be working parallely on different ports).
4. In your web browser, open `public-dns-ipv4:PORT` to open up the jupyter notebook. For example `ec2-54-212-67-222.us-west-2.compute.amazonaws.com:8888`. Enter your notebook password when prompted.
5. Grab a coffee and start coding!

### Data

Please note that we shouldn't save the data in the home directory as our machine has only 3 gb left. Instead, move to `/shared` directory and download all the data there. Following are the datasets which have been already downloaded in the `/shared` directory

1. `ixi-dataset` (from [here](http://brain-development.org/ixi-dataset/))
2. `fcp` (from [here](http://fcon_1000.projects.nitrc.org/fcpClassic/FcpTable.html))


