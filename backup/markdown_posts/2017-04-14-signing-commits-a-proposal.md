---
title: "Signing Commits &#8211; A Proposal."
slug: "signing-commits-a-proposal"
date: "2017-04-14T18:56:10"
original_url: "https://www.benmorristech.com/signing-commits-a-proposal/"
categories: ["Business", "DevOps", "Programming", "Security", "Technology"]
tags: []
featured_media_id: 1323
excerpt: "You step up to the counter. You're thirsty and just want your drink. The cashier asks you to pay and you use your credit card. A piece of paper pops out and they ask you to sign the transaction? Why do they need that? The argument goes that some verification is needed from you that you authorized the transaction. But ..."
---

# Signing Commits &#8211; A Proposal.

You step up to the counter. You're thirsty and just want your drink. The cashier asks you to pay and you use your credit card. A piece of paper pops out and they ask you to sign the transaction? Why do they need that? The argument goes that some verification is needed from you that you authorized the transaction. 

But in this increasingly fast paced world, do we care about signing transactions? What about when it comes to code commits to Git? This post was in part inspired by a post:

[Git Horror Story](https://mikegerwitz.com/papers/git-horror-story.html)

If you do a survey of Github repositories and commits, you’ll see that a large number of them don’t have signed commits? Why is this? 

**Example of not signing commits.** 

![](http://52.12.181.38/wp-content/uploads/2017/04/Commits-not-verified-1024x550.png)

**Example of usage of signed commits. **

![](http://52.12.181.38/wp-content/uploads/2017/04/Screen-Shot-2017-04-13-at-1.38.19-PM-1024x456.png)

Is this a symptom of too fast CI/CD? Is creating a GPG secret/public key too difficult? If so, here’s a quick guide to the process of generating GPG keys. This effort has value beyond Github commits with many digital secure transactions requiring some sort of signature and you can use your GPG key. 

https://help.github.com/articles/generating-a-new-gpg-key/

In addition, one possible SOLUTION is a feature request to Git hosting providers that they introduce a feature that would allow for the “requirement” for ONLY verified commits to a particular repository from committers that have uploaded their public keys. 

I understand this might introduce friction to the pipeline and prevent otherwise strong valuable committers, but at least the option would be there for certain repositories. 

 Would love to hear your feedback.

@benmorris
