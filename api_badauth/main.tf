provider "aws" {
  region = "us-east-1"  
}

resource "aws_instance" "jwt" {
  ami           = "ami-058bd2d568351da34"  
  instance_type = "t2.small"
  vpc_security_group_ids = ["sg-0362e7eabcc677a60"]
  key_name = "awskey"


  tags = {
    Name = "jwt"
  }
}

resource "aws_instance" "rce" {
  ami           = "ami-058bd2d568351da34" 
  instance_type = "t2.small"
  vpc_security_group_ids = ["sg-0362e7eabcc677a60"]
  key_name = "awskey"

  tags = {
    Name = "rce"
  }
}


output "instance_public_ips" {
  value = aws_instance.jwt.public_dns
}