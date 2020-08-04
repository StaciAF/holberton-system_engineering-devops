# 0x0B. SSH

### Learning Objectives

- What is a server
- Where servers usually live
- What is SSH
- How to create an SSH RSA key pair
- How to connect to a remote host using an SSH RSA key pair
- The advantage of using #!/usr/bin/env bash instead of /bin/bash

### Tasks

#### 0. Use a private key mandatory

Write a Bash script that uses ssh to connect to your server using the private key ~/.ssh/holberton with the user ubuntu.

Requirements:
- Only use ssh single-character flags
- You cannot use -l
- You do not need to handle the case of a private key protected by a passphrase


#### 1. Create an SSH key pair mandatory

Write a Bash script that creates an RSA key pair.

Requirements:

- Name of the created private key must be holberton
- Number of bits in the created key to be created 4096
- The created key must be protected by the passphrase betty


#### 2. Client configuration file mandatory

Your Ubuntu Vagrant machine has an SSH configuration file for the local SSH client, let’s configure it to our needs so that you can connect to a server without typing a password. Share your SSH client configuration in your answer file.


#### 3. Let me in! mandatory

Now that you have successfully connected to your server, we would also like to join the party.

Add the SSH public key below to your server so that we can connect using the ubuntu user.
