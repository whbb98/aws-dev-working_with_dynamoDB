sudo yum -y remove python36
sudo yum -y install python38
sudo update-alternatives --set python /usr/bin/python3.8
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
rm awscliv2.zip
sudo pip install boto3