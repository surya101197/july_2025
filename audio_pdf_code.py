from pypdf import PdfReader #PdfReader ane method ni pypdf dependency nunchi import cheskunaam.
from gtts import gTTS #gTTs ane method ni gtts module nunchi import cheskunaam 

#Pdfreader pdf file ni chaduvuthaadhi
reader=PdfReader("mirror_world_story.pdf")

#text varial Pdf lo unna texts ni store cheydaniki
text=""

#pdf lo unna pages in loop chesthaadhi
for page in reader.pages:
#page_text ane oka variable pdf no unna information antha theeskuntadhi(endhukante .extract_text() use chesaam kabtti)(page loop to print avthunna prathee sari) read chesthadhi adhi kuda text format lo unnavi matrame
    page_text=page.extract_text()
#if condition endhuku use chesaam ant ee page_text ane variable nijanga page lo unna texts in extract chesindho ledho ani endhukate akkada .extract_text() ane method use chesam kabatti so method successfull ayndho ledho ani if tho check chestam
if page_text:
#pyna unna if condition true aythe kindha statement to extract ayna texts anni kuda mundhu create chesina text variable to store avthaadhi
    text+=page_text
#pyna unna anni lines of code to text and pdf tho pani aypendhi ippudu oka variable create cheyali text ni speech lo store cheydaniki, so gTTS ane class to manam store cheskunna text in insert chestham so text antha audio lo convert avthaadhi
speech=gTTS(text)
#kind statement lo convert chesina audio file in mp3 ki marustam, mari audio file to extension .mp3 kada, .pdf or .text or .mp4 kadhu kada. So marchina dhaanni .save tho save chestam so file create avhadhi audio laage
speech.save("mirror_world_story.mp3")
