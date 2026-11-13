---
title: Podcasts
permalink: /podcasts/
---

# Podcasts

{% assign episodes = site.podcasts | sort: "date" | reverse %}
{% for episode in episodes %}
<section class="episode" id="{{ episode.slug }}">
  <h2>{{ episode.title }}</h2>
  <p class="post-date">{{ episode.date | date: "%B %-d, %Y" }}</p>
  {% if episode.description %}<p class="episode-description">{{ episode.description }}</p>{% endif %}
  {{ episode.content }}
</section>
{% endfor %}
