from pathlib import Path
import subprocess, textwrap, pty, select, os, time
from PIL import Image, ImageDraw, ImageFont

root=Path(__file__).resolve().parents[1]
assets=root/'assets'
exe=root/'build/music_assistant'

def session(steps):
    master,slave=pty.openpty()
    child=subprocess.Popen([str(exe)],stdin=slave,stdout=slave,stderr=slave)
    os.close(slave)
    data=''; cursor=0
    for prompt,entry in steps:
        deadline=time.monotonic()+4
        while prompt not in data[cursor:]:
            assert time.monotonic()<deadline, ('Missing prompt',prompt,data)
            ready,_,_=select.select([master],[],[],0.1)
            if ready: data+=os.read(master,65536).decode()
        cursor=data.index(prompt,cursor)+len(prompt)
        os.write(master,(entry+'\n').encode())
    while True:
        ready,_,_=select.select([master],[],[],0.1)
        if ready:
            try: block=os.read(master,65536)
            except OSError: break
            if not block: break
            data+=block.decode()
        elif child.poll() is not None: break
    os.close(master)
    assert child.wait(timeout=2)==0
    return data.replace('\r\n','\n').replace('\r','')

prompts=['Choose genre (1-3): ','Choose mood (1-3): ', 'Length: 1 Up to 4 min  2 Over 4 min: ','Find another? 1 Yes  2 No: ']
demo=session(list(zip(prompts,['2','1','2','1']))+list(zip(prompts,['1','3','1','2'])))
invalid=session([(prompts[0],'1abc'),(prompts[0],'1.5')]+list(zip(prompts,['1','3','1','2'])))
assets.joinpath('program_output.txt').write_text(demo)
assets.joinpath('invalid_output.txt').write_text(invalid)

def picture(text,name,size=22):
    font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf',size)
    lines=[]
    for line in text.expandtabs(4).splitlines():
        lines.extend(textwrap.wrap(line,80,replace_whitespace=False,drop_whitespace=False) or [''])
    lineheight=size+8; width=1120; height=52+lineheight*len(lines)
    im=Image.new('RGB',(width,height),'#172432');draw=ImageDraw.Draw(im)
    for i,line in enumerate(lines): draw.text((24,24+i*lineheight),line,font=font,fill='#F0F4F7')
    im.save(assets/name)

source=(root/'src/main.cpp').read_text().splitlines()
start=next(i for i,x in enumerate(source) if x.startswith('int readChoice'))
end=next(i for i,x in enumerate(source[start:],start) if x.startswith('int main'))
picture('\n'.join(f'{i+1:3}  {source[i]}' for i in range(start,end-1)), 'code_capture.png')
start=next(i for i,x in enumerate(source) if 'int bestScore' in x)
end=next(i for i,x in enumerate(source) if 'std::cout << "\\nRecommendation:' in x)
picture('\n'.join(f'{i+1:3}  {source[i]}' for i in range(start,end)), 'logic_capture.png')
picture(demo,'output_capture.png')
picture(invalid,'invalid_capture.png')
picture(invalid.split('Mood:')[0],'invalid_validation.png')

log=subprocess.check_output(['git','log','--oneline','--graph','--all'],cwd=root,text=True)
detail=subprocess.check_output(['git','log','--format=%h %an <%ae> %aI %s','--reverse'],cwd=root,text=True)
assets.joinpath('git_history.txt').write_text(log)
assets.joinpath('git_history_authors.txt').write_text(detail)
picture(log,'git_capture.png',20)
print('Captured actual interactive runs, complete source extracts and current Git evidence.')
