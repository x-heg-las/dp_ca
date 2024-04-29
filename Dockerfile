FROM ubuntu:22.04

# Install OpenSSL
RUN apt-get update && apt-get install -y openssh-server nano git


# Genrerate ssh keys
RUN mkdir /var/run/sshd && \
    echo "root:password" | chpasswd 

  
RUN useradd -m -p $(openssl passwd -1 ca_password) ca
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd


# Create and set mount volume
WORKDIR /scheduler-certs
VOLUME  /scheduler-certs



EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]

