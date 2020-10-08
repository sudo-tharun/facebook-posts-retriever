import json
from translate import Translator
from datetime import datetime
import docx
doc=docx.Document()
da = json.load(open("your_posts.json"))
i=0
s=datetime(2019,12,22,00,00,00)
for i in range(len(da)):
    try:
        timestamp = da[i]['timestamp']
        dt = datetime.fromtimestamp(timestamp)
        if dt>s:
            k=da[i]['data'][0]['post']
            k = k.encode('latin-1').decode('unicode_escape').encode('latin-1').decode('utf-8')
            doc.add_heading(str(dt))
            doc.add_paragraph(k)
    except:
        pass
doc.save("FBPostsRetrieve.docx")


