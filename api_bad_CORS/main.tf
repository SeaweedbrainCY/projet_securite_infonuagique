provider "aws" {
  region = "us-east-1"  
}

resource "aws_instance" "cors" {
  ami           = "ami-058bd2d568351da34"  
  instance_type = "t2.small"
  vpc_security_group_ids = ["sg-0e6cd799c1ee9a1d6"]
  key_name = "seaweedbrain"


  tags = {
    Name = "cors"
  }
}

resource "aws_instance" "ssrf" {
  ami           = "ami-058bd2d568351da34" 
  instance_type = "t2.small"
  vpc_security_group_ids = ["sg-0e6cd799c1ee9a1d6"]
  key_name = "seaweedbrain"

  tags = {
    Name = "ssrf"
  }
}


output "instance_public_ips" {
  value = aws_instance.cors.public_dns
}