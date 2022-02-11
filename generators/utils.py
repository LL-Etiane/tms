from django.template.loader import get_template
from xhtml2pdf import pisa
from io import BytesIO

def generatePDF(template,context):
    template = get_template(template)
    html = template.render(context)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")),result)
    if not pdf.err:
        return result
    else: 
        return None