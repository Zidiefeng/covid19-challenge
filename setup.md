# Setup

1. Start instance and connect with service 
`cd` where stored `.pem` key-value pair
```
ssh -L localhost:8888:localhost:8888 -i key.pem ubuntu@public_dns_name
jupyter notebook
```

2. git clone repo
```
git clone https://github.com/Zidiefeng/covid19-challenge.git
```

3. create user/name/.kaggle and upload the json file to .kaggle
```
cd
mkdir .kaggle
```

4. Download and unzip data
```
cd 
cd covid19-challenge
mkdir data
cd data
kaggle datasets download -d allen-institute-for-ai/CORD-19-research-challenge
unzip 
```
