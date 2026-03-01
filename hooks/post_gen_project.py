import os
import shutil

create_docs = "{{ cookiecutter._create_docs }}"
module_name = "{{ cookiecutter.package_name | lower | replace('-', '_') }}"

if __name__ == "__main__":
    if create_docs != "yes":
        shutil.rmtree("docs", ignore_errors=True)
        os.remove(".github/workflows/docs_build_and_deploy.yml")
        os.remove(f"{module_name}/greetings.py")
        os.remove(f"{module_name}/math.py")
    shutil.rmtree("licenses", ignore_errors=True)
