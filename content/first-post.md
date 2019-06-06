Title: My First Real Post
Date: 2019-06-04
Category: General
Modified: 2019-06-04
Tags:
Slug: my-first-post
Author: Thomas Cole
Summary: This is the first Pelican blog post.

This is the first Pelican blog post. I am new to Pelican. I just switched over from Jekyll. Before that it was Wordpress.

I can't seem to see my changes in the browser. Perhaps it's caching?

I added this to the ```pelicanconf.py``` file:
```python
# disable cache to see changes
LOAD_CONTENT_CACHE = False
```
Okay not exactly sure what's going on here, because I just cleared the browser cache for the last 24 hours, and I still can't see the changes.

Just tried this:
```bash
tom@tbeaver:~/code-2019/pelican$ pelican --listen --ignore-cache
```
Still nothing. Nada. Manually delete the cache? Killed that. Still nothing. Moving along...

Okay I found out where the themes are, and by running this command you can see there are two of them:
```bash
(venv) tom@tbeaver:~/code-2019/pelican$ pelican-themes -l -v
/home/tom/code-2019/pelican/venv/lib/python3.6/site-packages/pelican/themes/simple
/home/tom/code-2019/pelican/venv/lib/python3.6/site-packages/pelican/themes/notmyidea
```
A quick look at the template tells me I am using 'notmyidea', but if I add a line to the ```pelicanconf.py``` file, still nothing changes:
```THEME = 'simple'```
It still looks the same. I'm missing something obvious here, it's serving from some cache that I haven't yet discovered and disabled/deleted. Okay from the command line I did ```pelican --r`` and the theme change took I think. But still no content update?

Okay now after switching the theme back to 'notmyidea' in the config, and doing another ```pelican --r``` followed by another ```pelican --listen``, it looks like everything is now showing up. Hmm...

Okay it looks like there is something I can use, using this command:
```bash
(venv) tom@tbeaver:~/code-2019/pelican$ pelican --listen --autoreload
  --- AutoReload Mode: Monitoring `content`, `theme` and `settings` for changes. ---

-> Modified: content, theme, settings. re-generating...
Done: Processed 1 article, 0 drafts, 0 pages, 0 hidden pages and 0 draft pages in 1.28 seconds.
```
Now I can see changes after a refresh, good enough for now.