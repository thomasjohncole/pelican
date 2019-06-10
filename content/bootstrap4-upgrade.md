Title: Upgrade Pelican Theme to Bootstrap 4
Date: 2019-06-07
Category: Pelican
Modified: 2019-06-04
Tags: Pelican
Slug: boostrap-4-upgrade
Author: Thomas Cole
Summary: Upgrading the template to use Bootstrap 4

## Done so far

* changed column classes to col-9 and col-3
* updated navbar collapse to 768px (md)
* restyled collapse list items
* added sticky-top to nav (will hide for one with less height)
* change .well to .card in sidebar
* removed card inline styles, restyled cards
* elmininate DISPLAY_PAGES from base template (probably not to standard)
* add top margin to headers 1-3
* fixed layout of pagination.html, added custom color
* changed 'read more' button layout, changed class
* added solarized-dark pygments theme for code block
* fixed CSS boxes for code blocks
* fixed sidebar should bump down below content at 768px
* added style to `code` tags to override bootstrap

## Still To Do

* make cool landing page for index.html
* Add favicon.ico
* add content to pages
* write another blog post about the book "Deep Work"
* get rid of author stuff, remove dead links
* deploy to gihub-pages