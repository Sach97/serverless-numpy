# serverless-numpy
A ready to deploy repo explained in this [blog](https://serverless.com/blog/serverless-python-packaging/)

## Prerequesites

Make sure you have exported your AWS keys

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

## Testing locally

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



