# seeourminds.com-mdb

Repo for converting the css for SeeOurMinds.com from Bootstrap 3.3.7 to Material Design Bootstrap (MDB).

# Initialization

## Step 1: Copy Files

Copy almost all files from the current seeourminds.com repo into this one.

### Notes

- Moving contents of `doc` directory to the `doc/seeourminds.com` directory in the `jmws_accoutrements` repo.
- Updated `bin/run.sh` to run on port 8002

## Step 2: Delete Bootstrap Files

Delete all Bootstrap 3.3.7 files under `Site/content/static`

### Notes

- Deleting all files under
  - `fonts`
  - `js/vendor`
- Deleting most files under css
  - **Not deleting** `README.md`
  - **Not deleting** `seeourminds.css`
- **Not deleting any files under:**
  - `images`
  - `json`
- **Not deleting these** specific files either:
  - `favicon.ico`
  - `js/score_bars.js`
  - `js/seeourminds.js`

Commands run:

```
gossmc
cd static/content/
git rm -r css/[bfmn]* fonts/ js/vendor/
```

## Step 3: Add MDB Files

Add files from the `static` directory of the `groja.com-mdb` repo to the `Site/content/static` directory.

- It may not be the latest version, but anything we do css-wise on one site should work just fine on the other as well.

### Notes

- Copying **all** files under:
  - `font/`
  - `img/`
  - `js/`
- Also copying:
  - `License-MDB.pdf`
  - `README-MDB.txt`
  - **All** files under `css/` **except** `groja.css` and `home.css`

Commands run:

```
gossmc
cd static/content/
l /var/www/groja.com/htdocs/groja.com-mdb/Site/static/
cp  /var/www/groja.com/htdocs/groja.com-mdb/Site/static/License-MDB.pdf  .
cp  /var/www/groja.com/htdocs/groja.com-mdb/Site/static/README-MDB.txt .
cp -r /var/www/groja.com/htdocs/groja.com-mdb/Site/static/font .
cp -r /var/www/groja.com/htdocs/groja.com-mdb/Site/static/img .
cp -r /var/www/groja.com/htdocs/groja.com-mdb/Site/static/js .
cd css
l /var/www/groja.com/htdocs/groja.com-mdb/Site/static/css/[Rabfm]*
cp -r /var/www/groja.com/htdocs/groja.com-mdb/Site/static/css/[Rabfm]* .
```

