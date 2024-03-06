import os
from pkg_resources import resource_filename
# use args
import argparse

def handle_deploy(service_name):
    build_dir = "build"
    os.makedirs(build_dir, exist_ok=True)
    template_backend_path = resource_filename('simple_site', 'templates/template_backend.service')

    with open(template_backend_path, 'r') as f:
        template_backend_content = f.read()

    service_backend_name = f"{service_name}_backend"
    service_content = template_backend_content.replace('<service_name>', service_backend_name)

    # save the file
    with open(f"{build_dir}/{service_backend_name}.service", 'w') as f:
        f.write(service_content)

    # run the deploy.sh script
    os.system(f"bash deploy.sh {service_name}")

def main(service_name, deploy):

    if not deploy:
        return

    handle_deploy(service_name)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a simple site')
    parser.add_argument('service_name', type=str)
    parser.add_argument("deploy", type=bool, default=False)

    service_name = parser.parse_args().service_name
    deploy = parser.parse_args().deploy
    main(service_name, deploy)
