import xml.etree.ElementTree as ET


def manage_student_xml():
  tree = ET.parse("students.xml")
  root = tree.getroot()

  for student in root.findall("student"):
    if student.get("id") == "101":
      student.find("cgpa").text = "8.5"

  new_student = ET.Element("student", id="111")
  ET.SubElement(new_student, "name").text = "Pooja Roy"
  ET.SubElement(new_student, "department").text = "CSE"
  ET.SubElement(new_student, "year").text = "2"
  ET.SubElement(new_student, "email").text = "pooja.roy@example.com"
  ET.SubElement(new_student, "cgpa").text = "9.0"
  root.append(new_student)

  tree.write("updated_students.xml", encoding="utf-8", xml_declaration=True)
  print(
      "XML document updated and saved successfully as 'updated_students.xml'."
  )


if __name__ == "__main__":
  manage_student_xml()
