import os

def getFileListToArray():
    elements = [x for x in os.listdir(directory_path) if path.isfile(directory_path+os.sep+x)]
    return elements
    
def writeToFile( fontFamily, fontName, fontFormat ):
    CSSFile = open( 'fonts/fonts.css', 'ab+' )
    elements = getFileListToArray()

    for i in elements:
        if i is 'gitLog' or i is 'fonts.css':
            continue

        else:
            CSSFile.write( '@font-face {\n' )
            CSSFile.write( '    font-family:\'' + i + "\';\n" )
            CSSFile.write( '    src:url(\"' + fontName + "\") format(\'" + fontFormat + "\');\n"  )
            CSSFile.write( '}\n\n' )

    CSSFile.close()
