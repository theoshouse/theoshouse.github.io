---
title: Blog
permalink: /blog/
---

# Blog

{% for post in site.posts %}
<div class="post-item">
  <a class="post-link" href="{{ post.url | relative_url }}">{{ post.title }}</a>
  <span class="post-date">{{ post.date | date: "%B %-d, %Y" }}</span>
  {% if post.description %}<p>{{ post.description }}</p>{% endif %}
</div>
{% endfor %}

## Get new posts by email

My posts also go out on Substack. [Subscribe by email]({{ site.substack_url }}/subscribe) to get them in your inbox.
