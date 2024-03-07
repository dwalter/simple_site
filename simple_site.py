import os
from pkg_resources import resource_filename
import argparse
import requests

def handle_deploy(service_name, port, public_ip):
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
    # os.system(f"bash deploy.sh {service_name}")

    # # sync the frontend files
    # mkdir -p /var/www/$service_name;
    # cp frontend/* /var/www/$service_name/;
    os.makedirs(f"/var/www/{service_name}", exist_ok=True)
    os.system(f"cp frontend/* /var/www/{service_name}/")

    # sync the backend files
    # mkdir -p /var/www/$service_name/backend;
    # cp backend/* /var/www/self_system_app/backend/;
    os.makedirs(f"/var/www/{service_name}/backend", exist_ok=True)
    os.system(f"cp backend/* /var/www/{service_name}/backend/")

    # create the nginx config from the template

    if public_ip is None:
        public_ip = get_public_ip()

    nginx_template = None
    with open("nginx_template", 'r') as f:
        nginx_template = f.read()

    nginx_config = nginx_template.replace('<service_name>', service_name)
    nginx_config = nginx_config.replace('port', port)
    nginx_config = nginx_config.replace('public_ip', public_ip)

    with open(f"/etc/nginx/sites-available/{service_name}", 'w') as f:
        f.write(nginx_config)

    # # symlink the nginx config file:
    # if [ ! -L /etc/nginx/sites-enabled/self_system_app ]; then
    #     sudo ln -s \
    # /etc/nginx/sites-available/self_system_app \
    # /etc/nginx/sites-enabled/self_system_app
    # fi
    # if not os.path.exists(f"/etc/nginx/sites-enabled/{service_name}"):
    os.symlink(
        f"/etc/nginx/sites-available/{service_name}",
        f"/etc/nginx/sites-enabled/{service_name}"
    )

    # enable the backend service on boot:
    os.system(f"sudo systemctl enable {service_backend_name}.service")
    # restart the backend service that runs `python app.py`:
    os.system(f"sudo systemctl restart {service_backend_name}.service")

    # restart the nginx server which hosts the frontend
    # also reverse proxies the backend
    os.system("sudo systemctl enable nginx")
    os.system("sudo systemctl restart nginx")


def get_public_ip():
    response = requests.get('https://api.ipify.org')
    return response.text

def main(service_name, deploy, port, public_ip):

    if not deploy:
        return

    handle_deploy(service_name, port, public_ip)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Create a simple site')
    parser.add_argument('service_name', type=str)
    parser.add_argument("deploy", type=bool, default=False)
    parser.add_argument("port", type=int, default=8081)
    parser.add_argument("public_ip", type=str, default=None)

    service_name = parser.parse_args().service_name
    deploy = parser.parse_args().deploy
    port = parser.parse_args().port
    public_ip = parser.parse_args().public_ip
    main(service_name, deploy, port, public_ip)
