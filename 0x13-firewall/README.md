UFW, or Uncomplicated Firewall, is an interface to iptables that is geared towards simplifying the process of configuring a firewall. While iptables is a solid and flexible tool, it can be difficult for beginners to learn how to use it to properly configure a firewall. If you’re looking to get started securing your network, and you’re not sure which tool to use, UFW may be the right choice for you
HTTP on port 80, which is what unencrypted web servers use, using sudo ufw allow http or sudo ufw allow 80
HTTPS on port 443, which is what encrypted web servers use, using sudo ufw allow https or sudo ufw allow 443
Apache with both HTTP and HTTPS, using sudo ufw allow ‘Apache Full’
Nginx with both HTTP and HTTPS, using sudo ufw allow ‘Nginx Full’

