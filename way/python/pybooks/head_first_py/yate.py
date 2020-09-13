from string import Template


def start_response(resp="text/html"):
    return f'Content-type: {resp}\n\n'

def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return header.substitute(title=the_title)

def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()

    link_string = ""
    for key in the_links:
        link_string += f'<a href="{the_links[key]}">{key}</a>&nbsp;&nbsp;&nbsp;&nbsp;'
    footer = Template(foot_text)
    return footer.substitute(links=link_string)

def start_form(the_url, form_type="POST"):
    return f'<form action="{the_url}" method="{form_type}">'

def end_form(submit_msg="Submit"):
    return f'<p></p><input type="submit" value="{submit}"></form>'

def radio_button(rb_name, rb_value):
    return f'<input type="radio" name="{rb_name}" value="{rb_value}"> {rb_value}<br/>'

def u_list(items):
    return f'<ul>{"".join([f"<li>{item}</li>" for item in items])}</ul>'
# print(u_list(["a", "b", "c"]))

def header(header_text, header_level=2):
    return f'<h{header_level}>{header_text}</h{header_level}>'
# print(header("Hello", 5))

def paragraph(para_text):
    return f'<p>{para_text}</p>'