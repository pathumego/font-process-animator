import os, sys

count = 1

def cpFile( fileName, fileDir ):
    global count
    os.system( 'cp ' + fileDir + fileName + ' ' + 'temp/' + str( count ) + '_' + fileName )
    count += 1

def rollCommits( fileName, fileDir, gitHash ):
    os.system( 'cd ' + fileDir + ' && git checkout ' + gitHash + ' ' + fileName )
    os.system( 'cd - > /dev/null' )

def genGitLog( fileName, fileDir ):
    os.system( 'mkdir -p temp' )
    os.system( 'cd ' + fileDir + '&& git log --pretty=%h ' + fileName + ' > gitLog' )
    os.system( 'cd - > /dev/null' )

def gitLogToArray( fileDir ):
    hashArray = open( fileDir + 'gitLog' ).read().splitlines()
    ##print( hashArray )
    return hashArray

def process( fileName, fileDir ):
    genGitLog( fileName, fileDir )
    hashArray = gitLogToArray( fileDir )
    for hashNum in hashArray:
        rollCommits( fileName, fileDir, hashNum )
        cpFile( fileName, fileDir )

def main( argv ):
    fileName = fileDir = ""
    if '-f' in argv:
        fileName = argv[ argv.index( '-f' ) + 1 ]
        ##print( fileName )
        if '-i' in argv:
            fileDir = argv[ argv.index( '-i' ) + 1 ]
            ##print( fileDir )
            process( fileName, fileDir )
        else:
            print( "no file location is given." )
            print( "Usage : python3 gen.py -i [fileDirectory] -f [fileName]" )
    else:
        print( "no input file is given." )
        print( "Usage : python3 gen.py -i [fileDirectory] -f [fileName]" )

if __name__ == "__main__":
    main( sys.argv )

