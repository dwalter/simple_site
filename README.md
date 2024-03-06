# simple_site
Simple program that sets up an nginx server to run a html frontend and flask backend

## Getting Started

### Installation
```
pip install .
```

### Requirements
The following are not provided, so you'll need to have these ready
- index.html (frontend entrypoint)
- app.py (Flask backend entrypoint)

- A machine compatible with running systemctl. Ubuntu OS is recommended.

### To run
To run `simple_site`, go to the directory with your frontend and backend entrypoints and run
```
sudo simple_site deploy
```

and your site will automatically deploy to your current machine. This will setup an nginx server that runs your frontend and backend. Once the deployment is complete go to the provided url to access your site.
