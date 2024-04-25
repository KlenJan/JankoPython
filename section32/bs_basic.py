from bs4 import BeautifulSoup
html_var = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html_var, "html.parser")
print(soup.body)
print(soup.body.div)
d = soup.select("[data-example]")
print(d)
d = soup.find_all("div")
print(d)
d = soup.find(id="first")
print(d)
# have to use class_ because class is reserver python keyword
d = soup.find(class_="special")
print(d)
d = soup.select(".special")[0]
print(d.getText())
d = soup.find_all(attrs={"data-example": "yes"})
print(d)


d = soup.body.contents
print(d)
d = soup.body.contents[1].next_sibling.next_sibling
print(d)
