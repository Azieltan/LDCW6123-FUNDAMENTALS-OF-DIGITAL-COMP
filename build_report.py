from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4,A3,landscape
from reportlab.lib.colors import HexColor,white
from reportlab.lib.utils import ImageReader
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from pypdf import PdfReader,PdfWriter
from pathlib import Path
from io import BytesIO
from PIL import Image
P=Path(__file__).parent; O=P/'output';O.mkdir(exist_ok=True)
FONT='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf';BOLD='/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf';MONO='/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'
pdfmetrics.registerFont(TTFont('DV',FONT));pdfmetrics.registerFont(TTFont('DVB',BOLD));pdfmetrics.registerFont(TTFont('DVM',MONO))
NAVY=HexColor('#173247'); TEAL=HexColor('#187F85'); LIGHT=HexColor('#EAF3F2'); AMBER=HexColor('#DB9935'); INK=HexColor('#203544'); GRAY=HexColor('#61717B')
style=ParagraphStyle('body',fontName='DV',fontSize=10.3,leading=15,textColor=INK,spaceAfter=8)
small=ParagraphStyle('small',parent=style,fontSize=8.5,leading=12)
def para(c,t,x,y,w,sty=style):
 p=Paragraph(t,sty);_,h=p.wrap(w,1000);p.drawOn(c,x,y-h);return y-h-sty.spaceAfter
def head(c,title,num=None):
 w,h=A4;c.setFillColor(NAVY);c.rect(0,h-82,w,82,fill=1,stroke=0);c.setFillColor(white);c.setFont('DVB',20);c.drawString(43,h-52,title)
 c.setFillColor(GRAY);c.setFont('DV',8)
 if num:c.drawRightString(w-42,30,str(num))
def rule(c,y):c.setStrokeColor(HexColor('#D7E3E4'));c.line(43,y,A4[0]-43,y)
def page_toc():
 b=BytesIO();c=canvas.Canvas(b,pagesize=A4);head(c,'Contents',3);y=745
 for label,num in [('Assessment coversheet and declarations','1-2'),('Part 1  Innovation life cycle poster','4'),('Part 1  Analysis and model application','5'),('Part 1  APA references','6'),('Part 2  Program design and code capture','7'),('Part 2  Test cases and actual program output','8'),('Part 2  Git development log','9'),('Presentation plan and required video link','10')]:
  c.setFont('DV',11);c.setFillColor(INK);c.drawString(48,y,label);c.drawRightString(544,y,num);rule(c,y-11);y-=47
 y-=25;c.setFont('DVB',12);c.drawString(48,y,'Completion fields for the group');y-=25
 y=para(c,'Complete every field and individual declaration on the attached coversheet. Insert the actual OneDrive recording link on page 10. The captured Git history documents preparation of this AI-assisted draft; group members must add their own reviewed contributions.',48,y,495)
 c.save();return b.getvalue()
def card(c,x,y,w,h,kicker,title,body):
 c.setFillColor(white);c.roundRect(x,y,w,h,10,fill=1,stroke=0)
 c.setFillColor(TEAL);c.setFont('DVB',11);c.drawString(x+15,y+h-23,kicker)
 c.setFillColor(NAVY);c.setFont('DVB',14);c.drawString(x+15,y+h-48,title)
 para(c,body,x+15,y+h-59,w-30,small)
def poster():
 W,H=landscape(A3);b=BytesIO();c=canvas.Canvas(b,pagesize=(W,H));c.setFillColor(HexColor('#F4F8F8'));c.rect(0,0,W,H,fill=1,stroke=0)
 c.setFillColor(NAVY);c.rect(0,H-104,W,104,fill=1,stroke=0)
 c.setFillColor(white);c.setFont('DVB',28);c.drawString(42,H-54,'NETFLIX AND VIDEO RENTAL DISRUPTION')
 c.setFont('DV',12);c.drawString(44,H-79,'Christensen model  |  entrant: DVD by mail  |  incumbent: Blockbuster stores')
 c.setFillColor(NAVY);c.setFont('DVB',15);c.drawString(43,H-139,'The market being disrupted: in-store DVD and video rental')
 para(c,'The model requires a foothold with customers poorly served by the incumbent, an initially weaker offer on a traditional performance measure, and improvement that reaches the mainstream. Netflix initially lacked same-day pickup but offered broad selection, mail delivery and a subscription model [1, 2].',43,H-151,W-86,style)
 y=H-365; gap=12;cw=(W-86-4*gap)/5
 cards=[
 ('1998','ENTRY','Online DVD rental begins; customers order from home. No store visit is required [3].'),
 ('2000s','FOOTHOLD','Mail and the internet extend access beyond convenient store locations; immediate viewing remains weaker [1].'),
 ('2002','IMPROVEMENT','Regional distribution and CineMatch help access and discovery; the subscription gains scale [4, 5].'),
 ('2007','UPMARKET','Streaming adds immediate online viewing. This is a later improvement to Netflix, not its original foothold [6].'),
 ('2010-23','MARKET SHIFT','Blockbuster enters bankruptcy in 2010; Netflix ends its DVD service in 2023 [1, 7].')]
 for i,(k,t,body) in enumerate(cards):card(c,43+i*(cw+gap),y,cw,184,k,t,body)
 c.setStrokeColor(AMBER);c.setLineWidth(3);c.line(55,y-28,W-55,y-28)
 for i in range(5):
  x=43+i*(cw+gap)+cw/2;c.setFillColor(AMBER);c.circle(x,y-28,5,fill=1,stroke=0)
 c.setFillColor(NAVY);c.setFont('DVB',13);c.drawString(43,y-72,'INCUMBENT PERFORMANCE');c.drawString(W/2+15,y-72,'NEW VALUE AND SOCIAL IMPACT')
 para(c,'Stores offered instant pickup and face-to-face browsing. DVDs by mail were slower when a customer wanted a film that night [1]. Blockbuster later responded online, so its decline should not be attributed to a single invention alone.',43,y-84,W/2-72,small)
 para(c,'Home ordering, access to a wider catalogue away from stores, and fewer trips improved convenience for some users [1, 2]. The later move to streaming changed the way subscribers could watch and increased dependence on internet access [6].',W/2+15,y-84,W/2-63,small)
 c.setFillColor(TEAL);c.roundRect(43,78,W-86,102,10,fill=1,stroke=0)
 c.setFillColor(white);c.setFont('DVB',13);c.drawString(60,158,'WHY THIS IS DISRUPTION')
 s=ParagraphStyle('white',parent=small,textColor=white,fontSize=9.4,leading=14)
 para(c,'Netflix began with a different value network: web ordering, postal delivery, distribution centres and no retail-store estate. It traded away immediate pickup while serving less convenient locations and customers interested in choice. Subsequent improvements made the offer more competitive with store rental. This is an application of Christensen\'s model, not proof that every later Netflix feature was itself a disruptive innovation [1, 2].',60,148,W-120,s)
 c.setFillColor(GRAY);c.setFont('DV',8);c.drawString(44,48,'[1]-[7] source details on the next report page. Dates reflect cited company records and Christensen Institute analysis.')
 c.save();return b.getvalue()
def analysis():
 b=BytesIO();c=canvas.Canvas(b,pagesize=A4);head(c,'Part 1  Model application',5);y=739
 y=para(c,'<b>Technology and unit of analysis.</b> Netflix is the case; the original innovation assessed is the DVD-by-mail rental service relative to Blockbuster\'s physical stores. The subsequent streaming service is a later stage of improvement. Defining the unit matters because calling streaming the original disruptive entry would erase the earlier mail-rental foothold.',43,y,505)
 y=para(c,'<b>Why the Christensen model fits.</b> Disruptive innovation is a process: an entrant starts with an offering that incumbents may regard as less attractive under existing measures, serves neglected or less convenient customers, then improves and competes more directly. The Christensen Institute identifies Netflix versus Blockbuster as a case and notes Netflix\'s early disadvantage in immediate access [1, 2].',43,y,505)
 y=para(c,'<b>Historical sequence.</b> Netflix had launched online DVD rental by 1998 [3]. By 2002 it described a subscription service with regional distribution and CineMatch-assisted selection [4, 5]. It introduced streaming in 2007 [6]. Blockbuster filed for bankruptcy in 2010 [1]. Netflix shipped its final DVDs on 29 September 2023 [7]. These dates mark changes in Netflix\'s offering and the incumbent market; they are not a claim that one event alone caused the next.',43,y,505)
 y=para(c,'<b>Market and social consequences.</b> Mail rental helped people access a wider choice of titles without travelling to a store, especially where stores were inconvenient [1]. The trade-off was waiting for delivery; streaming later removed that wait for viewers with adequate internet access. The analysis concerns convenience, access and rental-market competition. It does not establish that every consumer benefited equally.',43,y,505)
 y=para(c,'<b>Critical limitation.</b> The case is often compressed into a simple tale of a better technology defeating a worse one. Christensen\'s mechanism is more specific: the initial service was weaker at immediate pickup, and its postal and internet value network mattered. Incumbent responses, changes in consumer behaviour and streaming also contributed. The poster therefore distinguishes the initial disruptive trajectory from later product evolution.',43,y,505)
 y=para(c,'<b>Part 2 connection.</b> The C++ assistant mirrors one customer-facing benefit of an online catalogue: discovering a suitable title through preferences. It uses explicit scoring rules and a fictional catalogue; it is not Netflix software or a recreation of the proprietary CineMatch system.',43,y,505)
 c.save();return b.getvalue()
refs=[
'[1] Christensen Institute. (n.d.). <i>Disruptive innovation theory</i>. https://www.christenseninstitute.org/theory/disruptive-innovation/',
'[2] Christensen, C. M., Raynor, M. E., &amp; McDonald, R. (2015). What is disruptive innovation? <i>Harvard Business Review</i>. https://hbr.org/2015/12/what-is-disruptive-innovation',
'[3] Netflix, Inc. (2002, May 22). <i>Netflix announces initial public offering</i>. https://ir.netflix.net/investor-news-and-events/financial-releases/press-release-details/2002/Netflix-Announces-Initial-Public-Offering/default.aspx',
'[4] Netflix, Inc. (2002). <i>Netflix announces opening of 10 regional distribution centers</i>. https://ir.netflix.net/investor-news-and-events/financial-releases/press-release-details/2002/Netflix-Announces-Opening-of-10-Regional-Distribution-Centers/default.aspx',
'[5] Netflix, Inc. (2002, March 6). <i>Netflix files registration statement for initial public offering</i>. https://ir.netflix.net/investor-news-and-events/financial-releases/press-release-details/2002/Netflix-Files-Registration-Statement-for-Initial-Public-Offering/default.aspx',
'[6] Netflix, Inc. (2018). <i>Annual report on Form 10-K</i>. https://ir.netflix.net/files/doc_financials/annual_reports/2018/Form-10K_Q418_Filed.pdf',
'[7] Netflix. (2023, April 18). <i>Netflix DVD: The final season</i>. https://about.netflix.com/en/news/netflix-dvd-the-final-season']
def reference_page():
 b=BytesIO();c=canvas.Canvas(b,pagesize=A4);head(c,'Part 1  References',6);y=737
 y=para(c,'Primary company records and the theory source support the historical milestones and model application shown on the poster. Number labels are used on the poster for compactness; full entries follow in APA style.',43,y,505)
 for r in refs:y=para(c,r,45,y-3,500,small)
 c.save();return b.getvalue()
def program_page():
 b=BytesIO();c=canvas.Canvas(b,pagesize=A4);head(c,'Part 2  Interactive C++ program',7);y=738
 y=para(c,'<b>Purpose.</b> The offline Movie Discovery Assistant recommends a fictional title using three customer choices: genre, mood and preferred duration. This illustrates catalogue discovery associated with Netflix\'s online rental service. The program is deliberately small and does not represent Netflix\'s real algorithm.',43,y,505)
 y=para(c,'<b>Inputs and output.</b> The menu accepts numbered genre, mood and length choices. It checks each input, scores films of the chosen genre (+2 for mood, +1 for length), and displays the best match with a brief reason. If no exact mood or duration match exists, it still returns a film from the chosen genre and explains the actual matches.',43,y,505)
 y=para(c,'<b>Implementation.</b> C++17; <font name="DVM">Movie</font> structure; <font name="DVM">vector</font> catalogue; a reusable bounded-input function; a loop for another recommendation. Full source and a reproducible build command are in <font name="DVM">src/main.cpp</font> and the README in the companion project archive.',43,y,505)
 im=Image.open(P/'assets/code_capture.png');ratio=im.height/im.width;target=495;c.drawImage(str(P/'assets/code_capture.png'),49,y-target*ratio-9,width=target,height=target*ratio)
 c.setFillColor(GRAY);c.setFont('DV',8);c.drawString(49,50,'Code capture from the actual source file; source archive contains all remaining lines.')
 c.save();return b.getvalue()
def run_page():
 b=BytesIO();c=canvas.Canvas(b,pagesize=A4);head(c,'Part 2  Run and testing',8);y=733
 y=para(c,'<b>Actual run.</b> The captured output below comes from the compiled program. The first recommendation follows Comedy + Relaxed + Over 100 minutes. A second interaction shows repeated use. Movie names and descriptions are fictional.',43,y,505)
 im=Image.open(P/'assets/output_capture.png');r=im.height/im.width;w=500;c.drawImage(str(P/'assets/output_capture.png'),46,y-w*r-8,width=w,height=w*r);y-=w*r+28
 y=para(c,'<b>Verification.</b> The local test script compiled with <font name="DVM">-std=c++17 -Wall -Wextra -pedantic</font> and passed five scenarios: three genre/mood/length combinations, invalid text/out-of-range input, and a terminated input stream. The executable was run locally; no network or real subscriber information was involved.',43,y,505)
 c.save();return b.getvalue()
def git_page():
 b=BytesIO();c=canvas.Canvas(b,pagesize=A4);head(c,'Part 2  Development record',9);y=738
 y=para(c,'The history below is a real local Git log created while preparing this AI-assisted draft. It is not evidence that named students made these changes. The group should add its own reviewed commits and use its own project history when submitting.',43,y,505)
 im=Image.open(P/'assets/git_capture.png');r=im.height/im.width;c.drawImage(str(P/'assets/git_capture.png'),46,y-500*r-4,width=500,height=500*r);y-=500*r+30
 y=para(c,'<b>To continue development.</b> Change the recommendation logic or catalogue, run <font name="DVM">./test.sh</font>, commit the real change with a descriptive message, and generate an updated log with <font name="DVM">git log --oneline --graph</font>. The brief says "--online", which appears to be a typo; the valid Git option is "--oneline".',43,y,505)
 c.save();return b.getvalue()
def video_page():
 b=BytesIO();c=canvas.Canvas(b,pagesize=A4);head(c,'Presentation plan',10);y=737
 y=para(c,'<b>Recorded group video link (OneDrive):</b> _________________________________________________',43,y,505)
 y=para(c,'The assignment requires a recorded group presentation, at most 18 minutes, in MPEG, MP4 or MOV format. A group member must record the real presentation, upload it, and insert the working OneDrive link above.',43,y,505)
 for title,body in [('0:00-1:30  Introduce the case','State the incumbent rental market and the specific innovation: Netflix DVD by mail.'),('1:30-5:00  Explain the model','Describe foothold, initial performance disadvantage, improvement and market shift.'),('5:00-8:00  Walk through the poster','Cite the dates, point out the 2007 streaming transition, and discuss the social impact and limitations.'),('8:00-12:00  Demonstrate the code','Explain inputs, scoring and fallback; run two combinations and one invalid entry.'),('12:00-14:00  Show tests and Git history','Explain the real commits, five test scenarios and the distinction between draft and student work.'),('14:00-16:00  Conclude','Discuss what the poster shows and what the simple program cannot represent.')]:
  y=para(c,f'<b>{title}</b><br/>{body}',43,y-7,505)
 y=para(c,'<b>Before submission.</b> Complete and sign the supplied coversheet individually; add the actual section, group leader, student IDs and deadline fields; upload the group video; check that the video link and any code repository link are accessible; review citations and disclose AI assistance according to course rules.',43,y-3,505)
 c.save();return b.getvalue()
cover=P/'assets/cover_render/LDCW6123_Assessment_Coversheet.pdf'
w=PdfWriter();w.append(str(cover))
for fn in [page_toc,poster,analysis,reference_page,program_page,run_page,git_page,video_page]:
 w.append(PdfReader(BytesIO(fn())))
with open(O/'LDCW6123_Netflix_Project_Draft.pdf','wb') as f:w.write(f)
with open(O/'Netflix_Lifecycle_A3_Poster.pdf','wb') as f:f.write(poster())
print('pages',len(PdfReader(str(O/'LDCW6123_Netflix_Project_Draft.pdf')).pages))
