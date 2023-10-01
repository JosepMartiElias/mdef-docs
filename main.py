from jinja2 import Environment, FileSystemLoader
from mistune import html
import re
import os
import yaml

def define_env(env):
    
    @env.macro
    def insert_banner():

        environment = Environment(loader=FileSystemLoader("custom_theme/templates/"))
        template = environment.get_template("banner.html")

        vbls = env.page.meta.copy()
        if 'page_type' in env.page.meta:
            if env.page.meta['page_type'] == 'course':
                try:
                    with open(f"custom_theme/templates/{env.page.meta['track'].lower()}_icon.html") as file:
                        icon = file.read()
                    vbls['banner_icon'] = icon
                except:
                    pass
        result = template.render(vbls)

        return result

    def get_frontmatter(content):
        if '---\n' not in content:
            print ('No frontmatter in content')
            return None

        if '---\n' in content[1:]:
            frontmatter = yaml.load('\n'.join(content[1:content[1:].index('---\n')+1]), Loader=yaml.SafeLoader)
        else:
            frontmatter = None

        return frontmatter

    def render_markdown(markdown):
        return html(markdown)

    def create_faculty(faculty, custom_dir):
        environment = Environment(loader=FileSystemLoader(f"{custom_dir}/templates/"), autoescape=True)
        template = environment.get_template("faculty_item.html")

        faculty_path = 'docs/faculty'

        if os.path.exists(f"docs/faculty/{faculty}.md"):
            with open(os.path.join(faculty_path, f'{faculty}.md')) as _file:
                content = _file.readlines()

            frontmatter = get_frontmatter(content)
            if frontmatter is not None:
                vbls = frontmatter
                vbls['body'] = render_markdown(''.join(content[content[1:].index('---\n')+2:]))

                result = template.render(vbls)
                # TODO add custom_theme as environment variable
                with open(os.path.join(f"{custom_dir}/includes", f'{faculty}.html'), 'w') as _file:
                    _file.write(result)
        else:
            print (f"MACROS WARNING - {faculty}.md not found")

    @env.macro
    def insert_faculty():
        custom_dir = os.path.basename(os.path.normpath(env.conf.theme.custom_dir))

        if 'faculty' in env.page.meta:
            result = ''

            for faculty in env.page.meta['faculty']:
                create_faculty(faculty, custom_dir)

                if os.path.exists(f"{custom_dir}/includes/{faculty}.html"):
                    with open(f"{custom_dir}/includes/{faculty}.html") as file:
                        result += file.read()
                else:
                    print (f"{faculty}.html not found")

        return result

    @env.macro
    def insert_students():
        custom_dir = os.path.basename(os.path.normpath(env.conf.theme.custom_dir))

        environment = Environment(loader=FileSystemLoader(f"{custom_dir}/templates/"), autoescape=True)
        template = environment.get_template("students.html")

        if 'students' in env.page.meta:
            students = []
            for item in env.page.meta['students'].keys():
                students.append({'name': item,
                                 'photo': env.page.meta['students'][item]['photo'],
                                 'website': env.page.meta['students'][item]['website']
                                 })

            result = template.render(students=students)
            return result
        else:
            print ('Incorrectly configured')
            return None
