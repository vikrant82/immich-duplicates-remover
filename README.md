- Run the Duplicate Detection Job from Jobs page in Administration
    
- Copy the the value of immich_access_token from Cookies in your browser and put it [here](https://github.com/vikrant82/immich-duplicates-remover/blob/main/duplicates-remover.py#L11)
    
- Set the base URL [here](https://github.com/vikrant82/immich-duplicates-remover/blob/main/duplicates-remover.py#L5) without a *slash* at the end for e.g. *https://photos.yourdomain.com*
    
- Install dependencies
    
    - `pip3 install -r requirements.txt`
    - `python3 duplicates-remover.py`
- Gotchas:
    
    - Use at your own risk, python is not my native language ;)
    - The script skips the videos duplicates as Immich flags videos duplicates based on first frame, which can often be black or white. So flip [this flag](https://github.com/vikrant82/immich-duplicates-remover/blob/main/duplicates-remover.py#L8) on your own risk
    - The script would select the image which maximum size among the duplicates. This seems to be the default behavior in the UX as well.
    - Also play around with Settings -> Machine Learning Settings -> Duplicate Detection -> Max Detection System to change criteria for duplicates detection.
