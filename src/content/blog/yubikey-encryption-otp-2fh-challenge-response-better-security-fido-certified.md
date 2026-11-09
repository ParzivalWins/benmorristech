---
title: "Yubikey - Encryption - OTP - 2FH - Challenge-Response - Better Security  - FIDO Certified"
date: "2017-03-14"
excerpt: "Recently, in order to take the security story further I purchased a Yubikey from http://www.yubico.com. My decision was prompted to use better security for all places that I use keys. 1. Laptop - Logi"
categories: ["Security", "Technology"]
tags: ["encryption", "security"]
featured: false
---


# Yubikey &#8211; Encryption &#8211; OTP &#8211; 2FH &#8211; Challenge-Response &#8211; Better Security  &#8211; FIDO Certified

Recently, in order to take the security story further I purchased a Yubikey from http://www.yubico.com. 

My decision was prompted to use better security for all places that I use keys.

1. Laptop - Login to Device (Challenge-Response)

2. Access to hosting provider (VULTR)

3. SSH access to systems (VPS, AWS)

4. Move away from Google Authenticator (2FH)

5. Laptop access to websites via password manager - LastPass

The Yubikey I decided on was the Yubikey Neo due to the fact that it had NFC capabilities for mobile device. Now this presents a problem for tablets like the Samsung S2 Tab that doesn't include NFC. Furthermore, Apple and its implementation of NFC haven't opened their NFC access. 

1. Laptop - Login to Device (Challenge-Response)

This is by far the most difficult and risky to setup. Highly recommend a backup of your laptop before you implement. 

2. Access to hosting provider (VULTR)

Vultr, IMHO, appears to be a good progressive web hosting provider that has resources in many markets and provides VPS services at a fair cost. They accept BTC too if you are interested in keeping with your modern payment strategies. They also have an option to require Yubikey for administrative console access. See below.

[![Vultr - Yubikey Access](http://54.214.102.151/wp-content/uploads/2016/07/Screen-Shot-2016-07-21-at-6.05.27-PM-1024x411.png)](http://54.214.102.151/wp-content/uploads/2016/07/Screen-Shot-2016-07-21-at-6.05.27-PM.png)

3. SSH access to systems (VPS, AWS) via GPG.

Make sure you have the Yubikey inserted.

Make sure you have PATH statement in place.

Initialize the YubiKey

echo "enable-ssh-support" >> ~/.gnupg/gpg-agent.conf

export SSH_AUTH_SOCK=~/.gnupg/S.gpg-agent.ssh

![](http://52.12.181.38/wp-content/uploads/2017/03/Screen-Shot-2017-03-13-at-7.02.24-PM-1024x423.png)

4. Move away from Google Authenticator (2FH)

Hardware key for Google.

![](http://52.12.181.38/wp-content/uploads/2017/03/Screen-Shot-2017-03-13-at-6.53.28-PM-1016x1024.png)

5. Laptop access to websites via password manager - LastPass 

Here's an example of the LastPass request on laptop when trying to unlock vault. [![Yubikey and LastPass](http://54.214.102.151/wp-content/uploads/2016/07/Screen-Shot-2016-07-21-at-12.21.32-PM-1024x469.png)](http://54.214.102.151/wp-content/uploads/2016/07/Screen-Shot-2016-07-21-at-12.21.32-PM.png)

