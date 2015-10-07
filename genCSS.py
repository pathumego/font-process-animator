import os

def getFileListToArray():
    elements = ( os.listdir('fonts/') )

    for element in elements:
        if element.endswith( '.css' ) or element.endswith( 'Log' ):
            elements.remove( element )

    elements.sort()
    return elements
    
def writeToFile( fontName, fontFormat ):
    CSSFile = open( 'fonts/fonts.css', 'ab+' )
    elements = getFileListToArray()

    for i in elements:
        CSSFile.write( bytes( "@font-face {\n", 'UTF-8' ) )
        CSSFile.write( bytes( '    font-family:\'' + i[ :-4 ] + "\';\n", 'UTF-8' ) )
        CSSFile.write( bytes( '    src:url(\"' + fontName + "\") format(\'" + fontFormat + "\');\n", 'UTF-8'  ) )
        CSSFile.write( bytes( '}\n\n', 'UTF-8' ) )

    CSSFile.close()
