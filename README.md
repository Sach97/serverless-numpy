# serverless-numpy
A ready to deploy repo as explained in this [blog](https://serverless.com/blog/serverless-python-packaging/)

## Prerequesites

- Have node and npm installed. There is a good guide for installing node and npm on linux [here](https://github.com/creationix/nvm)
- Have python and pip installed. There is a good guide for installing python with conda [here](https://conda.io/docs/user-guide/install/linux.html)
- Make sure you have exported your AWS keys in your environmnet variables

## Install serverless framework

```
npm install -g serverless
```

## Getting started
```
git clone https://github.com/Sach97/serverless-numpy.git
cd serverless-numpy
source venv/bin/activate
pip install requirements.txt
npm install --save serverless-python-requirements
```

## Run locally

```
serverless invoke local -f numpy --data '{"a":15,"b":5,"c":3}' --log
```

## Deploy

```
serverless deploy
serverless invoke -f numpy --data '{"a":15,"b":5,"c":3}' --log
```

## Undeploy

```
serverless remove
```

## TODOs

- [ ] Add [CircleCI](https://serverless.com/blog/ci-cd-workflow-serverless-apps-with-circleci/) continuous integration badge and an explanation guide. 
- [ ] Add an AWS deployment button


