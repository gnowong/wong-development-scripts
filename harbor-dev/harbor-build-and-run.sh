openssl genpkey -algorithm ed25519 > localhost1.key
openssl req -x509 -new -key localhost1.key -out localhost1.crt
sudo ./prepare
sudo ./install