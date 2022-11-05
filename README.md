# Italki teachers

Scrape all italki teachers for Chinese and start a datasette instance for 
searching.

## Dependencies

```bash
$ pip install -r requirements.txt
```

Make sure you have `jq` installed:

```bash
$ brew install jq
```

## Create the database

```bash
$ cat pages/* | jq '.data[] | (.teacher_info + .user_info)' | jq -s | sqlite-utils insert db.sqlite teachers -
```

## Enable full text search
```bash
$ sqlite-utils enable-fts db.sqlite teachers intro nickname
```

## Start server
```bash
$ datasette db.sqlite
```


## Link to SQL query for searching

[Click here](http://localhost:8001/db?sql=select%0D%0A++%27https%3A%2F%2Fwww.italki.com%2Fteacher%2F%27+%7C%7C+user_id+%7C%7C+%27%2Fchinese%27+nickname%2C%0D%0A++intro%2C%0D%0A++first_valid_time%2C%0D%0A++session_count%2C%0D%0A++overall_rating%2C%0D%0A++qiniu_video_url%2C%0D%0A++is_new%2C%0D%0A++user_id%0D%0Afrom%0D%0A++teachers%0D%0Awhere%0D%0A++rowid+in+%28%0D%0A++++select%0D%0A++++++rowid%0D%0A++++from%0D%0A++++++teachers_fts%0D%0A++++where%0D%0A++++++teachers_fts+match+escape_fts%28%3Asearch%29%0D%0A++%29%0D%0Aorder+by%0D%0A++rowid%0D%0Alimit%0D%0A++101&search=business)


## A few impressive teachers
- [Liang, very fluent english](https://www.italki.com/teacher/7016816/chinese)
