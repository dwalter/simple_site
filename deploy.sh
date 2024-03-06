# make the app name the name of the current directory
service_name=$(basename $(pwd))

# cp the files to the appropriate locations

# sync the frontend files
mkdir -p /var/www/$service_name;
cp frontend/* /var/www/$service_name/;

# sync the backend files
mkdir -p /var/www/$service_name/backend;
cp backend/* /var/www/self_system_app/backend/;


# copy the backend service file to the appropriate location
# TODO

# # sync the backend service file:
# cp backend_service/self_system_app_backend.service \
#   /etc/systemd/system/self_system_app_backend.service;

# # sync the nginx config file:
# cp nginx/self_system_app \
#   /etc/nginx/sites-available/self_system_app;
# # symlink the nginx config file:
# if [ ! -L /etc/nginx/sites-enabled/self_system_app ]; then
#     sudo ln -s \
#   /etc/nginx/sites-available/self_system_app \
#   /etc/nginx/sites-enabled/self_system_app
# fi

# # restart the frontend and backend servers

# # enable the backend service on boot:
# sudo systemctl enable self_system_app_backend.service;
# # restart the backend service that runs `python app.py`:
# sudo systemctl restart self_system_app_backend.service;

# # restart the nginx server which hosts the frontend
# # also reverse proxies the backend
# sudo systemctl enable nginx;
# sudo systemctl restart nginx;
