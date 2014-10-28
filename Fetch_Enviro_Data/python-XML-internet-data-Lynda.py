#  Purpose of this script:
# To fetch xml formatted data from the internet, parse, and visualize it

import xml.dom.minidom


def main():
    # Get the content of interest from xml file for parsing and printing #
    doc = xml.dom.minidom.parse("sample.xml")
     
    # print out the document node and the name of the first child tag
    print doc.nodeName
    print doc.firstChild.tagName
    
    # get a list of XML tags from the document and print each one
    skills = doc.getElementsByTagName("skill")
    print("{} skills".format(skills.length))
    for skill in skills:
        print(skill.getAttribute("name"))
    
    # create a new XML tag and add it into the document
    newSkill = doc.createElement("skill")
    newSkill.setAttribute("name", "jQuery")
    doc.firstChild.appendChild(newSkill)
    print("\n")
    
    # get a list of XML tags from the document and print each one
    skills = doc.getElementsByTagName("skill")
    print("{} skills".format(skills.length))
    for skill in skills:
        print(skill.getAttribute("name"))
    
if __name__ == "__main__" :
    main()