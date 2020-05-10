# AWS Deep Learning AMI instance

### [Get Started with Deep Learning Using the AWS Deep Learning AMI](https://aws.amazon.com/cn/blogs/machine-learning/get-started-with-deep-learning-using-the-aws-deep-learning-ami/)
1. Choose a DL AMI instance through EC2 console (AWS Deep Learning AMI (Ubuntu 18.04))
2. View product details for [price](https://aws.amazon.com/marketplace/pp/B07Y43P7X5)
3. Choose instance size
4. Launch with key pair downloaded

### [Connect from Windows using PuTTY/ other methods](https://docs.aws.amazon.com/quickstarts/latest/vmlaunch/step-2-connect-to-instance.html#browser)
1. Download and open PuTTY
2. Host Name, enter `ubuntu`@`public_dns_name`.
3. Connect type: SSH
4. Category-Connection, SSH, Auth -- Open .ppl key-pair file
5. Enter `ubuntu` terminal and enter `jupyter notebook`
6. Copy URL to browser and get started!

`*` terminal:
1. `cd download` (where .pem key-pair downloaded)
2. `ssh -L localhost:8888:localhost:8888 -i key.pem ubuntu@public_dns_name`
