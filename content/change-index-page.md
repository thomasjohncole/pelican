Title: How to Change the Pelican Index Page
Date: 2019-06-06
Category: Pelican
Modified: 2019-06-04
Tags: Pelican
Slug: change-index-page
Author: Thomas Cole
Summary: How to change the landing page on a pelican static site.

[Pelican](http://getpelican.com "Pelican Development Blog") is a static site generator written in Python. It is used by many as a blogging tool, and the default setup is an index or landing page which shows the most recent blog articles in reverse chronological order, similar to the default for Wordpress.

I wanted to have some fun making a landing page for my site, so I didn't want the blog to be the index.html page - the first thing people see. I still wanted to keep the blog index page though, but serve it at a different URL like blog.html, and make it accesible as a navigation menu link.

Pelican takes data from its configuration files, content files, and template files, and converts it all to a group of static HTML files, which are stored by default in the output directory. One option with Pelican is to use [markdown](https://en.wikipedia.org/wiki/Markdown "Markdown Wikipedia page") files to create content, which is what I'm using for my site.

## Change the URL of the default index page
I changed the URL of the default index page by adding one line to the ```pelicanconf.py``` file:
```python
INDEX_SAVE_AS = 'blog.html'
```
Now Pelican will save that file with the new name when it builds the site.

## Assign index.html to my custom home page
To tell Pelican that I want my custom home page to be the new index, I add some information to the metadata of my home.md file:
```md
Title: Home
save_as: index.html
```
## Define the navigation menu links
I've created some other static pages in addition to the home page. I want these to show up on the navigation menu in a specific order with a specific URL. Pelican by default expects any static pages you create to go in a directory named ```pages```. If you define ```DISPLAY_PAGES_ON_MENU = True``` setting in the ```pelicanconf.py``` file, Pelican will take the files in your ```/pages```  folder, and display them in the navigation menu in alphabetical order. It will also keep the ```/pages``` path as part of the URL. For instance, if you define a ```contact.md``` file in your ```/pages``` directory, Pelican will add ```contact.html``` to your navigation menu, with a URL of ```SITEURL/pages/contact.html```

To change the order and the URLs of the navigation links I did two things. First, I defined the URLs for pages in the ```pelicanconf.py`` so they don't include the full path:
```python
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
```
I then added the ```slug``` parameter to the metadata of my pages. Here is an example of the metadata for the contact.md page:
```md
Title: Contact
slug: contact
```
Now the URL and file name for the contact page will take on the value of the slug from the metadata, so the URL will now be ```SITEURL/contact.html```

Finally I specified the links and associated URLs I wanted in the navigation menu:
```python
MENUITEMS = (
    ('Home', '/'),
    ('About', '/about-me.html'),
    ('Projects', '/projects.html'),
    ('Blog', '/blog.html'),
    ('Contact', '/contact.html' )
    )
```
In order for this to work properly make sure that ```DISPLAY_PAGES_ON_MENU``` is set to false.

## Conclusion
Pelican is a very flexible tool, and with a few changes to my configuration and page metadata I now have a site with a custom landing page, a custom navigation menu, and much cleaner URLs for my content pages. Here are all the changes to ```pelicanconf.py``` discussed in this article in one code block for easy reference:
```python
# save default index page as blog.html
INDEX_SAVE_AS = 'blog.html'
# define shorter filename and URL for content pages
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}.html'
# define custom navigation menu
DISPLAY_PAGES_ON_MENU = False
MENUITEMS = (
    ('Home', '/'),
    ('About', '/about-me.html'),
    ('Projects', '/projects.html'),
    ('Blog', '/blog.html'),
    ('Contact', '/contact.html' )
    )
```




