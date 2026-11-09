---
title: "Encrypted Email &#8211; Enigmail for Thunderbird"
slug: "encrypted-email-enigmail-for-thunderbird"
date: "2016-05-31T16:41:19"
original_url: "https://www.benmorristech.com/encrypted-email-enigmail-for-thunderbird/"
categories: ["Technology"]
tags: ["security"]
featured_media_id: 1207
excerpt: "I recently came across a great tool for working with Encrypted email. Thunderbird is a great free email client for OS X and Windows Enigmail is a free plug-in for Thunderbird that allows for sending and receiving encrypted email messages. You can also sign emails. https://enigmail.net/index.php/en/ Once downloaded and installed you need to also install GnuPG tools: \"The first and ..."
---

# Encrypted Email &#8211; Enigmail for Thunderbird

[![EnigMail](http://54.214.102.151/wp-content/uploads/2016/05/Screen-Shot-2016-05-31-at-9.40.06-AM.png)](http://54.214.102.151/wp-content/uploads/2016/05/Screen-Shot-2016-05-31-at-9.40.06-AM.png)

I recently came across a great tool for working with Encrypted email.

Thunderbird is a great free email client for OS X and Windows

Enigmail is a free plug-in for Thunderbird that allows for sending and receiving encrypted email messages. You can also sign emails. 

https://enigmail.net/index.php/en/

Once downloaded and installed you need to also install GnuPG tools:

[![GNuPG](http://54.214.102.151/wp-content/uploads/2016/05/GNuPG-1024x756.png)](http://54.214.102.151/wp-content/uploads/2016/05/GNuPG.png)

"The first and most popular option is to use the MacGPG package by

gpgtools.org. They provide pre-built binaries of GnuPG 2.0.22 and later for

users running OS X 10.6 (Snow Leopard) or later. Download the GPG-Suite

from https://gpgtools.org/gpgsuite.html and install it. If you don't

want to use the other components (Certificate Manager, Apple-Mail plugin and

Services application), you can deselect them during the installation process.

Only the MacGPG component is required for Enigmail."

[![Creating Public and Private Keys](http://54.214.102.151/wp-content/uploads/2016/05/Creating-Keys-1024x318.png)](http://54.214.102.151/wp-content/uploads/2016/05/Creating-Keys.png)

Sharing your Public Key (don't share Private)

https://enigmail.wiki/Key_Management#Share_your_public_key_manually

"Share your public key manually

On the Key Management window, select your key pair and click on File → Export Keys to File. Again, you will be asked whether you want to include your secret key in the saved OpenPGP key file: make sure you click on Export Public Keys Only this time. Save the ASC file, which will have a name like Firstname_Lastname_you@domain.com_(0x89ABCDEF)_pub.asc.

This is a copy of your public key; notice the "pub" word at the end of the filename. You can now put the file on your website for people to download it, or carry it around in a USB drive to distribute it to people, or send it via email as an attachment.

Concerning this last option, there is a simple Enigmail shortcut for it: when writing your mail in the Message Composition window, simply click on Attach My Public Key or choose from the menu bar Enigmail → Attach My Public Key and Enigmail will attach it upon sending."
