# 0x10. HTTPS SSL

### Learning Objectives

-What is HTTPS SSL 2 main roles
-What is the purpose encrypting traffic
-What SSL termination means

### Tasks

#### 0. HTTPS ABC
As for project 0x07, use numbers in your answer file.

#### 1. World wide web mandatory

Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.


#### 2. HAproxy SSL termination mandatory

“Terminating SSL on HAproxy” means that HAproxy is configured to handle encrypted traffic, unencrypt it and pass it on to its destination.

Create a certificate using certbot and configure HAproxy to accept encrypted traffic for your subdomain www..

#### 3. No loophole in your website traffic #advanced

A good habit is to enforce HTTPS traffic so that no unencrypted traffic is possible. Configure HAproxy to automatically redirect HTTP traffic to HTTPS.

