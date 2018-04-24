# serverless-numpy
serverless numpy


serverless invoke local -f numpy --data '{"a":15,"b":5,"c":3}' --log
serverless deploy
serverless invoke -f numpy --data '{"a":15,"b":5,"c":3}' --log
serverless remove



