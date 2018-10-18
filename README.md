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

## Step 4: Add Files for the Fancy MDB Landing Page

### 2018-10-16

Decided to re-do the home page of this site to look like the example in the
`material_design/05-material_design_bootstrap/04-landing_page_freebie`
directory of the `always_learning_google_products` repo.

- This requires adding a few files downloaded from the site last night
  - These files are for use on the home page only
- See `material_design/05-material_design_bootstrap/README.md` for URLs
- Original version of the new home page is form.html

### Adding Files for the New Landing Page:

Adding these files to subdirectories of `static/content` :

```
css/style.css
css/style.min.css
```

