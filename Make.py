#!/usr/bin/python3
import io,re,subprocess
import docx,docx.shared,htmldocx

def doc(html,filename):
    html = re.sub('<a .*?</a>','',html)
    html = re.sub('<p>[ \n]*<br.*?></p>','',html,re.S|re.M)
    html = re.sub('<br.*?>','',html)
    document = docx.Document()
    style = document.styles['Normal']
    font = style.font
    font.name = 'Arial'
    font.size = docx.shared.Pt(10)
    style = document.styles['Heading 3']
    font = style.font
    font.name = 'Arial'
    font.size = docx.shared.Pt(14)
    htmldocx.h2d.LIST_INDENT = 0.1
    htmldocx.HtmlToDocx().add_html_to_document(html, document)
    document.save(filename)

src = open('srl.md').read()
out = open('srl.html','w')
out.write(re.search('^(.*<body>.)', src, re.S|re.M).group(1))
out.flush()
subprocess.Popen(['markdown'], stdin=subprocess.PIPE, stdout=out).communicate(re.search('<body>(.*)$', src, re.S).group(1).encode('utf8'))
srl = open('srl.html').read()
l = re.findall('<blockquote>(.*?)</blockquote>', srl, re.S|re.M)

doc(l[0], 'srl_bp.docx')
doc(l[1], 'srl_acte.docx')
doc(l[3], 'srl_banque.docx')

