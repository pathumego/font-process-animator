import os, sys

prefix = 1

def cpFile( fileName, fileDir ):
    os.system( 'cp ' + fileDir + fileName + ' ' + 'temp/' + str( prefix ) + '_' + fileName )
    prefix =+ 1

def rollCommits( fileName, fileDir, gitHash ):
    os.system( 'git checkout ' + hashNum )

def genGitLog( fileName, fileDir ):
    os.system( 'mkdir -p temp' )
    os.system( 'git log --pretty=%h ' + fileDir + fileName + ' > temp/gitLog' )

def gitLogToArray( logDir ):
    hashArray = open( 'temp/gitLog' ).read().splitlines()
    return hashArray

def process( fileName, fileDir ):
    genGitLog( fileName, fileDir )
    hashArray = gitLogToArray()
    for hashNum in hashArray:
        rollCommits( fileName, fileDir )
        cpFile( fileName, fileDir )

def main( argv ):
    fileName = fileDir = ""
    if '-f' in argv:
        fileName = argv[ argv.index( '-f' ) + 1 ]
        if '-i' in argv:
            fileDir = argv[ argv.index( '-i' ) + 1 ]
        else:
            print( "no file location is given." )
    else:
        print( "no input file is given." )

if __name__ == "__main__":
    main( sys.argv )
