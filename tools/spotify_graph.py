"""Conceptual Clayton graph. Vertical coordinates are illustrative, not measurements."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'assets' / 'spotify_clayton_graph.png'
W, H = 2400, 1420
INK = '#193048'; RED = '#D84A42'; PINK = '#B6389B'; YELLOW = '#F5CE26'
GREEN = '#12A85D'; BLUE = '#4279C4'; MUTE = '#5C6B77'

def font(size, bold=False):
    name = 'DejaVuSans-Bold.ttf' if bold else 'DejaVuSans.ttf'
    return ImageFont.truetype('/usr/share/fonts/truetype/dejavu/'+name,size)

def arrow(d, start, end, color, width=10, head=23):
    import math
    d.line([start,end], fill=color, width=width)
    dx=end[0]-start[0];dy=end[1]-start[1];a=math.atan2(dy,dx)
    p=[end,(end[0]-head*math.cos(a-.47),end[1]-head*math.sin(a-.47)),
       (end[0]-head*math.cos(a+.47),end[1]-head*math.sin(a+.47))]
    d.polygon(p,fill=color)

def dotted(d, y, color):
    for x in range(246,1885,40):d.line([(x,y),(min(x+25,1885),y)],fill=color,width=6)
    arrow(d,(1850,y),(1890,y),color,width=6,head=25)

def draw_graph(path=OUT):
    im=Image.new('RGB',(W,H),'white');d=ImageDraw.Draw(im)
    d.text((120,40),'SPOTIFY vs CDs  |  CLAYTON DISRUPTIVE MODEL',fill=INK,font=font(48,True))
    d.text((120,106),'Your technology: Spotify on-demand music streaming',fill=MUTE,font=font(28))
    x0=250; x1=1880; y0=1160; yt=245
    arrow(d,(x0,y0),(x1+60,y0),INK,6,24);arrow(d,(x0,y0),(x0,yt-30),INK,6,24)
    # The incumbent line is almost level: the CD's 16-bit/44.1 kHz format is fixed.
    arrow(d,(330,425),(1770,385),YELLOW,24,61)
    d.text((560,281),'ESTABLISHED MARKET TECHNOLOGY TRAJECTORY',fill=INK,font=font(27,True))
    d.text((800,319),'CD / physical recorded music',fill=INK,font=font(25))
    # Qualitative streaming progression. The 2017 revenue marker is only on X.
    points=[(375,1028),(456,945),(945,862),(1109,838),(1678,781),(1760,395)]
    d.line(points,fill=GREEN,width=26,joint='curve');arrow(d,points[-2],points[-1],GREEN,24,61)
    d.text((1010,920),'EMERGING MARKET TECHNOLOGY TRAJECTORY',fill='#087347',font=font(27,True))
    d.text((1220,958),'Spotify / streaming',fill='#087347',font=font(25))
    dotted(d,505,RED);dotted(d,853,PINK)
    d.text((1920,467),'HIGH END',fill=RED,font=font(25,True))
    d.text((1920,502),'Lossless-focused',fill=INK,font=font(23))
    d.text((1920,533),'CD listeners',fill=INK,font=font(23))
    d.text((1920,811),'LOW END',fill=PINK,font=font(25,True))
    d.text((1920,846),'Listeners accepting',fill=INK,font=font(23))
    d.text((1920,877),'compressed audio',fill=INK,font=font(23))
    # The lecturer's curved new-performance callout denotes different customer value.
    d.arc((720,500,1040,800),20,155,fill=BLUE,width=17)
    arrow(d,(1008,735),(1030,700),BLUE,15,32)
    d.text((537,560),'NEW PERFORMANCE',fill=BLUE,font=font(23,True))
    d.text((584,596),'TRAJECTORY',fill=BLUE,font=font(23,True))
    d.text((527,637),'On-demand access',fill=BLUE,font=font(22))
    d.text((584,671),'and discovery',fill=BLUE,font=font(22))
    # Values are event years, not calibrated horizontal distances for fidelity.
    years=[(375,'2008'),(945,'2015'),(1109,'2017'),(1760,'2025')]
    for x,label in years:
        d.line([(x,y0-8),(x,y0+13)],fill=INK,width=4)
        box=d.textbbox((0,0),label,font=font(26,True));d.text((x-(box[2]-box[0])/2,y0+27),label,fill=INK,font=font(26,True))
    d.text((900,1250),'TIME  (actual years)',fill=INK,font=font(30,True))
    # Rotated axis label.
    txt=Image.new('RGBA',(850,85),(255,255,255,0));td=ImageDraw.Draw(txt)
    td.text((0,0),'PERFORMANCE: delivered digital audio fidelity',fill=INK,font=font(30,True))
    rot=txt.rotate(90,expand=True);im.paste(rot,(88,304),rot)
    d.text((285,1320),'2008 launch  |  2009 mobile  |  2015 discovery  |  2017 industry streaming revenue lead  |  2025 Premium Lossless',fill=MUTE,font=font(20))
    d.text((285,1362),'Conceptual placement only. 2017 revenue is an industry outcome, not audio parity; CD format remains fixed.',fill=MUTE,font=font(19))
    path.parent.mkdir(parents=True,exist_ok=True);im.save(path)
    return path

if __name__ == '__main__': print(draw_graph())
