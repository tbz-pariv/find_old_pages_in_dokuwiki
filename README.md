# Find old pages in DokuWiki

## Goal

You want to see all old pages of a particular wiki user? This tool is for you.

## More precise

What means old? You can specify this in the unit "months".

What means "of a particular user"? You need to supply a user name.
All pages where the user did more than given percentage of changes.
See parameter "--percent".

## Why?

You want to clean up the wiki. 


## Usage

```
usage: find_old_pages_in_dokuwiki [-h] [--min_age MIN_AGE] [--percent PERCENT]
                                  [--output_template OUTPUT_TEMPLATE]
                                  meta_directory user_name

find old pages in dokuwiki

positional arguments:
  meta_directory        Path name of meta-directory. Example:
                        /srv/www/vhosts/example.com/dokuwiki/data/meta
  user_name             Find old pages of this user.

optional arguments:
  -h, --help            show this help message and exit
  --min_age MIN_AGE     Unit months. 12 means the articles should be unchanged
                        since one year.
  --percent PERCENT     90 means most of the changes are from the given user.
  --output_template OUTPUT_TEMPLATE
```

## Output

The output is pure text with one line per page and an URL.

Since modern terminals/IDEs let you click on the URL you have an ready to use list for your Subbotnik.

## Install

Directly via github. Not on pypi up to now.

```
pip install -e git+https://github.com/tbz-pariv/find_old_pages_in_dokuwiki.git#egg=find_old_pages_in_dokuwiki
```

