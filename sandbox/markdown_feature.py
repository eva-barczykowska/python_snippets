# import markdown2
#
# md_text = '''
# # To Do
# ## At Home
# * Wash dishes
# ## At Work
# * Finish Report
# '''
#
# html_text = markdown2.markdown(md_text)
# print(html_text)


# # version 2
# from markdown2 import markdown
# md_text = '''
# # To Do
# ## At Home
# * Wash dishes
# ## At Work
# * Finish Report
# '''
#
# html_text = markdown(md_text)
# print(html_text)

# version 2
# from markdown2 import markdown as mx
# md_text = '''
# # To Do
# ## At Home
# * Wash dishes
# ## At Work
# * Finish Report
# '''
#
# html_text = mx(md_text)
# print(html_text)


# try:
#     1/0
# except Exception as e:
#     print(f"An error occurred: {e}") # instance of the Exception class!

# try:
#     1/0
# except Exception:
#     print(f"An error occurred: {Exception}")  # Exception class

#
import markdown2

markdown_content = '[To read](https://example.com)'
html_content = markdown2.markdown(markdown_content)
print(html_content)

markdown_table = """
| Header 1 | Header 2 |
| --- | --- |
| Row 1, Col 1 | Row 1, Col 2 |
| Row 2, Col 1 | Row 2, Col 2 |
"""
html_content = markdown2.markdown(markdown_table, extras=["tables", "code-friendly", "fenced-code-blocks"])

print(html_content)

# import markdown  # another possible library
# html = markdown.markdown("[abc](http://example.com)")
# print(html)
