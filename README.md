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

Command run:

```
git rm -r css/[bfmn]* fonts/ js/vendor/
```

## Step 3: Add MDB Files

Add files from the `static` directory of the `groja.com-mdb` repo to the `Site/content/static` directory.

### Notes


