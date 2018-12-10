# File Compression Python using LZW

---

### Requirements
- [virtualenv](https://virtualenv.pypa.io/en/latest/)



### Instructions
- install packages from `requirements.txt`

    `virtualenv --no-site-packages venv`

    `source venv/bin/activate`

    `pip install -r requirements.txt`


### Compressing a file

    `sudo python compress.py -c -l <file_path_here_of_.txt_file>`


    Sample with verbose elasped time and space savings:

    `sudo python compress.py -c -l -v ./sample.txt`


### Decompressing a file

    `sudo python compress.py -d <file_path_here_of_.lzw_file>`



### Options:
Should choose exactly one from "-c" and "-d"
* -c: Compress `file`. Should choose exactly one of the following options:
    * -l: Compress `file` using LZW
* -d: Decompress `file`
* -v: verbose output
