'''
Created on 07/03/2012

@author: Steve Cassidy
'''

import css

PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en" style="
    margin-left: 10%;
    margin-right: 10%;
    text-align: center;
">
  <head>
     """ + css.STYLE + """
    <title>%title</title>
  </head>

  <body>
    <header><h1>%title</h1></header>

    <nav>
      %navigation
    </nav>

    %form

    <div class="content">
      <p id='message'>%message</p>

      %content
    </div>
    <footer>
      <p>&copy; Jackson Dale, 2015</p>
    </footer>

  </body>
</html>
"""

XML_THROW = '<form method=POST><fieldset>\
                           <legend>Generate your XML</legend>\
                               <table><tr><td>Enter in your excel table</td><td>\
                                    <tr><td colspan=2><textarea cols=200 rows=30 name=\'excel\' style=\'width:100%\';>Enter a your excel files...</textarea></td></tr>\
                                    <tr><td colspan=2><input type=\'submit\' value=\'Generate XML\'></td></tr></fieldset>\
                                    </form>\
                            <table>'

XML_RETURN = '<h2>Download your xml file</h2>' \
             '<a href="http://localhost:63342/job_import/Output.xml" download>XML FILE</a>' \
             '<br>' \
             'Download the xml file. Zip it and upload it to /home/oracle. Then import it via emcli.' \



def navigation(links):
    """Generate a set of navigation links enclosed in 
    a <nav></nav> element from a list of
    links, each link is a pair (url, text) which is 
    turned into the HTML <a href="url">text</a>, each
    link is embedded in a <li> inside a <ul> which is
    embedded in a <nav>. 
    Return the HTML as a string"""
    
    nav = "<ul>\n"
    for link in links:
        nav += "<li><a href='%s'>%s</a></li>\n" % link
    nav += "</ul>\n"
    
    return nav
    
def table(headings, data):
    """Generate an HTML table with column
    headings taken from the list headings (a list of strings) 
    and the cell entries taken from data (a list of lists).
    Return a string containing the generated table HTML"""
    
    #print 'data, ', data
    
    table = "<table><tr>"
    for head in headings:
        table += "<th>"+head+"</th>"
    table += "</tr>\n"
    for row in data:
        table += "<tr>"
        for cell in row:
            table += "<td>"+cell+"</td>"
        table += "</tr>\n"
    table += "</table>\n"
    
    return table


def generate_page(title, content, template):
    """Generate an HTML page by substituting the given
    title (a string)  wherever %title
    appears in the given page template and for every 
    key in the dictionary content, substitute the value
    whereever %key occurs. 
    If there are any remaining %xxxx occurences in the
    page that have not been replaced, they should be 
    removed.
    Return a string
    containing the generated HTML page"""
    
    import re
    
    page = template.replace("%title", title)
    for key in content.keys():
        page = page.replace("%"+key, content[key])
    
    page = re.sub("%[a-z]+", "", page)
    
    return page
