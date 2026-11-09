---
title: "Strava - As Experience Vehicle - Data and UI"
date: "2017-06-23"
excerpt: "We continue to capture more and more data and we process this data as fast as the firehose (see Kinesis) can accept. One platform that continues to aggregate the data that fuels the future of augmente"
categories: ["Data", "DevOps", "performance", "Technology"]
tags: ["augmented", "strava"]
featured: false
---


# Strava &#8211; As Experience Vehicle &#8211; Data and UI

We continue to capture more and more data and we process this data as fast as the firehose (see Kinesis) can accept. One platform that continues to aggregate the data that fuels the future of augmented reality (AR) is **[Strava](http://www.strava.com)**.

As brief background, Strava is a platform built around athletes and their recorded events whether outdoor or inside [Zwift](http://www.zwift.com) and [Peloton Cycle](https://www.pelotoncycle.com/) . They have recently added new leadership members (James Quarles as CEO, formerly at Instagram) and have constantly been innovating their platform by utilizing rich APIs. Their experience platform that they are building is establishing a community of authentic experiences based around devices. (Apple, Garmin,etc).

Let's very quickly dive into the Strava's API to see the data points it delivers for athletes.

 "name": "The Math of Emotion", "distance": 60662, "moving_time": 11797, "elapsed_time": 15262, "total_elevation_gain": 1143, "type": "Ride", "achievement_count": 6, "kudos_count": 65, "comment_count": 5, "athlete_count": 2, 

Then let's match this up with a summary of Strava's visual manifestation.

![](http://52.12.181.38/wp-content/uploads/2017/06/Screen-Shot-2017-06-22-at-11.49.35-AM-1024x667.png)

**Add let's not forget Relive.cc .**

 

The richness of visual representation of the data cannot be underestimated yet that richness is deeply connected to the core data engineering infrastructure and the API interface to drive its presentation.

Like microservices ([Great Amazon book by Sam Newman](https://www.amazon.com/Building-Microservices-Designing-Fine-Grained-Systems/dp/1491950358?SubscriptionId=AKIAILSHYYTFIVPWUY6Q&#038;tag=duckduckgo-d-20&#038;linkCode=xm2&#038;camp=2025&#038;creative=165953&#038;creativeASIN=1491950358)) , the decoupling both data and interface teams in a microservices architecture "pizza" size team provides speed and flexibility.

Lastly, there's a great ARKIT demo from Adam Debreczeni‏ utilizing Unity + ARKit + Mapbox + Strava that shows the future of data and interface leveraging the Strava API.

**Deep Visual-Data Rich Experience.**

![](http://52.12.181.38/wp-content/uploads/2017/06/Screen-Shot-2017-06-20-at-7.04.13-AM-1004x1024.png)

Would love to hear about your data tool mashups (D3, etc) and the role that interface is playing in building the future experiences.

**[@benmorris](http://www.twitter.com/benmorris)**

