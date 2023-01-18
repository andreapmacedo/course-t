# ---docker ps

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ping / traceroute / iptables
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# ---docker run --privileged -it ubuntu:20.04 bash

# --- saber versão: cat /etc/*-release

# ---apt update && apt install iputils-ping traceroute iptables

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# $ ping google.com 
# $ ping google.com -c 4
# $ traceroute google.com
# $ localhost
# ptables -L
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ---Bloqueio ICMP  (bloquear placa de rede)

# iptables -A INPUT -p icmp --icmp-type echo-request -j DROP
# iptables -A INPUT -p icmp --icmp-type echo-request -j REJECT

# $ localhost (ver o que ocorre)

# ---Apagar regras

# iptables –F
# iptables -–flush

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# ---bloquei de portas

# iptables -A INPUT -p tcp --destination-port 8080 -j DROP
# iptables -A INPUT -p tcp --destination-port 80 -j REJECT
# pingar 80
# instalar telnet para validar: ---apt-get install telnet


# bloquear facebook:
# iptables -A OUTPUT -d IP -j REJECT

