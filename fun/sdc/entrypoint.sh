docker build -t csr . && docker run --rm -e CURRENCY=$1 -e THRESHOLD=$2 --name csr-1 csr
