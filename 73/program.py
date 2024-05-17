import my_html
import os


def es73(dir, htmlFile):
    """Define the recursive function (or a function that uses one of your
    recursive functions) es73(dir, htmlfile) that, given a directory
    name, reads its structure and recursively constructs the
    my_html.HTMLNode node tree of an html document to be saved in a
    file.
    Arguments:
        dir:      path to the root directory to scan
        htmlFile: path of html file to write

    All files and directories starting with '.' must be ignored.

    The tree to be built must contain a series of bulleted lists that
    list the files and directories found according to the structure:
    <ul>
        <li>rootDir
            <ul>
                <li>fileName</li>
                <li>dirName
                    <ul>
                    <li>fileName</li>
                    <li>fileName</li>
                    </ul>
                </li>
                <li>fileName</li>
                <li>dirName
                    <ul>
                    <li>fileName</li>
                    <li>fileName</li>
                    </ul>
                </li>
            </ul>
        </li>
    </ul>
    (note, the structure is indented for the sake of clearness, but it
    should not be done to pass all the tests).  To produce the HTML
    file shown, first build the my_html.HTMLNode tree and then
    save it to file.  The tree should contain a node with tag=\"ul\" for
    each directory. Inside the tag 'ul' there should be as many tag='li' as
    the number of file/dir contained (in alphabetical order).  Each
    'li' tag contains the file/dir name (in the form of a
    tag='_text_').  If it is a directory, after the tag '_text_' a tag
    'ul' is added which lists the contents of the directory.  The
    function also returns the built tree.

    """
    # insert here your code
